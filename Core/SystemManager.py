import signal
import sys
from contextlib import contextmanager
from typing import Dict, final, List

from Core import Type, Error
from Util import Printer


def sigint_handler(sig, frame) -> None:
    """
    Signal handler for interrupt signal (ctrl + C).
    Print a message and terminate the whole process.

    :param sig: Signal number to be handled.
    :param frame: Frame where signal is sent.
    """
    print(f'Tiny calculator received SIGINT({sig}). Terminate.')
    sys.exit(0)


def sigtstp_handler(sig, frame) -> None:
    """
    Signal handler for stop signal (ctrl + Z).
    Print a message and terminate the whole process.

    :param sig: Signal number to be handled.
    :param frame: Frame where signal is sent.
    """
    print(f'Tiny calculator received SIGTSTP({sig}). Terminate.')
    sys.exit(0)


def sigalrm_handler(sig, frame) -> None:
    raise Error.SysErr(Type.SysErrT.TIMEOUT)


@contextmanager
def timeout(lim: int) -> None:
    try:
        signal.signal(signal.SIGALRM, sigalrm_handler)
    except OSError as os_err:
        raise Error.SysErr(Type.SysErrT.REG_FAIL, sig='SIGALRM', err_str=os_err.strerror)

    if lim > 0:
        signal.alarm(lim)

    try:
        yield
    except TimeoutError:
        pass
    finally:
        signal.alarm(0)

        try:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
        except OSError as os_err:
            raise Error.SysErr(Type.SysErrT.UNREG_FAIL, sig='SIGALRM', err_str=os_err.strerror)


@final
class SysManager:
    __inst = None

    def __init__(self) -> None:
        self.__sys_var: Dict[str, Type.SysVar] = {
            'Author': Type.SysVar('PSH (lkd1962@naver.com)', Type.T.STR),
            'Version': Type.SysVar('0.0.1', Type.T.STR),
            'Computation_Timeout': Type.SysVar(3, Type.T.NUM, False),
            'Input_Timeout': Type.SysVar(100, Type.T.NUM, False)
        }
        self.__sig_handler: List[Type.SigHandler] = [
            Type.SigHandler(signal.SIGINT, sigint_handler, 'SIGINT'),
            Type.SigHandler(signal.SIGTSTP, sigtstp_handler, 'SIGTSTP'),
        ]

    def __del__(self) -> None:
        pass

    @classmethod
    def inst(cls):
        if not cls.__inst:
            cls.__inst = SysManager()

        return cls.__inst

    def reg_sighandler(self, debug: bool = False, buf: Type.BufT = Type.BufT.DEBUG) -> None:
        if debug:
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('signal handler info'), buf)
            Printer.Printer.inst().buf('@target: ', buf, indent=2)

            for i in range(len(self.__sig_handler)):
                Printer.Printer.inst().buf(f'[{i}] {self.__sig_handler[i].brief}({self.__sig_handler[i].sig})', buf,
                                           indent=4)

            Printer.Printer.inst().buf_newline(buf)
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('registering signal handler'), buf)

            for handler in self.__sig_handler:
                Printer.Printer.inst().buf(
                    Printer.Printer.inst().f_prog(f'Registering {handler.brief} handler'), buf, False, 2)

                try:
                    signal.signal(handler.sig, handler.handler)
                except OSError as os_err:
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)

                    raise Error.SysErr(Type.SysErrT.REG_FAIL, sig=handler.brief, err_str=os_err.strerror)
                else:
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
                    Printer.Printer.inst().buf(f'@handler: {handler.handler}', buf, indent=4)
                    Printer.Printer.inst().buf_newline(buf)
        else:
            for handler in self.__sig_handler:
                try:
                    signal.signal(handler.sig, handler.handler)
                except OSError as os_err:
                    raise Error.SysErr(Type.SysErrT.REG_FAIL, sig=handler.brief, err_str=os_err.strerror)

    def get_sys_var(self, k: str) -> Type.SysVar:
        return self.__sys_var.get(k)

    def set_sys_var(self, k: str, v: int) -> None:
        self.__sys_var[k] = Type.SysVar(v, Type.T.NUM, False)
