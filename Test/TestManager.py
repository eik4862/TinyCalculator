import os
import statistics
import time
from decimal import Decimal
from typing import List, final, Union, Callable, TextIO, Final

from Core import Type, DB
from Function import Trigonometric, HyperbolicTrigonometric, SpecialFunction, Exponential
from Util import Printer


@final
class TestManager:
    """
    Run tests for numerical analysis.

    Test inputs and reference outputs are generated by MATLAB using arbitrary precision arithmetic.
    By default, the precision of inputs and outputs are 100 which is quite high.
    Test results are also processed and analyzed by MATLAB using arbitrary precision arithmetic.
    For detailed code and explanation, refer to comments in ``test_gen.m`` and ``plt_err.m``.
    For the concept of arbitrary precision arithmetic, consult the references below.

    This class is implemented as singleton.
    For the concept of singleton pattern, consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic
        * https://en.wikipedia.org/wiki/Singleton_pattern

    :cvar __MAX_PRINTOUT: Maximum # of lines of test results to be printed out.
    :cvar __inst: Singleton object.
    """
    __MAX_PRINTOUT: Final[int] = 10

    __inst = None

    @classmethod
    def inst(cls):
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: TestManager
        """
        if not cls.__inst:
            cls.__inst = TestManager()

        return cls.__inst

    def test(self, fun: Union[Type.FunT, Callable[[Decimal], Union[float, Decimal]]], verb: bool = False,
             id: str = None) -> None:
        """
        Run test, report with supplementary statistics and save the result.

        One should load test DB before calling this function.
        Otherwise, it will fail in unexpected way.
        The result will be stored as a text file as ``../Test/Test.out`` wrt. current working directory.

        :param fun: Function to be tested. Should be built-in function type or function handle which takes Decimal and
                    returns float or Decimal.
        :type fun: Union[Type.FunT, Callable[[Decimal], Union[float, Decimal]]]
        :param verb: Flag for verbose mode. (Default: False)
        :type verb: bool
        :param id: String expression of function to be tested.
                   This is only needed when the function to be tested is not built in. (Default: None)
        :type id: str
        """
        buf: Type.BufT = Type.BufT.DEBUG  # Debug buffer.
        test_in: List[Decimal] = DB.DB.inst().get_test_in()  # Test input.
        test_ref: List[Decimal] = DB.DB.inst().get_test_ref()  # Test ref output.

        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('test info'), buf)

        if isinstance(fun, Type.FunT):
            Printer.Printer.inst().buf(f'@target        : {fun.name.capitalize()}', buf, indent=2)
        else:
            Printer.Printer.inst().buf(f'@target        : {id}', buf, indent=2)

        Printer.Printer.inst().buf(f'@input size    : {len(test_in)}', buf, indent=2)
        Printer.Printer.inst().buf(f'@reference size: {len(test_ref)}', buf, indent=2)
        Printer.Printer.inst().buf_newline(buf)

        # Start test.
        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('start test'), buf)
        Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running test'), buf, False, 2)

        start: float = time.process_time()  # Start time stamp for elapsed time measure.

        if isinstance(fun, Type.FunT):
            if fun in [Type.FunT.SIN, Type.FunT.COS, Type.FunT.TAN, Type.FunT.ASIN, Type.FunT.ACOS, Type.FunT.ATAN]:
                test_out: List[Decimal] = Trigonometric.Tri.test(fun, test_in)  # Test output.
            elif fun in [Type.FunT.SINH, Type.FunT.COSH, Type.FunT.TANH, Type.FunT.ASINH, Type.FunT.ACOSH,
                         Type.FunT.ATANH]:
                test_out: List[Decimal] = HyperbolicTrigonometric.HyperTri.test(fun, test_in)  # Test output.
            elif fun in [Type.FunT.GAMMA, Type.FunT.LGAMMA, Type.FunT.ERF, Type.FunT.ERFC]:
                test_out: List[Decimal] = SpecialFunction.SpecialFunc.test(fun, test_in)  # Test output.
            else:
                test_out: List[Decimal] = Exponential.Exp.test(fun, test_in)  # Test output.
        else:
            test_out: List[Decimal] = list(map(lambda x: Decimal(fun(x)), test_in))  # Test output.

        Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)

        # Write test output.
        Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Writing test results'), buf, False, 2)

        try:
            out: TextIO = open('../Test/Test.out', 'w')  # File to write output.
        except OSError as os_err:
            Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)

            raise os_err

        for n in test_out:
            Printer.Printer.inst().buf(f'{n:.100e}', Type.BufT.INTERNAL, True)

        Printer.Printer.inst().print(Type.BufT.INTERNAL, out)

        try:
            out.close()
        except OSError as os_err:
            Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)

            raise os_err

        Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
        Printer.Printer.inst().buf_newline(buf)

        elapsed: float = time.process_time() - start  # Elapsed time.
        sz: int = os.path.getsize('../Test/Test.out')  # Test output file size.

        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('test finished'), buf)
        Printer.Printer.inst().buf(f'@out    :../Test/Test.out ({sz}bytes)', buf, indent=2)
        Printer.Printer.inst().buf(f'@elapsed: {elapsed * 1000:.2f}ms', buf, indent=2)
        Printer.Printer.inst().buf_newline(buf)

        # Report.
        test_err: List[Decimal] = list(map(lambda x, y: abs(x - y), test_ref, test_out))  # Test abs error.
        quant: List[Decimal] = statistics.quantiles(test_err)  # Quantiles.

        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('test report', 133), buf)
        Printer.Printer.inst().buf(f'@mean     : {statistics.fmean(test_err):.20e}', buf, indent=2)
        Printer.Printer.inst().buf(f'@sd       : {statistics.stdev(test_err):.20e}', buf, indent=2)
        Printer.Printer.inst().buf(f'@min      : {min(test_err):.20e}', buf, indent=2)
        Printer.Printer.inst().buf(f'@1st quant: {quant[0]:.20e}', buf, indent=2)
        Printer.Printer.inst().buf(f'@mode     : {quant[1]:.20e}', buf, indent=2)
        Printer.Printer.inst().buf(f'@3rd quant: {quant[2]:.20e}', buf, indent=2)
        Printer.Printer.inst().buf(f'@max      : {max(test_err):.20e}', buf, indent=2)
        Printer.Printer.inst().buf('@brief    :', buf, indent=2)
        Printer.Printer.inst().buf(Printer.Printer.inst().f_tb(['INPUT', 'REFERENCE', 'OUTPUT', 'ABSOLUTE ERROR'], 30),
                                   buf, indent=7)
        Printer.Printer.inst().buf(Printer.Printer.inst().f_hline(30, 4), buf, indent=7)

        if verb:
            for i in range(len(test_in)):
                Printer.Printer.inst().buf(
                    f'[{i:04d}] {test_in[i]:30.20e}  {test_ref[i]:30.20e}  {test_out[i]:30.20e}  {test_err[i]:30.20e}',
                    buf)
        else:
            for i in range(len(test_in)):
                if i > self.__MAX_PRINTOUT:
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_tb(['...', '...', '...', '...'], 30), buf,
                                               indent=7)
                    Printer.Printer.inst().buf(f'Followed by {len(test_out) - self.__MAX_PRINTOUT} more lines.', buf,
                                               indent=2)

                    break

                Printer.Printer.inst().buf(
                    f'[{i:04d}] {test_in[i]:30.20e}  {test_ref[i]:30.20e}  {test_out[i]:30.20e}  {test_err[i]:30.20e}',
                    buf)

        Printer.Printer.inst().buf_newline(buf)
