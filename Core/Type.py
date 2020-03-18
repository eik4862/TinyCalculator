import sys
from enum import Enum, auto
from typing import final, List, Union, Callable


@final
class Const(Enum):
    """
    Constant types.

    Constant are approximated with 80 significant digits.
    For definition or details on each function consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Pi
        * https://en.wikipedia.org/wiki/E_(mathematical_constant)
        * https://en.wikipedia.org/wiki/Euler–Mascheroni_constant
        * https://en.wikipedia.org/wiki/Golden_ratio
        * https://en.wikipedia.org/wiki/Golden_angle
        * https://en.wikipedia.org/wiki/Catalan%27s_constant
        * https://en.wikipedia.org/wiki/Glaisher–Kinkelin_constant
        * https://en.wikipedia.org/wiki/Khinchin%27s_constant
        * https://docs.python.org/3/library/sys.html

    :cvar Pi: Pi.
    :cvar E: Base of natural logarithm.
    :cvar Degree: Conversion factor from degree to radian. (pi / 180)
    :cvar EulerGamma: Euler–Mascheroni constant.
    :cvar GoldenRatio: Golden ratio.
    :cvar GoldenAngle: Golden angle.
    :cvar Catalan: Catalan's constant.
    :cvar Glaisher: Glaisher's constant.
    :cvar Khinchin: Khinchin's constant.
    :cvar Eps: Machine epsilon for floating point number.
    :cvar FloatMax: Largest expressible floating point number.
    :cvar FloatMin: Smallest expressible floating point number.
    """

    Pi: float = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862090
    E: float = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535476
    Degree: float = 0.017453292519943295769236907684886127134428718885417254560971914401710091146034494
    EulerGamma: float = 0.57721566490153286060651209008240243104215933593992359880576723488486772677766467
    GoldenRatio: float = 1.6180339887498948482045868343656381177203091798057628621354486227052604628189024
    GoldenAngle: float = 2.3999632297286533222315555066336138531249990110581150429351127507313073382394388
    Catalan: float = 0.91596559417721901505460351493238411077414937428167213426649811962176301977625477
    Glaisher: float = 1.2824271291006226368753425688697917277676889273250011920637400217404063088588265
    Khinchin: float = 2.6854520010653064453097148354817956938203822939944629530511523455572188595371520
    Eps: float = sys.float_info.epsilon
    FloatMax: float = sys.float_info.max
    FloatMin: float = sys.float_info.min
    End: float = 0

    def __str__(self) -> str:
        return self.name


@final
class BufT(Enum):
    """
    Buffer type for printer module.

    :cvar STDOUT: Standard output.
    :cvar STDERR: Standard error.
    :cvar STDWARN: Warning buffer.
    :cvar DEBUG: Debug buffer.
    :cvar INTERNAL: Internal buffer.
    """
    STDOUT = auto()
    STDERR = auto()
    STDWARN = auto()
    DEBUG = auto()
    INTERNAL = auto()


@final
class Col(Enum):
    """
    Color type for printer module.

    :cvar RED: Bold red style.
    :cvar BLUE: Bold blue style.
    """
    RED = auto()
    BLUE = auto()


@final
class SysErrT(Enum):
    """
    System error types.

    :cvar REG_FAIL: Fail to register signal handler.
    :cvar UNREG_FAIL: Fail to unregister signal handler.
    :cvar TIMEOUT: Given operation exceeded limit computation time.
    """
    REG_FAIL = auto()
    UNREG_FAIL = auto()
    TIMEOUT = auto()


@final
class DBErrT(Enum):
    """
    DB error types.

    :cvar OPEN_ERR: Cannot open source file.
    :cvar CLOSE_ERR: Cannot close source file.
    """
    OPEN_ERR = auto()
    CLOSE_ERR = auto()


@final
class UtilErrT(Enum):
    """
    Utility command error type.

    :cvar NOT_FOUND: System variable is not found.
    :cvar T_MISMATCH: Type of system variable and given parameter does not match.
    :cvar RD_ONLY: System variable is read only.
    :cvar QUIT: Terminate system.
    :cvar INF_DETECT: Inf is detected as a given parameter.
    :cvar NAN_DETECT: Nan is detected as a given parameter.
    :cvar DOMAIN_OUT: Given parameter is not in domain.
    """
    NOT_FOUND = auto()
    T_MISMATCH = auto()
    RD_ONLY = auto()
    QUIT = auto()
    INF_DETECT = auto()
    NAN_DETECT = auto()
    DOMAIN_OUT = auto()


