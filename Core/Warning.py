from typing import final, Dict, Any

from Core import Type


class Warn:
    """
    Base error class.

    Do not remove this.
    This is used to express all user-defined warnings at once.
    """

    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass


@final
class InterpWarn(Warn):
    """
    Interpreter warning class.

    :ivar __warn_t: Warning type.
    :ivar __warn_no: Warning code.
    :ivar __extra_info: Extra information.
    """

    def __init__(self, warn_t: Type.InterpWarnT, warn_no: int, **kwargs: Any) -> None:
        super().__init__()
        self.__warn_t: Type.InterpWarnT = warn_t
        self.__warn_no: int = warn_no
        self.__extra_info: Dict[str, Any] = kwargs

    def __del__(self) -> None:
        pass

    @property
    def warn_t(self) -> Type.InterpWarnT:
        """
        Getter for interpreter warning type.

        :return: Interpreter warning type.
        :rtype: Type.InterpWarnT
        """
        return self.__warn_t

    @property
    def warn_no(self) -> int:
        """
        Getter for warning code.

        :return: Warning code.
        :rtype: int
        """
        return self.__warn_no

    @property
    def handle(self) -> str:
        """
        Getter for erroneous function handle.

        :return: Erroneous function handle.
        :rtype: str
        """
        return self.__extra_info.get('handle')

    @property
    def arg_pos(self) -> int:
        """
        Getter for the position of erroneous operand.

        :return: Erroneous operand position.
        :rtype: int
        """
        return self.__extra_info.get('arg_pos')


@final
class UtilWarn(Warn):
    """
    Utility command warning type.

    :ivar __warn_t: Warning type.
    :ivar __warn_no: Warning code.
    """
    def __init__(self, warn_t: Type.UtilWarnT, warn_no: int) -> None:
        super().__init__()
        self.__warn_t: Type.UtilWarnT = warn_t
        self.__warn_no: int = warn_no

    def __del__(self) -> None:
        pass

    @property
    def warn_t(self) -> Type.UtilWarnT:
        """
        Getter for utility command warning type.

        :return: Utility command warning type.
        :rtype: Type.UtilWarnT
        """
        return self.__warn_t

    @property
    def warn_no(self) -> int:
        """
        Getter for warning code.

        :return: Warning code.
        :rtype: int
        """
        return self.__warn_no
