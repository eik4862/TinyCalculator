from Core import Type, DB, SystemManager
from Error import *
from Util import Printer


class ErrManager:
    """
    Handle error by generating proper error messages in consistent form.

    This class is implemented as singleton.
    For the concept of singleton pattern, consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Singleton_pattern

    :cvar __inst: Singleton object.
    """
    __inst = None

    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass

    def __handle_sys_err(self, err: Error.SysErr) -> None:
        """
        Handler for error from system manager module.

        It handles following errors according to following forms.
            * REG_FAIL
                [System] ERROR: Cannot register signal handler to {signal name}.
                Error message from OS: {error message from OS}
            * UNREG_FAIL
                [System] ERROR: Cannot unregister signal handler to {signal name}.
                Error message from OS: {error message from OS}
            * TIMEOUT
                [System] ERROR: Timeout.
                {error message} (It contains the # of iterations until timeout.)
        For detailed information of each error, refer to the comments of ``SysErrT``.

        This method is private and called internally as a helper of ``ErrManager.handle_err``.
        For detailed description for error handling, refer to the comments of ``ErrManager.handle_err``.

        :param err: Interpreter error to be handled.
        :type err: Error.InterpErr
        """
        buf: Type.BufT = Type.BufT.STDERR  # Target buffer.
        mark: str = Printer.Printer.inst().f_col('ERROR', Type.Col.RED)  # Error mark.

        if err.err_no == 25:
            Printer.Printer.inst().buf_newline(buf)
            lim: int = SystemManager.SysManager.inst().get_sys_var('Input_Timeout').v  # Timeout limit.
            msg: str = DB.DB.inst().get_err_msg(24).replace('$1', str(lim))  # Error message.

        if err.err_t == Type.SysErrT.REG_FAIL:
            Printer.Printer.inst().buf(f'[System] {mark}: Cannot register signal handler to {err.sig}.', buf)
            Printer.Printer.inst().buf(f'Error message from OS: {err.err_str}.', buf)
            Printer.Printer.inst().buf('DB error is critical and cannot be recovered. Terminate.', buf)
            Printer.Printer.inst().buf_newline(buf)

            return
        elif err.err_t == Type.SysErrT.UNREG_FAIL:
            Printer.Printer.inst().buf(f'[System] {mark}: Cannot unregister signal handler to {err.sig}.', buf)
            Printer.Printer.inst().buf(f'Error message from OS: {err.err_str}.', buf)
            Printer.Printer.inst().buf('DB error is critical and cannot be recovered. Terminate.', buf)
            Printer.Printer.inst().buf_newline(buf)

            return
        else:
            Printer.Printer.inst().buf(f'[System] {mark}: Timeout.', buf)

        if err.err_no == 24:
            lim: int = SystemManager.SysManager.inst().get_sys_var('Computation_Timeout').v  # Timeout limit.
            msg: str = DB.DB.inst().get_err_msg(23).replace('$1', str(lim))  # Error message.
            msg = msg.replace('$2', str(err.iter))
        elif err.err_no != 25:
            msg: str = DB.DB.inst().get_err_msg(err.err_no - 1)  # Error message.

        Printer.Printer.inst().buf(msg, buf)
        Printer.Printer.inst().buf_newline(buf)

    def __handle_DB_err(self, err: Error.DBErr) -> None:
        """
        Handler for error from DB module.

        This method is private and called internally as a helper of ``ErrManager.handle_err``.
        For detailed description for error handling, refer to the comments of ``ErrManager.handle_err``.

        :param err: DB error to be handled.
        :type err: Error.DBErr
        """
        # Since DB error may occur before error messages are fully loaded, its error messages are hardcoded here.
        buf: Type.BufT = Type.BufT.STDERR  # Target buffer.
        mark: str = Printer.Printer.inst().f_col('ERROR', Type.Col.RED)  # Error mark.

        if err.err_t == Type.DBErrT.OPEN_ERR:
            Printer.Printer.inst().buf(f'[DB] {mark}: Cannot open DB source file at {err.path}.', buf)
            Printer.Printer.inst().buf(f'Error message from OS: {err.err_str}.', buf)
        else:
            Printer.Printer.inst().buf(f'[DB] {mark}: Cannot close DB source file at {err.path}.', buf)
            Printer.Printer.inst().buf(f'Error message from OS: {err.err_str}.', buf)

        Printer.Printer.inst().buf('DB error is critical and cannot be recovered. Terminate.', buf)
        Printer.Printer.inst().buf_newline(buf)

    def __handle_parser_err(self, err: ParserError) -> None:
        """
        Handler for error from parser module.

        This method is private and called internally as a helper of ``ErrManager.handle_err``.
        For detailed description for error handling, refer to the comments of ``ErrManager.handle_err``.

        :param err: Parser error to be handled.
        :type err: Error.ParserErr
        """
        buf: Type.BufT = Type.BufT.STDERR  # Target buffer.
        mark: str = Printer.Printer.inst().f_col('ERROR', Type.Col.RED)  # Error mark.
        err_t: type = type(err)  # Error type.

        if err_t == ParserError.EmptyExpr:
            Printer.Printer.inst().buf(f'[Parser] {mark}: Empty expression.', buf)
        elif err_t == ParserError.InvalidTok:
            Printer.Printer.inst().buf(err.line, buf)
            Printer.Printer.inst().buf('~' * err.pos + '^', buf)
            Printer.Printer.inst().buf(f'[Parser] {mark}: Invalid token.', buf)
        else:
            Printer.Printer.inst().buf(err.line, buf)
            Printer.Printer.inst().buf('~' * err.pos + '^', buf)
            Printer.Printer.inst().buf(f'[Parser] {mark}: Invalid expression.', buf)

        if err.errno == 2:
            msg: str = DB.DB.inst().get_err_msg(1).replace('$1', err.line[err.pos])  # Error message.
        elif err.errno == 11:
            msg: str = DB.DB.inst().get_err_msg(10)  # Error message.

            msg = msg.replace('$1', err.err_op[0].sym()).replace('$2', err.err_op[1].sym())
        else:
            msg: str = DB.DB.inst().get_err_msg(err.errno - 1)  # Error message.

        Printer.Printer.inst().buf(msg, buf)
        Printer.Printer.inst().buf_newline(buf)

    def __handle_interp_err(self, err: InterpreterError) -> None:
        """
        Handler for error from interpreter module.

        This method is private and called internally as a helper of ``ErrManager.handle_err``.
        For detailed description for error handling, refer to the comments of ``ErrManager.handle_err``.

        :param err: Interpreter error to be handled.
        :type err: Error.InterpErr
        """
        buf: Type.BufT = Type.BufT.STDERR  # Target buffer.
        mark: str = Printer.Printer.inst().f_col('ERROR', Type.Col.RED)  # Error mark.

        if type(err) == InterpreterError.TErr:
            Printer.Printer.inst().buf(err.line, buf)
            Printer.Printer.inst().buf('~' * err.pos + '^', buf)
            Printer.Printer.inst().buf(f'[Interpreter] {mark}: Type error.', buf)
        else:
            Printer.Printer.inst().buf(err.line, buf)
            Printer.Printer.inst().buf('~' * err.pos + '^', buf)
            Printer.Printer.inst().buf(f'[Interpreter] {mark}: Signature is not found.', buf)

        if err.errno == 22:
            msg: str = DB.DB.inst().get_err_msg(21).replace('$1', str(err.wrong_t))  # Error message.
            msg = msg.replace('$2', str(err.right_t))
        else:
            msg: str = DB.DB.inst().get_err_msg(22).replace('$1', f'\n  {err.err_sgn}\n')  # Error message.
            tmp: str = '\n'  # Temporary buffer for candidate signatures.

            for i in range(len(err.cand_sgn)):
                tmp += f'  [{i}] {err.cand_sgn[i]}\n'

            msg = msg.replace('$2', tmp).replace('$3', err.handle)

        Printer.Printer.inst().buf(msg, buf)
        Printer.Printer.inst().buf_newline(buf)

    def __handle_util_err(self, err: Error.UtilErr) -> None:
        buf: Type.BufT = Type.BufT.STDERR  # Target buffer.
        mark: str = Printer.Printer.inst().f_col('ERROR', Type.Col.RED)  # Error mark.

        if err.t == Type.UtilErrT.NOT_FOUND:
            Printer.Printer.inst().buf(f'[Cmd.Utility] {mark}: Not found.', buf)
        elif err.t == Type.UtilErrT.DOMAIN_OUT:
            Printer.Printer.inst().buf(f'[Cmd.Utility] {mark}: Not in domain.', buf)
        elif err.t == Type.UtilErrT.RD_ONLY:
            Printer.Printer.inst().buf(f'[Cmd.Utility] {mark}: Read only.', buf)
        elif err.t == Type.UtilErrT.T_MISMATCH:
            Printer.Printer.inst().buf(f'[Cmd.Utility] {mark}: Type error.', buf)
        elif err.t == Type.UtilErrT.INF_DETECT:
            Printer.Printer.inst().buf(f'[Cmd.Utility] {mark}: Inf detected.', buf)
        else:
            Printer.Printer.inst().buf(f'[Cmd.Utility] {mark}: Nan detected.', buf)

        if err.err_no in [26, 28]:
            msg: str = DB.DB.inst().get_err_msg(err.err_no - 1).replace('$1', err.id)
        elif err.err_no == 30:
            msg: str = DB.DB.inst().get_err_msg(29).replace('$1', err.wrong_t).replace('$2', err.id)
            msg = msg.replace('$3', err.correct_t)
        else:
            msg: str = DB.DB.inst().get_err_msg(err.err_no - 1)

        Printer.Printer.inst().buf(msg, buf)
        Printer.Printer.inst().buf_newline(buf)

    @classmethod
    def inst(cls):
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: ErrManager
        """
        if not cls.__inst:
            cls.__inst = ErrManager()

        return cls.__inst

    def handle_err(self, err: Error.Err) -> None:
        """
        Handle error by generating proper error messages.

        Error messages have following general form with slight difference depending on specific error type and error
        code.
            [{Error source}] ERROR: {Brief description}
            {Detailed description of error}

        :param err: Error to be handled.
        :type err: Error.Err
        """
        err_t: type = type(err).__base__

        if err_t == Error.ParserErr:
            self.__handle_parser_err(err)
        elif isinstance(err, Error.DBErr):
            self.__handle_DB_err(err)
        elif isinstance(err, Error.SysErr):
            self.__handle_sys_err(err)
        elif isinstance(err, Error.InterpErr):
            self.__handle_interp_err(err)
        else:
            self.__handle_util_err(err)