@final
class InterpWarnT(Enum):
    """
    Interpreter warning type.

    :cvar DOMAIN_OUT: Given parameter is not in domain.
    :cvar POLE_DETECT: Mathematical pole is detected.
    :cvar NAN_DETECT: Nan is detected as a given parameter.
    :cvar INF_DETECT: Inf is detected as a given parameter.
    :cvar BIG_INT: Too big integer which cannot be casted to float is detected as a given parameter.
    :cvar SMALL_INT: Too small integer which cannot be casted to float is detected as a given parameter.
    """
    DOMAIN_OUT = auto()
    POLE_DETECT = auto()
    NAN_DETECT = auto()
    INF_DETECT = auto()
    BIG_INT = auto()
    SMALL_INT = auto()


@final
class UtilWarnT(Enum):
    """
    Utility command warning type.

    :cvar DOMAIN_OUT: Given parameter is not in domain.
    :cvar TURN_OFF: Timeout functionality is turned off.
    :cvar INF_DETECT: Inf is detected as a given parameter.
    """
    DOMAIN_OUT = auto()
    TURN_OFF = auto()
    INF_DETECT = auto()


@final
class TestSzT(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()


@final
class FileSrc:
    """
    File source class for DB loading.

    :cvar __cnt: Counter to assign index for each source.

    :ivar __path: Path of source file.
    :ivar __brief: Brief description of source file.
    :ivar __tag: Flag for tagged DB source file.
    :ivar __idx: Index of source file in DB storage.
    """
    __cnt: int = 0

    def __init__(self, path: str, brief: str, tag: bool) -> None:
        self.__path: str = path
        self.__brief: str = brief
        self.__tag: bool = tag
        self.__idx: int = self.__cnt

        FileSrc.inc_cnt()

    def __del__(self) -> None:
        pass

    @classmethod
    def inc_cnt(cls) -> None:
        """
        Increase class counter by one.
        """
        cls.__cnt += 1

    @property
    def path(self) -> str:
        """
        Getter for path of source file.

        :return: Path of source file.
        :rtype: str
        """
        return self.__path

    @property
    def brief(self) -> str:
        """
        Getter for brief description of source file.

        :return: Brief description.
        :rtype: str
        """
        return self.__brief

    @property
    def tag(self) -> bool:
        """
        Getter for tag flag.

        :return: True if the source file is tagged. False otherwise.
        :rtype: bool
        """
        return self.__tag

    @property
    def idx(self) -> int:
        """
        Getter for index of the source file in DB storage.

        :return: Index in DB storage.
        :rtype: int
        """
        return self.__idx


@final
class SigHandler:
    """
    Signal handler class for system manager.

    :ivar __sig: Signal no to be handled.
    :ivar __handler: Handler for signal.
    :ivar __brief: Brief description of signal to be handled.
    """

    def __init__(self, sig: int, handler: Callable[..., None], brief: str) -> None:
        self.__sig: int = sig
        self.__handler: Callable[..., None] = handler
        self.__brief = brief

    def __del__(self) -> None:
        pass

    @property
    def sig(self) -> int:
        """
        Getter for signal no to be handled.

        :return: Signal no to be handled.
        :rtype: int
        """
        return self.__sig

    @property
    def handler(self) -> Callable[..., None]:
        """
        Getter for signal handler.

        :return: Signal handler.
        :rtype: Callable[..., None]
        """
        return self.__handler

    @property
    def brief(self) -> str:
        """
        Getter for brief description of signal to be handled.

        :return: Brief description.
        :rtype: str
        """
        return self.__brief


@final
class SysVar:
    """
    System variable class for system manager.

    :ivar __v: Value of system variable.
    :ivar __t: Type of system variable.
    :ivar __rd_only: Read only flag. (Default: True)
    """

    def __init__(self, v: Union[str, int], rd_only: bool = True) -> None:
        self.__v: Union[str, int] = v
        self.__rd_only: bool = rd_only

    def __del__(self) -> None:
        pass

    @property
    def v(self) -> Union[str, int]:
        """
        Getter for system variable value.

        :return: System variable value.
        :rtype: Union[str, int]
        """
        return self.__v

    @property
    def rd_only(self) -> bool:
        """
        Getter for read only flag.

        :return: Read only flag.
        :rtype: bool
        """
        return self.__rd_only

    @v.setter
    def v(self, v: Union[int, str]) -> None:
        """
        Setter for system variable value.

        :param v: Value of system variable to be set.
        :type v: Union[int, str]
        """
        self.__v = v
