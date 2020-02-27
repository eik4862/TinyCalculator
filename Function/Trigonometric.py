import math
from decimal import Decimal
from typing import Tuple, List, Dict, Optional, final, Final

from Core import Type, Token, Warning
from Util.Macro import is_bigint, is_smallint


@final
class Tri:
    """
    Trigonometric function toolbox.

    :cvar __sign: Signatures of trigonometric functions.
    """
    __sign: Final[Dict[Type.FunT, List[Type.Sign]]] = {
        Type.FunT.SIN: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.SIN)],
        Type.FunT.COS: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.COS)],
        Type.FunT.TAN: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.TAN)],
        Type.FunT.CSC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.CSC)],
        Type.FunT.SEC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.SEC)],
        Type.FunT.COT: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.COT)],
        Type.FunT.ASIN: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ASIN)],
        Type.FunT.ACOS: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ACOS)],
        Type.FunT.ATAN: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ATAN)],
        Type.FunT.ACSC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ACSC)],
        Type.FunT.ASEC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ASEC)],
        Type.FunT.ACOT: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ACOT)]
    }

    def __init__(self) -> None:
        raise NotImplementedError

    def __del__(self) -> None:
        raise NotImplementedError

    @classmethod
    def __sin(cls, x: float) -> float:
        """
        Sine function.

        Sine function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite, the result is ``math.sin(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where sine function is to be computed.
        :type x: float

        :return: Computed value of sine function.
        :rtype: float
        """
        return math.nan if math.isinf(x) else math.sin(x)

    @classmethod
    def __cos(cls, x: float) -> float:
        """
        Cosine function.

        Cosine function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite, the result is ``math.cos(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where cosine function is to be computed.
        :type x: float

        :return: Computed value of cosine function.
        :rtype: float
        """
        return math.nan if math.isinf(x) else math.cos(x)

    @classmethod
    def __tan(cls, x: float) -> float:
        """
        Tangent function.

        Tangent function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite which is (integer multiple of pi)+pi/2, the result is nan.
            3. If x is finite which is not (integer multiple of pi)+pi/2, the result is ``math.tan(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where tangent function is to be computed.
        :type x: float

        :return: Computed value of tangent function.
        :rtype: float
        """
        return math.nan if math.isinf(x) or (x - math.pi / 2) % math.pi == 0 else math.tan(x)

    @classmethod
    def __csc(cls, x: float) -> float:
        """
        Cosecant function.

        Cosecant function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite which is integer multiple of pi, the result is nan.
            3. If x is finite which is not integer multiple of pi, the result is ``1 / math.sin(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where cosecant function is to be computed.
        :type x: float

        :return: Computed value of cosecant function.
        :rtype: float
        """
        return math.nan if math.isinf(x) or x % math.pi == 0 else 1 / math.sin(x)

    @classmethod
    def __sec(cls, x: float) -> float:
        """
        Secant function.

        Secant function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite which is (integer multiple of pi)+pi/2, the result is nan.
            3. If x is finite which is not (integer multiple of pi)+pi/2, the result is ``1 / math.cos(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where secant function is to be computed.
        :type x: float

        :return: Computed value of secant function.
        :rtype: float
        """
        return math.nan if math.isinf(x) or (x - math.pi / 2) % math.pi == 0 else 1 / math.cos(x)

    @classmethod
    def __cot(cls, x: float) -> float:
        """
        Cotangent function.

        Secant function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite which is integer multiple of pi, the result is nan.
            3. If x is finite which is not integer multiple of pi, the result is ``1 / math.tan(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where cotangent function is to be computed.
        :type x: float

        :return: Computed value of cotangent function.
        :rtype: float
        """
        return math.nan if math.isinf(x) or x % math.pi == 0 else 1 / math.tan(x)

    @classmethod
    def __asin(cls, x: float) -> float:
        """
        Arcsine function.

        Arcsine function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite which is not in [-1, 1], the result is nan.
            3. If x is finite which is in [-1. 1], the result is ``math.asin(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where arcsine function is to be computed.
        :type x: float

        :return: Computed value of arcsine function.
        :rtype: float
        """
        return math.nan if math.isinf(x) or not (-1 <= x <= 1) else math.asin(x)

    @classmethod
    def __acos(cls, x: float) -> float:
        """
        Arccosine function.

        Arccosine function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite which is not in [-1, 1], the result is nan.
            3. If x is finite which is in [-1. 1], the result is ``math.acos(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where arccosine function is to be computed.
        :type x: float

        :return: Computed value of arccosine function.
        :rtype: float
        """
        return math.nan if math.isinf(x) or not (-1 <= x <= 1) else math.acos(x)

    @classmethod
    def __atan(cls, x: float) -> float:
        """
        Arctangent function.

        Arctangent function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is +-pi/2, resp.
            3. If x is finite, the result is ``math.atan(x)``.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        :param x: Point where arctangent function is to be computed.
        :type x: float

        :return: Computed value of arctangent function.
        :rtype: float
        """
        return math.atan(x)

    @classmethod
    def __acsc(cls, x: float) -> float:
        """
        Arccosecant function.

        Arccosecant function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is 0.
            3. If x is in (-1, 1), the result is nan.
            4. If x is finite which is not in (-1, 1), the result is ``math.asin(1 / x)``.
        Here, the rule 4 is based on identity ``asec(x) = acos(1 / x)``.
        For detail and more identities, consult the reference below.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        **Reference**
            * https://en.wikipedia.org/wiki/Inverse_trigonometric_functions

        :param x: Point where arccosecant function is to be computed.
        :type x: float

        :return: Computed value of arccosecant function.
        :rtype: float
        """
        return math.nan if -1 < x < 1 else math.asin(1 / x)

    @classmethod
    def __asec(cls, x: float) -> float:
        """
        Arcsecant function.

        Arcsecant function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is pi/2.
            3. If x is in (-1, 1), the result is nan.
            4. If x is finite which is not in (-1, 1), the result is ``math.acos(1 / x)``.
        Here, the rule 4 is based on identity ``asec(x) = acos(1 / x)``.
        For detail and more identities, consult the reference below.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        **Reference**
            * https://en.wikipedia.org/wiki/Inverse_trigonometric_functions

        :param x: Point where arcsecant function is to be computed.
        :type x: float

        :return: Computed value of arcsecant function.
        :rtype: float
        """
        return math.nan if -1 < x < 1 else math.acos(1 / x)

    @classmethod
    def __acot(cls, x: float) -> float:
        """
        Arccotangent function.

        Arccotangent function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is 0.
            3. If x is finite negative, the result is ``-(math.pi / 2 + math.atan(x))``.
            4. If x is nonnegative, the result is ``math.pi / 2 - math.atan(x)``.
        Here, the rule 3 and 4 are based on identity ``acot(x) = -pi / 2 - atan(x)`` for negative x and
        ``acot(x) = pi / 2 - atan(x)`` for nonnegative x.
        For detail and more identities, consult the reference below.

        This method is private and called internally as a helper of ``Tri.simplify``.
        For detailed description for simplification, refer to the comments of ``Tri.simplify``.

        **Reference**
            * https://en.wikipedia.org/wiki/Inverse_trigonometric_functions

        :param x: Point where arccotangent function is to be computed.
        :type x: float

        :return: Computed value of arccotangent function.
        :rtype: float
        """
        return -(math.pi / 2 + math.atan(x)) if x < 0 else math.pi / 2 - math.atan(x)

    @classmethod
    def chk_t(cls, rt: Token.FunTok) -> Optional[List[Type.Sign]]:
        """
        Type checker for trigonometric functions.
        It checks type of input function token and assigns return type as type information of the token.

        :param rt: Token to be type checked.
        :type rt: Token.FunTok

        :return: None if type check is successful. Candidate signatures if not.
        :rtype: Optional[List[Type.Signature]]
        """
        cand: List[Type.Sign] = cls.__sign.get(rt.v)  # Candidate signatures
        infer: Type.Sign = Type.Sign([tok.t for tok in rt.chd], Type.T.NUM, rt.v)  # Inferred signature

        # Inferred signature must be one of candidates and return type is NUM type.
        if infer in cand:
            rt.t = Type.T.NUM

            return None
        else:
            return cand

    # TODO: No function coalescing. They are not safe.
    @classmethod
    def simplify(cls, rt: Token.FunTok) -> Tuple[Token.Tok, List[Warning.InterpWarn]]:
        """
        Simplifier for trigonometric functions.

        It does following simplifications.
            1. Constant folding.
            2. Dead expression stripping.
            3. Sign propagation.
        For details and detailed explanation of these optimization tricks, consult following references and comments of
        ``Operator.simplify`` and references therein.

        :param rt: Root of AST to be simplified.
        :type rt: Token.FunTok

        :return: Root of simplified AST and list of generated warnings.
        :rtype: Tuple[Token.Tok, List[Warning.InterpWarn]]

        :raise NAN_DETECT: If nan is detected as a given parameter.
        :raise IFN_DETECT: If inf is detected as a given parameter.
        :raise DOMAIN_OUT: If given parameter is not in domain.
        :raise POLE_DETECT: If mathematical pole is detected.
        :raise BIG_INT: If given parameter exceeds floating point max.
        :raise SMALL_INT: If given parameter exceeds floating point min.
        """
        warn: List[Warning.InterpWarn] = []  # List of generated warnings.

        if rt.v == Type.FunT.SIN:
            # Check for warnings.
            # Sine function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Sin'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Sin'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Sin'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Sin'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__sin``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__sin(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Sin[-x] = -Sin[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.COS:
            # Check for warnings.
            # Cosine function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Cos'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Cos'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Cos'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Cos'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__cos``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__cos(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Cos[-x] = Cos[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.TAN:
            # Check for warnings.
            # Tangent function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is integer multiple of pi + pi/2. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Tan'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Tan'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Tan'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Tan'))
                elif (rt.chd[0].v - math.pi / 2) % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 5))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__tan``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__tan(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Tan[-x] = -Tan[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.CSC:
            # Check for warnings.
            # Cosecant function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is integer multiple of pi. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Csc'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Csc'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Csc'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Csc'))
                elif rt.chd[0].v % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 26))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__csc``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__csc(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Csc[-x] = -Csc[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.SEC:
            # Check for warnings.
            # Secant function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is integer multiple of pi + pi/2. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Sec'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Sec'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Sec'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Sec'))
                elif (rt.chd[0].v - math.pi / 2) % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 27))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__sec``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__sec(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Sec[-x] = Sec[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.COT:
            # Check for warnings.
            # Cotangent function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is integer multiple of pi. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Cot'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Cot'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Cot'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Cot'))
                elif rt.chd[0].v % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 28))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__cot``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__cot(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Cot[-x] = -Cot[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ASIN:
            # Check for warnings.
            # Arcsine function with parameter x generates warning for followings cases.
            #   1. x is nan. (NAN_DETECT)
            #   2. x is +-inf. (INF_DETECT)
            #   3. x is not in [-1, 1]. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v) or is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 3))
                    rt.chd[0].v = 2
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Asin'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Asin'))
                elif not (-1 <= rt.chd[0].v <= 1):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 3))

            # Constant folding.
            # Arcsine function with parameter x has following rules.
            # For detailed computation rule, refer to the comment in ``Tri.__asin``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__asin(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Asin[-x] = -Asin[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ACOS:
            # Check for warnings.
            # Arccosine function with parameter x generates warning for followings cases.
            #   1. x is nan. (NAN_DETECT)
            #   2. x is +-inf. (INF_DETECT)
            #   3. x is not in [-1, 1]. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v) or is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 4))
                    rt.chd[0].v = 2
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Acos'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Acos'))
                elif not (-1 <= rt.chd[0].v <= 1):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 4))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__acos``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__acos(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.ATAN:
            # Check for warnings.
            # Arctangent function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Atan'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Atan'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Atan'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Atan'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__atan``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__atan(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Atan[-x] = -Atan[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ACSC:
            # Check for warnings.
            # Arccosecant function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is in (-1, 1). (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Acsc'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Acsc'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Acsc'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Acsc'))
                elif -1 < rt.chd[0].v < 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 29))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__acsc``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__acsc(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Acsc[-x] = -Acsc[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ASEC:
            # Check for warnings.
            # Arcsecant function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is in (-1, 1). (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Asec'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Asec'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Asec'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Asec'))
                elif -1 < rt.chd[0].v < 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 30))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__asec``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__asec(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        else:
            # Check for warnings.
            # Arccotangent function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Acot'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Acot'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Acot'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Acot'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``Tri.__acot``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__acot(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn

    @classmethod
    def test(cls, fun: Type.FunT, test_in: List[List[Decimal]]) -> List[Decimal]:
        """
        Test function for trigonometric function.

        It just call corresponding target function and evaluate it at test input points.

        :param fun: Function to be tested.
        :type fun: Type.FunT
        :param test_in: Test input.
        :type test_in: List[List[Decimal]]

        :return: Test output.
        :rtype: List[Decimal]
        """
        if fun == Type.FunT.SIN:
            return list(map(lambda x: Decimal(cls.__sin(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.COS:
            return list(map(lambda x: Decimal(cls.__cos(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.TAN:
            return list(map(lambda x: Decimal(cls.__tan(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.CSC:
            return list(map(lambda x: Decimal(cls.__csc(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.SEC:
            return list(map(lambda x: Decimal(cls.__sec(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.COT:
            return list(map(lambda x: Decimal(cls.__cot(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.ASIN:
            return list(map(lambda x: Decimal(cls.__asin(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.ACOS:
            return list(map(lambda x: Decimal(cls.__acos(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.ATAN:
            return list(map(lambda x: Decimal(cls.__atan(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.ACSC:
            return list(map(lambda x: Decimal(cls.__acsc(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.ASEC:
            return list(map(lambda x: Decimal(cls.__asec(*list(map(float, x)))), test_in))
        else:
            return list(map(lambda x: Decimal(cls.__acot(*list(map(float, x)))), test_in))
