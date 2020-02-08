from typing import final, List, Dict, Any

from Core import Type


class Err(Exception):
    """
    Base error class.

    Do not remove this.
    This is used to catch all user-defined errors at once.
    """

    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass


@final
class SysErr(Err):
    """
    System error class.

    :ivar __err_type: Error type.
    :ivar __extra_info: Extra information.
    """

    def __init__(self, err_t: Type.SysErrT, **kwargs: Any) -> None:
        super().__init__()
        self.__err_t = err_t
        self.__extra_info: Dict[str, Any] = kwargs

    def __del__(self) -> None:
        pass

    @property
    def err_t(self) -> Type.SysErrT:
        """
        Getter for system error type.

        :return: System error type.
        :rtype: Type.SysErrT
        """
        return self.__err_t

    @property
    def sig(self) -> str:
        """
        Getter for signal name at which registering or unregistering handler failed.

        :return: Signal name which caused error. None if this information is not given.
        :rtype: str
        """
        return self.__extra_info.get('sig')

    @property
    def err_str(self) -> str:
        """
        Getter for error string from OS error.

        :return: OS error string. None if this information is not given.
        :rtype: str
        """
        return self.__extra_info.get('err_str')

    @property
    def iter(self) -> int:
        """
        Getter for the # of iteration until timeout.

        :return: The # of iteration. None if this information is not given.
        :rtype: int
        """
        return self.__extra_info.get('iter')

    @property
    def err_no(self) -> int:
        """
        Getter for error code.

        :return: Error code. None if this information is not given.
        :rtype: int
        """
        return self.__extra_info.get('err_no')

    @iter.setter
    def iter(self, iter: int) -> None:
        """
        Setter for the # of iteration until timeout.

        :param iter: The # of iteration to set.
        :type iter: int
        """
        self.__extra_info['iter'] = iter

    @err_no.setter
    def err_no(self, err_no: int) -> None:
        """
        Setter for error code.

        :param err_no: Error code to set.
        :type err_no: int
        """
        self.__extra_info['err_no'] = err_no


@final
class DBErr(Err):
    """
    DB error class.

    :ivar __err_t: Error type.
    :ivar __path: Path of source file where error occurred.
    :ivar __err_str: Error string from OS error. (Default: None)
    """

    def __init__(self, err_t: Type.DBErrT, path: str, err_str: str = None) -> None:
        super().__init__()
        self.__err_t: Type.DBErrT = err_t
        self.__path: str = path
        self.__err_str: str = err_str

    def __del__(self) -> None:
        pass

    @property
    def err_t(self) -> Type.DBErrT:
        """
        Getter for DB error type.

        :return: DB error type.
        :rtype: Type.DBErrT
        """
        return self.__err_t

    @property
    def path(self) -> str:
        """
        Getter for path of source file where error occurred.

        :return: Source file path where error occurred.
        :rtype: str
        """
        return self.__path

    @property
    def err_str(self) -> str:
        """
        Getter for error string from OS error.

        :return: OS error string. None if this information is not given.
        :rtype: str
        """
        return self.__err_str


@final
class ParserErr(Err):
    """
    Parser error class.

    :ivar __err_t: Error type.
    :ivar __err_no: Error code.
    :ivar __line: Raw input which caused error. (Default: None)
    :ivar __pos: Position in raw input where error occurred. (Default: None)
    """

    def __init__(self, err_t: Type.ParserErrT, err_no: int, line: str = None, pos: int = None) -> None:
        super().__init__()
        self.__err_t: Type.ParserErrT = err_t
        self.__err_no: int = err_no
        self.__line: str = line
        self.__pos: int = pos

    def __del__(self) -> None:
        pass

    @property
    def err_t(self) -> Type.ParserErrT:
        """
        Getter for parser error type.

        :return: Parser error type.
        :rtype: Type.ParserErrT
        """
        return self.__err_t

    @property
    def line(self) -> str:
        """
        Getter for raw input which caused error.

        :return: Erroneous raw input. None if this information is not given.
        :rtype: str
        """
        return self.__line

    @property
    def pos(self) -> int:
        """
        Getter for position in raw input where error occurred.

        :return: Position where error occurred. None if this information is not given.
        :rtype: int
        """
        return self.__pos

    @property
    def err_no(self) -> int:
        """
        Getter for error code.

        :return: Error code.
        :rtype: int
        """
        return self.__err_no


