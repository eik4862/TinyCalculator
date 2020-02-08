from Core import Type, DB, Error, SystemManager
from Util import Printer
from Util.Macro import is_white, is_delim, is_op


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

        It handles following errors according to following forms.
            * OPEN_ERR
                [DB] ERROR: Cannot open DB source file at {source path}.
                Error message from OS: {error message from OS}
                DB error is critical and cannot be recovered. Terminate.
            * CLOSE_ERR
                [DB] ERROR: Cannot close DB source file at {source path}.
                Error message from OS: {error message from OS}
                DB error is critical and cannot be recovered. Terminate.
        For detailed information of each error, refer to the comments of ``DBErrT``.

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

    def __handle_parser_err(self, err: Error.ParserErr) -> None:
        """
        Handler for error from parser module.

        It handles following errors according to following forms.
            * EMPTY_EXPR
                [Parser] ERROR: Empty expression.
                {error message}
            * INVALID_TOK
                {raw input}
                ~~...~^ (position of invalid token)
                [Parser] ERROR: Invalid token.
                {error message} (If contains invalid character)
            * INVALID_EXPR
                {raw input}
                ~~...~^ (position of invalid expression)
                [Parser] ERROR: Invalid expression.
                {error message} (It contains detailed explanation of invalid part.)
        For detailed information of each error, refer to the comments of ``ParserErrT``.

        This method is private and called internally as a helper of ``ErrManager.handle_err``.
        For detailed description for error handling, refer to the comments of ``ErrManager.handle_err``.

        :param err: Parser error to be handled.
        :type err: Error.ParserErr
        """
        buf: Type.BufT = Type.BufT.STDERR  # Target buffer.
        mark: str = Printer.Printer.inst().f_col('ERROR', Type.Col.RED)  # Error mark.

        if err.err_t == Type.ParserErrT.EMPTY_EXPR:
            Printer.Printer.inst().buf(f'[Parser] {mark}: Empty expression.', buf)
        elif err.err_t == Type.ParserErrT.INVALID_TOK:
            Printer.Printer.inst().buf(err.line, buf)
            Printer.Printer.inst().buf('~' * err.pos + '^', buf)
            Printer.Printer.inst().buf(f'[Parser] {mark}: Invalid token.', buf)
        else:
            Printer.Printer.inst().buf(err.line, buf)
            Printer.Printer.inst().buf('~' * err.pos + '^', buf)
            Printer.Printer.inst().buf(f'[Parser] {mark}: Invalid expression.', buf)

        if err.err_no == 2:
            msg: str = DB.DB.inst().get_err_msg(1).replace('$1', err.line[err.pos])  # Error message.
        elif err.err_no == 11:
            prev_pos: int = err.pos - 1  # Previous position of erroneous token.

            while prev_pos > 0:
                if not is_white(err.line[prev_pos]):
                    break

                prev_pos -= 1

            assert is_op(err.line[prev_pos])

            if err.line[prev_pos] == '*' and prev_pos > 0 and err.line[prev_pos - 1] == '*':
                msg: str = DB.DB.inst().get_err_msg(10).replace('$1', '**')  # Error message.
            else:
                msg: str = DB.DB.inst().get_err_msg(10).replace('$1', err.line[prev_pos])  # Error message.

            if err.pos + 1 < len(err.line) and err.line[err.pos] == err.line[err.pos + 1] == '*':
                msg = msg.replace('$2', '**')
            else:
                msg = msg.replace('$2', err.line[err.pos])
        elif err.err_no == 12:
            prev_pos: int = err.pos - 1  # Previous position of erroneous token.

            while prev_pos > 0:
                if not is_white(err.line[prev_pos]):
                    break

                prev_pos -= 1

            assert is_delim(err.line[prev_pos])

            msg: str = DB.DB.inst().get_err_msg(11).replace('$1', err.line[prev_pos])  # Error message.

            if err.line[err.pos] == '*' and err.pos + 1 < len(err.line) and err.line[err.pos + 1] == '*':
                msg = msg.replace('$2', '**')
            else:
                msg = msg.replace('$2', err.line[err.pos])
        elif err.err_no == 14:
            prev_pos: int = err.pos - 1  # Previous position of erroneous token.

            while prev_pos > 0:
                if not is_white(err.line[prev_pos]):
                    break

                prev_pos -= 1

            assert is_op(err.line[prev_pos])

            if err.line[prev_pos] == '*' and prev_pos > 0 and err.line[prev_pos - 1] == '*':
                msg: str = DB.DB.inst().get_err_msg(13).replace('$1', '**')  # Error message.
            else:
                msg: str = DB.DB.inst().get_err_msg(13).replace('$1', err.line[prev_pos])  # Error message.

            msg = msg.replace('$2', err.line[err.pos])
        elif err.err_no == 15:
            prev_pos: int = err.pos - 1  # Previous position of erroneous token.

            while prev_pos > 0:
                if not is_white(err.line[prev_pos]):
                    break

                prev_pos -= 1

            assert is_delim(err.line[prev_pos])

            msg: str = DB.DB.inst().get_err_msg(14).replace('$1', err.line[prev_pos])  # Error message.
            msg = msg.replace('$2', err.line[err.pos])
        else:
            msg: str = DB.DB.inst().get_err_msg(err.err_no - 1)  # Error message.

        Printer.Printer.inst().buf(msg, buf)
        Printer.Printer.inst().buf_newline(buf)

    def __handle_interp_err(self, err: Error.InterpErr) -> None:
        """
        Handler for error from interpreter module.

        It handles following errors according to following forms.
            * TYPE_MISMATCH
                [Interpreter] ERROR: Type error.
                {error message} (It contains inferred wrong type and expected correct type.)
            * CLOSE_ERR
                [Interpreter] ERROR: Signature is not found.
                {error message} (It contains inferred signature and list of candidate signatures.)
        For detailed information of each error, refer to the comments of ``InterpErrT``.

        This method is private and called internally as a helper of ``ErrManager.handle_err``.
        For detailed description for error handling, refer to the comments of ``ErrManager.handle_err``.

        :param err: Interpreter error to be handled.
        :type err: Error.InterpErr
        """
        buf: Type.BufT = Type.BufT.STDERR  # Target buffer.
        mark: str = Printer.Printer.inst().f_col('ERROR', Type.Col.RED)  # Error mark.

        if err.err_t == Type.InterpErrT.T_MISMATCH:
            Printer.Printer.inst().buf(err.line, buf)
            Printer.Printer.inst().buf('~' * err.pos + '^', buf)
            Printer.Printer.inst().buf(f'[Interpreter] {mark}: Type error.', buf)
        else:
            Printer.Printer.inst().buf(err.line, buf)
            Printer.Printer.inst().buf('~' * err.pos + '^', buf)
            Printer.Printer.inst().buf(f'[Interpreter] {mark}: Signature is not found.', buf)

        if err.err_no == 22:
            msg: str = DB.DB.inst().get_err_msg(21).replace('$1', str(err.wrong_t))  # Error message.
            msg = msg.replace('$2', str(err.right_t))
        else:
            msg: str = DB.DB.inst().get_err_msg(22).replace('$1', f'\n  {err.wrong_sign}\n')  # Error message.
            tmp: str = '\n'  # Temporary buffer for candidate signatures.

            for i in range(len(err.cand_sign)):
                tmp += f'  [{i}] {err.cand_sign[i]}\n'

            msg = msg.replace('$2', tmp).replace('$3', str(err.wrong_sign.handle).capitalize())

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
        if isinstance(err, Error.ParserErr):
            self.__handle_parser_err(err)
        elif isinstance(err, Error.DBErr):
            self.__handle_DB_err(err)
        elif isinstance(err, Error.SysErr):
            self.__handle_sys_err(err)
        elif isinstance(err, Error.InterpErr):
            self.__handle_interp_err(err)
        else:
            self.__handle_util_err(err)
