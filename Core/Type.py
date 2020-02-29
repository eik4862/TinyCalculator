import math
import sys
from enum import Enum, auto
from typing import final, List, Union, Callable


@final
class TokT(Enum):
    """
    Token types.

    :cvar NUM: Numeric token.
    :cvar OP: Operator token.
    :cvar VAR: Variable token.
    :cvar FUN: Function token.
    :cvar DELIM: Delimiter token
    :cvar CMD: Command token.
    :cvar STR: String token.
    :cvar VOID: Void token.
    """
    NUM = auto()
    OP = auto()
    VAR = auto()
    FUN = auto()
    DELIM = auto()
    CMD = auto()
    STR = auto()
    VOID = auto()

    def __str__(self) -> str:
        return self.name


@final
class OpT(Enum):
    """
    Operator types.

    :cvar ADD: Addition. (Binary)
    :cvar SUB: Subtraction. (Binary)
    :cvar MUL: Multiplication. (Binary)
    :cvar DIV: Division. (Binary)
    :cvar REM: Remainder. (Binary)
    :cvar POW: Power. (Binary)
    :cvar FACT: Factorial. (Unary)
    :cvar LPAR: Left parenthesis.
    :cvar RPAR: Right parenthesis.
    :cvar PLUS: Sign preservation. (Unary)
    :cvar MINUS: Sign inversion. (Unary)
    """
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    REM = auto()
    POW = auto()
    FACT = auto()
    LPAR = auto()
    RPAR = auto()
    PLUS = auto()
    MINUS = auto()

    def __str__(self) -> str:
        return self.name


@final
class FunT(Enum):
    """
    Function types.

    For definition or details on each function consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Trigonometric_functions
        * http://mathworld.wolfram.com/Sine.html
        * http://mathworld.wolfram.com/Cosine.html
        * http://mathworld.wolfram.com/Tangent.html
        * https://en.wikipedia.org/wiki/Inverse_trigonometric_functions
        * http://mathworld.wolfram.com/InverseSine.html
        * http://mathworld.wolfram.com/InverseCosine.html
        * http://mathworld.wolfram.com/InverseTangent.html
        * https://en.wikipedia.org/wiki/Hyperbolic_functions
        * http://mathworld.wolfram.com/HyperbolicSine.html
        * http://mathworld.wolfram.com/HyperbolicCosine.html
        * http://mathworld.wolfram.com/HyperbolicTangent.html
        * https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions
        * http://mathworld.wolfram.com/InverseHyperbolicSine.html
        * http://mathworld.wolfram.com/InverseHyperbolicCosine.html
        * http://mathworld.wolfram.com/InverseHyperbolicTangent.html
        * https://en.wikipedia.org/wiki/Error_function
        * http://mathworld.wolfram.com/Erf.html
        * http://mathworld.wolfram.com/Erfc.html
        * https://en.wikipedia.org/wiki/Gamma_function
        * http://mathworld.wolfram.com/GammaFunction.html
        * http://mathworld.wolfram.com/LogGammaFunction.html

    :cvar SIN: Sine function.
    :cvar COS: Cosine function.
    :cvar TAN: Tangent function.
    :cvar ASIN: Arcsine function.
    :cvar ACOS: Arccosine function.
    :cvar ATAN: Arctangent function.
    :cvar SINH: Sine hyperbolic function.
    :cvar COSH: Cosine hyperbolic function.
    :cvar TANH: Tangent hyperbolic function.
    :cvar CSCH: Cosecant hyperbolic function.
    :cvar SECH: Secant hyperbolic function.
    :cvar COTH: Cotangent hyperbolic function.
    :cvar ASINH: Arcsine hyperbolic function.
    :cvar ACOSH: Arccosine hyperbolic function.
    :cvar ATANH: Arctangent hyperbolic function.
    :cvar ACSCH: Arccosecant hyperbolic function.
    :cvar ASECH: Arcsecant hyperbolic function.
    :cvar ACOTH: Arccotangent hyperbolic function.
    :cvar ERF: Error function.
    :cvar ERFC: Complementary error function.
    :cvar GAMMA: Gamma function.
    :cvar LGAMMA: Log gamma function.
    :cvar RECIGAMMA: Reicprocal gamma function.
    :cvar BESSELCLIFFORD: Bessel-Clifford function.
    :cvar BETA: Beta function.
    :cvar CENTRALBETA: Central beta function.
    :cvar SINC: Sinc function.
    :cvar TANC: Tanc function.
    :cvar SINHC: Sinhc function.
    :cvar COSHC: Coshc function.
    :cvar TANHC: Tanhc function.
    :cvar DIRICHLETKERNEL: Dirichlet kernel.
    :cvar FEJERKERNEL: Fejer kernel.
    :cvar TOPOLOGISTSIN: Topologist's sine function.
    :cvar LOG: Log function.
    :cvar EXP: Exponential function.
    :cvar SQRT: Square root function.
    """
    SIN = auto()
    COS = auto()
    TAN = auto()
    CSC = auto()
    SEC = auto()
    COT = auto()
    ASIN = auto()
    ACOS = auto()
    ATAN = auto()
    ACSC = auto()
    ASEC = auto()
    ACOT = auto()
    SINH = auto()
    COSH = auto()
    TANH = auto()
    CSCH = auto()
    SECH = auto()
    COTH = auto()
    ASINH = auto()
    ACOSH = auto()
    ATANH = auto()
    ACSCH = auto()
    ASECH = auto()
    ACOTH = auto()
    ERF = auto()
    ERFC = auto()
    GAMMA = auto()
    LGAMMA = auto()
    RECIGAMMA = auto()
    BESSELCLIFFORD = auto()
    BETA = auto()
    CENTRALBETA = auto()
    SINC = auto()
    TANC = auto()
    SINHC = auto()
    COSHC = auto()
    TANHC = auto()
    DIRICHLETKERNEL = auto()
    FEJERKERNEL = auto()
    TOPOLOGISTSIN = auto()
    LOG = auto()
    EXP = auto()
    SQRT = auto()

    def __str__(self) -> str:
        return self.name