@final
class InterpErr(Err):
    """
    Interpreter error class.

    :ivar __err_type: Error type.
    :ivar __err_code: Error code.
    :ivar __line: Raw input which caused error.
    :ivar __pos: Position in raw input where error occurred.
    :ivar __extra_info: Extra information.
    """

    def __init__(self, err_t: Type.InterpErrT, err_no: int, line: str, pos: int, **kwargs: Any) -> None:
        super().__init__()
        self.__err_t: Type.InterpErrT = err_t
        self.__err_no: int = err_no
        self.__line: str = line
        self.__pos: int = pos
        self.__extra_info: Dict[str, Any] = kwargs

    def __del__(self) -> None:
        pass

    @property
    def err_t(self) -> Type.InterpErrT:
        """
        Getter for interpreter error type.

        :return: Interpreter error type.
        :rtype: Type.InterpErrT
        """
        return self.__err_t

    @property
    def err_no(self) -> int:
        """
        Getter for error code.

        :return: Error code.
        :rtype: int
        """
        return self.__err_no

    @property
    def line(self) -> str:
        """
        Getter for raw input which caused error.

        :return: Erroneous raw input.
        :rtype: str
        """
        return self.__line

    @property
    def pos(self) -> int:
        """
        Getter for position in raw input where error occurred.

        :return: Position where error occurred.
        :rtype: int
        """
        return self.__pos

    @property
    def wrong_t(self) -> Type.T:
        """
        Getter for erroneous inferred type.

        :return: Erroneous inferred type.
        :rtype: Type.T
        """
        return self.__extra_info.get('wrong_t')

    @property
    def right_t(self) -> Type.T:
        """
        Getter for correct type.

        :return: Correct type.
        :rtype: Type.T
        """
        return self.__extra_info.get('right_t')

    @property
    def cand_sign(self) -> List[Type.Sign]:
        """
        Getter for candidate signatures.

        :return: Candidate signatures.
        :rtype: List[Type.Sign]
        """
        return self.__extra_info.get('cand_sign')

    @property
    def wrong_sign(self) -> Type.Sign:
        """
        Getter for erroneous inferred signature.

        :return: Erroneous inferred signature.
        :rtype: Type.Sign
        """
        return self.__extra_info.get('wrong_sign')


@final
class UtilErr(Err):
    """
    Utility command error class.

    :ivar __err_type: Error type.
    :ivar __err_code: Error code.
    :ivar __extra_info: Extra information.
    """
    def __init__(self, err_t: Type.UtilErrT, err_no: int = 0, **kwargs: Any) -> None:
        super().__init__()
        self.__err_t: Type.UtilErrT = err_t
        self.__err_no: int = err_no
        self.__extra_info: Dict[str, Any] = kwargs

    def __del__(self) -> None:
        pass

    @property
    def t(self) -> Type.UtilErrT:
        """
        Getter for utility command error type.

        :return: Utility command error type.
        :rtype: Type.UtilErrT
        """
        return self.__err_t

    @property
    def id(self) -> str:
        """
        Getter for erroneous system variable id.

        :return: Erroneous system variable id.
        :rtype: str
        """
        return self.__extra_info.get('id')

    @property
    def err_no(self) -> int:
        """
        Getter for error code.

        :return: Error code.
        :rtype: int
        """
        return self.__err_no

    @property
    def wrong_t(self):
        return self.__extra_info.get('wrong_t')

    @property
    def correct_t(self):
        return self.__extra_info.get('correct_t')