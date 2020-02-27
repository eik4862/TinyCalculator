import sys
from decimal import Decimal, getcontext
from typing import List, TextIO, Union, Callable

from Core import Parser, Type, AST, Interpreter, SystemManager, ErrorManager, DB, Error, WarningManager
from Util import Printer


def main(debug: bool = False, verb: bool = False, to: TextIO = sys.stdout) -> None:
    """
    Main routine for tiny calculator.

    It simply repeats following four steps.
        1. Take user input.
        2. Parser parse the input, generating AST.
        3. Interpreter interpret AST, computing the result.
        4. Print out the result.

    This method supports modes.
        1. Verbose debug mode.
           In this mode, it takes test inputs from DB and print out detailed results to stdout.
        2. Silent debug mode.
           In this mode, it takes test inputs from DB and compare the output with correct output.
           Unlike verbose debug mode, it does not print the result to stdout.
           Instead, it shows whether the test is passed of failed.
       3. Verbose user mode.
          In this mode, it takes input from the user through stdin and prints out detailed results to stdout.
       4. Silent user mode.
          In this mode, it takes input from the user through stdin and prints out simple result to stdout.
          This mode is default mode.

    :param debug: Flag for debug mode. (Default: False)
    :type debug: bool
    :param verb: Flag for verbose mode. (Default: False)
    :type debug: bool
    :param to: File where the result is to be printed out. (Default: sys.stdout)
    :type to: TextIO
    """
    if debug:
        # Attach signal handler.
        try:
            SystemManager.SysManager.inst().reg_sighandler(True)
        except Error.SysErr as sys_err:
            # Signal handler registration failure is critical and cannot be recovered.
            # Terminate the whole process.
            ErrorManager.ErrManager.inst().handle_err(sys_err)
            Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)
            Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
            sys.exit(1)
        else:
            Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)

        # Load DB.
        try:
            DB.DB.inst().load(True)
        except Error.DBErr as DB_err:
            # DB error is critical and cannot be recovered.
            # Terminate the whole process.
            ErrorManager.ErrManager.inst().handle_err(DB_err)
            Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)
            Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
            sys.exit(1)
        else:
            Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)

        if verb:
            for cnt in range(DB.DB.inst().get_sz('debug_in')):
                line: str = DB.DB.inst().get_debug_in(cnt)  # Input to be tested.

                Printer.Printer.inst().buf(f'TEST #{cnt}', Type.BufT.DEBUG)

                # Parse and interpret.
                try:
                    expr: AST.AST = Parser.Parser.inst().parse(line, True)  # Generated AST.

                    # Print out buffered output.
                    Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)

                    expr = Interpreter.Interp.inst().interp(expr, True)
                except Error.UtilErr as util_err:
                    if util_err.t == Type.UtilErrT.QUIT:
                        Printer.Printer.inst().buf(DB.DB.inst().get_greet_msg('BYE'))
                        Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
                        Printer.Printer.inst().print(to=to)
                        sys.exit(0)

                    ErrorManager.ErrManager.inst().handle_err(util_err)
                    expr = None
                except Error.Err as err:
                    ErrorManager.ErrManager.inst().handle_err(err)
                    expr = None

                # Process warnings.
                for warn in WarningManager.WarnManager.inst().q:
                    WarningManager.WarnManager.inst().handle_warn(warn)

                WarningManager.WarnManager.inst().clr()

                # Print out all buffered outputs in right order.
                if expr and expr.rt.tok_t != Type.TokT.VOID:
                    Printer.Printer.inst().buf(expr.infix())
                    Printer.Printer.inst().buf_newline()

                Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)
                Printer.Printer.inst().print(Type.BufT.STDWARN, to=to)
                Printer.Printer.inst().print(Type.BufT.INTERNAL, to=to)
                Printer.Printer.inst().print(Type.BufT.STDOUT, to=to)
                Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
        else:
            import time
            import re

            # Target functions to be tested.
            target: List[str] = [
                'Parser.__init()',
                'Parser.__lexer()',
                'Parser.__add_tok()',
                'Parser.__infix_to_postfix()',
                'AST.__infix_hlpr()',
                'AST.__postfix_hlpr()',
                'AST.__prefix_hlpr()',
                'Interpreter.__chk_t()',
                'Interpreter.__simplify()',
                'Operator.chk_t()',
                'Operator.simplify()',
                'Trigonometric.chk_t()',
                'Trigonometric.simplify()',
                'System.chk_t()'
            ]
            tot: int = DB.DB.inst().get_sz('debug_in')  # Total # of tests.

            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('debug test info'))
            Printer.Printer.inst().buf(f'@size  : {tot}', indent=2)
            Printer.Printer.inst().buf('@target:', indent=2)

            for i in range(len(target)):
                Printer.Printer.inst().buf(f'[{i}] {target[i]}', indent=4)

            Printer.Printer.inst().buf_newline()
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('start test'))
            Printer.Printer.inst().print(to=to)

            fail_idx: List[int] = []  # Idx of failed tests.
            start: float = time.process_time()  # Time stamp for elapsed time measuring.

            for cnt in range(DB.DB.inst().get_sz('debug_in')):
                line: str = DB.DB.inst().get_debug_in(cnt)  # Test input.
                out: str = ''  # Test output.

                Printer.Printer.inst().buf(Printer.Printer.inst().f_prog(f'[{cnt}] Running test case #{cnt}'),
                                           newline=False, indent=2)

                # Parse and interpret.
                try:
                    expr: AST.AST = Parser.Parser.inst().parse(line, True)  # Generated AST.

                    # Print out buffered output.
                    out += Printer.Printer.inst().sprint(Type.BufT.DEBUG)

                    expr = Interpreter.Interp.inst().interp(expr, True)
                except Error.UtilErr as util_err:
                    # TODO: Here, we need more delicacy
                    if util_err.t == Type.UtilErrT.QUIT:
                        Printer.Printer.inst().buf(DB.DB.inst().get_greet_msg('BYE'), Type.BufT.INTERNAL)
                        Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
                        Printer.Printer.inst().print(to=to)
                except Error.Err as err:
                    ErrorManager.ErrManager.inst().handle_err(err)
                    expr = None

                # Process warnings.
                for warn in WarningManager.WarnManager.inst().q:
                    WarningManager.WarnManager.inst().handle_warn(warn)

                WarningManager.WarnManager.inst().clr()

                # Print out all buffered outputs in right order.
                out += Printer.Printer.inst().sprint(Type.BufT.DEBUG)
                out += Printer.Printer.inst().sprint(Type.BufT.STDWARN)

                if expr and expr.rt.tok_t != Type.TokT.VOID:
                    out += f'{expr.infix()}\n\n'

                out += Printer.Printer.inst().sprint(Type.BufT.STDERR)
                out = re.sub(r'\d+ iteration', '1000 iteration', out)

                # Compare the result with answer.
                if out == DB.DB.inst().get_debug_out(f'TEST #{cnt}'):
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_col('pass', Type.Col.BLUE))
                else:
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED))
                    fail_idx.append(cnt)

                Printer.Printer.inst().print(to=to)
                cnt += 1

            elapsed: float = time.process_time() - start  # Elapsed time.
            fail: int = len(fail_idx)  # # of failed tests.
            succ: int = tot - fail  # # of passed tests.

            Printer.Printer.inst().buf_newline()
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('test finished'))
            Printer.Printer.inst().buf(f'@total  : {tot:3d}', indent=2)
            Printer.Printer.inst().buf(f'@pass   : {succ:3d} ({succ / tot * 100:.02f}%)', indent=2)
            Printer.Printer.inst().buf(f'@fail   : {fail:3d} ({fail / tot * 100:.02f}%)', indent=2)
            Printer.Printer.inst().buf(f'@elapsed: {elapsed * 1000:.2f}ms', indent=2)
            Printer.Printer.inst().print(to=to)

            if fail:
                Printer.Printer.inst().buf_newline()
                Printer.Printer.inst().buf(Printer.Printer.inst().f_title('fail report'))

                for idx in fail_idx:
                    Printer.Printer.inst().buf(f'@Test #{idx}: {DB.DB.inst().get_debug_in(idx)}', indent=2)

                Printer.Printer.inst().print(to=to)
    else:
        # Attach signal handler.
        try:
            SystemManager.SysManager.inst().reg_sighandler()
        except Error.SysErr as sys_err:
            # Signal handler registration failure is critical and cannot be recovered.
            # Terminate the whole process.
            ErrorManager.ErrManager.inst().handle_err(sys_err)
            Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
            sys.exit(1)

        # Load DB.
        try:
            DB.DB.inst().load(False)
        except Error.DBErr as DB_err:
            # DB error is critical and cannot be recovered.
            # Terminate the whole process.
            ErrorManager.ErrManager.inst().handle_err(DB_err)
            Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
            sys.exit(1)

        # Print out greeting message.
        Printer.Printer.inst().buf(DB.DB.inst().get_greet_msg('HELLO'))
        Printer.Printer.inst().print(to=to)

        if verb:
            while True:
                try:
                    with SystemManager.timeout(SystemManager.SysManager.inst().get_sys_var('Input_Timeout').v):
                        line: str = input('>> ')  # User input.
                except Error.SysErr as sys_err:
                    sys_err.err_no = 25
                    ErrorManager.ErrManager.inst().handle_err(sys_err)
                    Printer.Printer.inst().buf(DB.DB.inst().get_greet_msg('BYE'))
                    Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
                    Printer.Printer.inst().print(to=to)
                    sys.exit(0)

                # Parse and interpret.
                try:
                    expr: AST.AST = Parser.Parser.inst().parse(line, True)  # Generated AST.

                    # Print out buffered output.
                    Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)

                    expr = Interpreter.Interp.inst().interp(expr, True)
                except Error.UtilErr as util_err:
                    if util_err.t == Type.UtilErrT.QUIT:
                        Printer.Printer.inst().buf(DB.DB.inst().get_greet_msg('BYE'))
                        Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
                        Printer.Printer.inst().print(to=to)
                        sys.exit(0)

                    ErrorManager.ErrManager.inst().handle_err(util_err)
                    expr = None
                except Error.Err as err:
                    ErrorManager.ErrManager.inst().handle_err(err)
                    expr = None

                # Process warnings.
                for warn in WarningManager.WarnManager.inst().q:
                    WarningManager.WarnManager.inst().handle_warn(warn)

                WarningManager.WarnManager.inst().clr()

                # Print out all buffered outputs in right order.
                if expr and expr.rt.tok_t != Type.TokT.VOID:
                    Printer.Printer.inst().buf(expr.infix())
                    Printer.Printer.inst().buf_newline()

                Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)
                Printer.Printer.inst().print(Type.BufT.STDWARN, to=to)
                Printer.Printer.inst().print(Type.BufT.INTERNAL, to=to)
                Printer.Printer.inst().print(Type.BufT.STDOUT, to=to)
                Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
        else:
            while True:
                try:
                    with SystemManager.timeout(SystemManager.SysManager.inst().get_sys_var('Input_Timeout').v):
                        line: str = input('>> ')  # User input.
                except Error.SysErr as sys_err:
                    sys_err.err_no = 25
                    ErrorManager.ErrManager.inst().handle_err(sys_err)
                    Printer.Printer.inst().buf(DB.DB.inst().get_greet_msg('BYE'))
                    Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
                    Printer.Printer.inst().print(to=to)
                    sys.exit(0)

                # Parse and interpret.
                try:
                    expr: AST.AST = Parser.Parser.inst().parse(line)  # Generated AST.
                    expr = Interpreter.Interp.inst().interp(expr)
                except Error.UtilErr as util_err:
                    if util_err.t == Type.UtilErrT.QUIT:
                        Printer.Printer.inst().buf(DB.DB.inst().get_greet_msg('BYE'))
                        Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
                        Printer.Printer.inst().print(to=to)
                        sys.exit(0)

                    ErrorManager.ErrManager.inst().handle_err(util_err)
                    expr = None
                except Error.Err as err:
                    ErrorManager.ErrManager.inst().handle_err(err)
                    expr = None

                # Process warnings.
                for warn in WarningManager.WarnManager.inst().q:
                    WarningManager.WarnManager.inst().handle_warn(warn)

                WarningManager.WarnManager.inst().clr()

                # Print out all buffered outputs in right order.
                if expr and expr.rt.tok_t != Type.TokT.VOID:
                    Printer.Printer.inst().buf(expr.infix())
                    Printer.Printer.inst().buf_newline()

                Printer.Printer.inst().print(Type.BufT.STDWARN, to=to)
                Printer.Printer.inst().print(Type.BufT.INTERNAL, to=to)
                Printer.Printer.inst().print(Type.BufT.STDOUT, to=to)
                Printer.Printer.inst().print(Type.BufT.STDERR, to=to)


def test(target: Type.FunT = None, verb: bool = False, to: TextIO = sys.stdout) -> None:
    from Test import TestManager

    # Load DB.
    try:
        DB.DB.inst().load_test()
    except Error.DBErr as DB_err:
        # DB error is critical and cannot be recovered.
        # Terminate the whole process.
        ErrorManager.ErrManager.inst().handle_err(DB_err)
        Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)
        Printer.Printer.inst().print(Type.BufT.STDERR, to=to)
        sys.exit(1)
    else:
        Printer.Printer.inst().print(Type.BufT.DEBUG, to=to)

    # Set precision.
    getcontext().prec = 100

    # Run test.
    TestManager.TestManager.inst().test(target, verb)

    # Print out all buffered outputs in right order.
    Printer.Printer.inst().print(Type.BufT.DEBUG)


if __name__ == '__main__':
    # to = open('../Data/Debug.out', 'w')
    test()
    # main(True, False)