@final
class ConstT(Enum):
    """
    Constant types.

    :cvar PI: Pi.
    :cvar E: Base of natural logarithm.
    :cvar E_GAMMA: Euler's gamma.
    :cvar PHI: Golden ratio.
    :cvar EPS: Machine epsilon for floating point number.
    :cvar MAX: Largest floating point number.
    :cvar MIN: Minimum floating point number.
    """
    PI: float = math.pi
    E: float = math.e
    E_GAMMA: float = 0.57721566490153286060651209008240243104215933593992359880576723488486772677766467
    PHI: float = 1.61803398874989484820458683436563811772030917980576286213544862270526046281890244
    EPS: float = sys.float_info.epsilon
    MAX: float = sys.float_info.max
    MIN: float = sys.float_info.min

    def __str__(self) -> str:
        return self.name


@final
class DelimT(Enum):
    """
    Delimiter types.

    :cvar START: Opening bracket.
    :cvar END: Closing bracket.
    :cvar CONT: Comma.
    """
    START = auto()
    END = auto()
    CONT = auto()

    def __str__(self) -> str:
        return self.name


@final
class CmdT(Enum):
    """
    Command types.

    :cvar QUIT: Quit command.
    :cvar HELP: Help command.
    :cvar GET_SYS_VAR: Get system variable command.
    :cvar SET_SYS_VAR: Set system variable command.
    :cvar SLEEP: Sleep command. (For debugging)
    """
    QUIT = auto()
    HELP = auto()
    GET_SYS_VAR = auto()
    SET_SYS_VAR = auto()
    SLEEP = auto()

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
class T(Enum):
    """
    Types for type checking and system variable.

    :cvar NUM: Numeric type.
    :cvar STR: String type.
    :cvar TER: Terminal type.
    """
    NUM = auto()
    STR = auto()
    TER = auto()

    def __str__(self) -> str:
        return self.name


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
class ParserErrT(Enum):
    """
    Parser error type.

    :cvar EMPTY_EXPR: Expression is empty.
    :cvar INVALID_TOK: Unknown token is encountered.
    :cvar INVALID_EXPR: Expression has syntax error.
    """
    EMPTY_EXPR = auto()
    INVALID_TOK = auto()
    INVALID_EXPR = auto()


@final
class InterpErrT(Enum):
    """
    Interpreter error type.

    :cvar T_MISMATCH: Type is not matched.
    :cvar SIGN_MISMATCH: Inferred signature is not found in candidates.
    """
    T_MISMATCH = auto()
    SIGN_MISMATCH = auto()


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
class Sign:
    """
    Signature class for type checking.

    :ivar __param_t: Parameter types.
    :ivar __ret_t: Return type.
    :ivar __handle: Handle of function or command.
    """

    def __init__(self, param_t: List[T], ret_t: T, handle: Union[FunT, CmdT]) -> None:
        self.__param_t: List[T] = param_t
        self.__ret_t: T = ret_t
        self.__handle: Union[FunT, CmdT] = handle

    def __del__(self) -> None:
        pass

    def __eq__(self, other) -> bool:
        return self.__param_t == other.param_t and self.__ret_t == other.ret_t and self.__handle == other.handle

    def __str__(self) -> str:
        return f'{self.__ret_t} {str(self.__handle).capitalize()}[' + ', '.join([str(t) for t in self.__param_t]) + ']'

    @property
    def param_t(self) -> List[T]:
        """
        Getter for parameter types.

        :return: Parameter types.
        :rtype: List[T]
        """
        return self.__param_t

    @property
    def ret_t(self) -> T:
        """
        Getter for return type.

        :return: Return type.
        :rtype: T
        """
        return self.__ret_t

    @property
    def handle(self) -> Union[FunT, CmdT]:
        """
        Getter for function or command handle.

        :return: Function or command handle.
        :rtype: Union[FunType, CmdType]
        """
        return self.__handle


@final
class HandleSrc:
    """
    Handle source class for handle registration.

    :ivar __enum: Enumeration class of handle.
    :ivar __brief: Brief description of handle.
    """

    def __init__(self, enum: Enum, brief: str) -> None:
        self.__enum: Enum = enum
        self.__brief: str = brief

    def __del__(self) -> None:
        pass

    @property
    def enum(self) -> Enum:
        """
        Getter for enumeration class of handle.

        :return: Enumeration class of handle.
        :rtype: Enum
        """
        return self.__enum

    @property
    def brief(self) -> str:
        """
        Getter for brief description of handle.

        :return: Brief description.
        :rtype: str
        """
        return self.__brief


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

    def __init__(self, v: Union[str, int], t: T, rd_only: bool = True) -> None:
        self.__v: Union[str, int] = v
        self.__t: T = t
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
    def t(self) -> T:
        """
        Getter for system variable type.

        :return: System variable type.
        :rtype: T
        """
        return self.__t

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
