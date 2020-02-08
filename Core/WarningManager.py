from typing import List, final

from Core import Type, DB, Warning
from Util import Printer


@final
class WarnManager:
    """
    Handle warning by generating proper warning messages in consistent form.

    This class is implemented as singleton.
    For the concept of singleton pattern, consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Singleton_pattern

    :cvar __inst: Singleton object.

    :ivar __q: Queue where generated warnings are queued.
    :ivar __cnt: Internal counter for buffering warning messages.
    """
    __inst = None

    def __init__(self) -> None:
        self.__q: List[Warning.Warn] = []
        self.__cnt: int = 0

    def __del__(self) -> None:
        pass

    def __handle_interp_warn(self, warn: Warning.InterpWarn) -> None:
        """
        Handler for warning from interpreter module.

        It handles following warnings according to following forms.
            * NAN_DETECT
                [Interpreter] WARNING: {warning message} (It contains the position of operand or parameter where NAN is
                                                          detected)
            * INF_DETECT
                [Interpreter] WARNING: {warning message} (It contains the position of operand or parameter where INF is
                                                          detected)
            * POLE_DETECT
                [Interpreter] WARNING: {warning message} (Detailed reason why pole is encountered)
            * DOMAIN_OUT
                [Interpreter] WARNING: {warning message} (Detailed reason why input parameter is not in domain)
        For detailed information of each warning, refer to the comments of ``InterpWarnT``.

        This method is private and called internally as a helper of ``WarnManager.handle_warn``.
        For detailed description for warning handling, refer to the comments of ``WarnManager.handle_warn``.

        :param warn: Interpreter warning to be handled.
        :type warn: Warning.InterpWarn
        """
        buf: Type.BufT = Type.BufT.STDWARN  # Target buffer.
        mark = Printer.Printer.inst().f_col('WARNING', Type.Col.BLUE)  # Warning mark.

        if warn.warn_no in [1, 2, 7, 8, 15, 16, 18, 19]:
            arg_pos: str = Printer.Printer.inst().f_ord(warn.arg_pos)  # Position of operand caused warning.
            msg: str = DB.DB.inst().get_warn_msg(warn.warn_no - 1).replace('$1', arg_pos)  # Warning message.
            msg = msg.replace('$2', warn.handle)
        else:
            msg: str = DB.DB.inst().get_warn_msg(warn.warn_no - 1)  # Warning message.

        if self.__cnt > 0:
            Printer.Printer.inst().pop(buf)

        Printer.Printer.inst().buf(f'[{self.__cnt}] [Interpreter] {mark}: {msg}', buf)
        Printer.Printer.inst().buf_newline(buf)
        self.__cnt += 1

    def __handle_util_warn(self, warn: Warning.UtilWarn) -> None:
        buf: Type.BufT = Type.BufT.STDWARN  # Target buffer.
        mark = Printer.Printer.inst().f_col('WARNING', Type.Col.BLUE)  # Warning mark.
        msg: str = DB.DB.inst().get_warn_msg(warn.warn_no - 1)  # Warning message.

        if self.__cnt > 0:
            Printer.Printer.inst().pop(buf)

        Printer.Printer.inst().buf(f'[{self.__cnt}] [Cmd.Utility] {mark}: {msg}', buf)
        Printer.Printer.inst().buf_newline(buf)
        self.__cnt += 1

    @classmethod
    def inst(cls):
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: WarnManager
        """
        if not cls.__inst:
            cls.__inst = WarnManager()

        return cls.__inst

    @property
    def q(self) -> List[Warning.Warn]:
        """
        Getter for warning queue.

        :return: Warning queue.
        :rtype: List[Warning.Warn]
        """
        return self.__q

    def push(self, warn: Warning.Warn) -> None:
        """
        Push warning into the internal queue.

        :param warn: Warning to be queued.
        :type warn: Warning.Warn
        """
        self.__q.append(warn)

    def is_warn(self) -> bool:
        """
        Check warning queue is empty.

        :return: True if warning queue is not empty. False otherwise.
        """
        return len(self.__q) != 0

    def clr(self) -> None:
        """
        Clear warning queue.
        """
        self.__q = []
        self.__cnt = 0

    def handle_warn(self, warn: Warning.Warn) -> None:
        """
        Handle error by generating proper error messages.

        Warning messages have following general form with slight difference depending on specific warning type and
        warning code.
            [{Warning source}] WARNING: {Brief description}

        :param warn: Warning to be handled.
        :type warn: Warning.Warn
        """
        if isinstance(warn, Warning.InterpWarn):
            self.__handle_interp_warn(warn)
        else:
            self.__handle_util_warn(warn)
