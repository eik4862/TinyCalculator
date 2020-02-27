import os
import statistics
import time
from decimal import Decimal
from typing import List, final, TextIO, Final, Tuple

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

    def test(self, fun: Type.FunT = None, verb: bool = False) -> None:
        """
        Run test, report with supplementary statistics and save the result.

        One should load test DB before calling this function.
        Otherwise, it will fail in unexpected way.
        The result will be stored as a text file as ``../Test/Test.out`` wrt. current working directory.

        :param fun: List of functions to be tested.
        :type fun: List[Type.FunT]
        :param verb: Flag for verbose mode. (Default: False)
        :type verb: bool
        """
        buf: Type.BufT = Type.BufT.DEBUG  # Debug buffer.

        if fun:
            test_in: List[Decimal] = DB.DB.inst().get_test_in()
            test_ref: List[Decimal] = DB.DB.inst().get_test_ref()
            argc: int = int(len(test_in) / len(test_ref))
            test_in: List[List[Decimal]] = [[test_in[argc * i + j] for j in range(argc)] for i in
                                            range(int(len(test_in) / argc))]

            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('test info'), buf)
            Printer.Printer.inst().buf(f'@target : {fun.name.capitalize()}', buf, indent=2)
            Printer.Printer.inst().buf(f'@size   : {len(test_ref)}', buf, indent=2)
            Printer.Printer.inst().buf(f'@argc   : {argc}', buf, indent=2)
            Printer.Printer.inst().buf_newline(buf)

            # Start test.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('start test'), buf)
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running test'), buf, False, 2)

            start: float = time.process_time()  # Start time stamp for elapsed time measure.

            if fun in [Type.FunT.SIN, Type.FunT.COS, Type.FunT.TAN, Type.FunT.CSC, Type.FunT.SEC, Type.FunT.COT,
                       Type.FunT.ASIN, Type.FunT.ACOS, Type.FunT.ATAN, Type.FunT.ACSC, Type.FunT.ASEC, Type.FunT.ACOT]:
                test_out: List[Decimal] = Trigonometric.Tri.test(fun, test_in)  # Test output.
            elif fun in [Type.FunT.SINH, Type.FunT.COSH, Type.FunT.TANH, Type.FunT.ASINH, Type.FunT.ACOSH,
                         Type.FunT.ATANH]:
                test_out: List[Decimal] = HyperbolicTrigonometric.HyperTri.test(fun, test_in)  # Test output.
            elif fun in [Type.FunT.GAMMA, Type.FunT.LGAMMA, Type.FunT.ERF, Type.FunT.ERFC, Type.FunT.BETA]:
                test_out: List[Decimal] = SpecialFunction.SpecialFun.test(fun, test_in)  # Test output.
            else:
                test_out: List[Decimal] = Exponential.Exp.test(fun, test_in)  # Test output.

            Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)

            # Write test output.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Writing test results'), buf, False, 2)

            if not os.path.isdir('../Test/Out'):
                os.mkdir('../Test/Out')

            try:
                out: TextIO = open('../Test/Out/Test.out', 'w')  # File to write output.
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
            sz: int = os.path.getsize('../Test/Out/Test.out')  # Test output file size.

            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('test finished'), buf)
            Printer.Printer.inst().buf(f'@out    :../Test/Out/Test.out ({sz}bytes)', buf, indent=2)
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
            Printer.Printer.inst().buf(
                Printer.Printer.inst().f_tb(['INPUT', 'REFERENCE', 'OUTPUT', 'ABSOLUTE ERROR'], 30), buf, indent=7)
            Printer.Printer.inst().buf(Printer.Printer.inst().f_hline(30, 4), buf, indent=7)

            if verb:
                for i in range(len(test_in)):
                    Printer.Printer.inst().buf(f'[{i:04d}] {test_in[i][0]:30.20e}  {test_ref[i]:30.20e}  '
                                               f'{test_out[i]:30.20e}  {test_err[i]:30.20e}', buf)

                    for j in range(argc - 1):
                        Printer.Printer.inst().buf(f'{test_in[i][j + 1]:30.20e}', buf, indent=7)
            else:
                for i in range(len(test_in)):
                    if i > self.__MAX_PRINTOUT:
                        Printer.Printer.inst().buf(Printer.Printer.inst().f_tb(['...', '...', '...', '...'], 30), buf,
                                                   indent=7)
                        Printer.Printer.inst().buf(f'Followed by {len(test_out) - self.__MAX_PRINTOUT} more lines.',
                                                   buf, indent=2)

                        break

                    Printer.Printer.inst().buf(
                        f'[{i:04d}] {test_in[i][0]:30.20e}  {test_ref[i]:30.20e}  {test_out[i]:30.20e}  '
                        f'{test_err[i]:30.20e}', buf)

                    for j in range(argc - 1):
                        Printer.Printer.inst().buf(f'{test_in[i][j + 1]:30.20e}', buf, indent=7)

            Printer.Printer.inst().buf_newline(buf)
        else:
            target: List[Tuple[Type.FunT, Type.TestSzT]] = DB.DB.inst().get_test_target()

            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('test info'), buf)
            Printer.Printer.inst().buf(f'@size   : {len(target)}', buf, indent=2)
            Printer.Printer.inst().buf(f'@target :', buf, indent=2)

            for i in range(len(target)):
                Printer.Printer.inst().buf(
                    f'[{i}] {target[i][0].name.capitalize()} ({target[i][1].name.lower()} input)', buf, indent=4)

            Printer.Printer.inst().buf_newline(buf)

            # Start test.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('start test'), buf)

            test_out: List[List[Decimal]] = []
            out_path: List[str] = []
            start: float = time.process_time()  # Start time stamp for elapsed time measure.

            for i in range(len(target)):
                test_in: List[Decimal] = DB.DB.inst().get_test_in(*target[i])
                test_ref: List[Decimal] = DB.DB.inst().get_test_ref(*target[i])
                argc: int = int(len(test_in) / len(test_ref))
                test_in: List[List[Decimal]] = [[test_in[argc * i + j] for j in range(argc)] for i in
                                                range(int(len(test_in) / argc))]

                Printer.Printer.inst().buf(Printer.Printer.inst().f_prog(f'[{i}] Running test #{i}'), buf, False, 2)

                if target[i][0] in [Type.FunT.SIN, Type.FunT.COS, Type.FunT.TAN, Type.FunT.CSC, Type.FunT.SEC,
                                    Type.FunT.COT, Type.FunT.ASIN, Type.FunT.ACOS, Type.FunT.ATAN, Type.FunT.ACSC,
                                    Type.FunT.ASEC, Type.FunT.ACOT]:
                    test_out.append(Trigonometric.Tri.test(target[i][0], test_in))
                elif target[i][0] in [Type.FunT.SINH, Type.FunT.COSH, Type.FunT.TANH, Type.FunT.ASINH, Type.FunT.ACOSH,
                                      Type.FunT.ATANH]:
                    test_out.append(HyperbolicTrigonometric.HyperTri.test(target[i][0], test_in))
                elif target[i][0] in [Type.FunT.GAMMA, Type.FunT.LGAMMA, Type.FunT.ERF, Type.FunT.ERFC, Type.FunT.BETA]:
                    test_out.append(SpecialFunction.SpecialFun.test(target[i][0], test_in))
                else:
                    test_out.append(Exponential.Exp.test(target[i][0], test_in))

                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)

            if not os.path.isdir('../Test/Out'):
                os.mkdir('../Test/Out')

            for i in range(len(target)):
                out_path.append(
                    f'../Test/Out/Test_{target[i][0].name.capitalize()}_{target[i][1].name.capitalize()}.out')

                try:
                    out: TextIO = open(out_path[-1], 'w')
                except OSError as os_err:
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)

                    raise os_err

                for n in test_out[i]:
                    Printer.Printer.inst().buf(f'{n:.100e}', Type.BufT.INTERNAL, True)

                Printer.Printer.inst().print(Type.BufT.INTERNAL, out)

                try:
                    out.close()
                except OSError as os_err:
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)

                    raise os_err

            Printer.Printer.inst().buf_newline(buf)

            elapsed: float = time.process_time() - start  # Elapsed time.
            sz: List[int] = [os.path.getsize(file) for file in out_path]  # Test output file size.

            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('test finished'), buf)
            Printer.Printer.inst().buf('@out    :', buf, indent=2)

            for i in range(len(out_path)):
                Printer.Printer.inst().buf(f'[{i}] {out_path[i]} ({sz[i]}bytes)', buf, indent=4)

            Printer.Printer.inst().buf(f'@elapsed: {elapsed * 1000:.2f}ms', buf, indent=2)
            Printer.Printer.inst().buf_newline(buf)
