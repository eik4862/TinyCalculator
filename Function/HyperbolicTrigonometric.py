import math
from decimal import Decimal
from typing import Dict, List, Tuple, Optional, final

from Core import Type, Token, Warning
from Util.Macro import is_bigint, is_smallint


@final
class HyperTri:
    """
    Hyperbolic trigonometric function toolbox.

    :cvar __sign: Signatures of hyperbolic trigonometric functions.
    """
    __sign: Dict[Type.FunT, List[Type.Sign]] = {
        Type.FunT.SINH: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.SINH)],
        Type.FunT.COSH: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.COSH)],
        Type.FunT.TANH: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.TANH)],
        Type.FunT.ASINH: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ASINH)],
        Type.FunT.ACOSH: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ACOSH)],
        Type.FunT.ATANH: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ATANH)]
    }

    def __init__(self) -> None:
        raise NotImplementedError

    def __del__(self) -> None:
        raise NotImplementedError

    @classmethod
    def __sinh(cls, x: float) -> float:
        """
        Sine hyperbolic function.

        Sine hyperbolic function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is +-inf, resp.
            3. If x is finite, the result is ``math.sinh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where sine hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of sine hyperbolic function.
        :rtype: float
        """
        try:
            return math.sinh(x)
        except OverflowError:
            return math.inf if x > 0 else -math.inf

    @classmethod
    def __cosh(cls, x: float) -> float:
        """
        Cosine hyperbolic function.

        Cosine hyperbolic function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is inf.
            3. If x is finite, the result is ``math.cosh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where cosine hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of cosine hyperbolic function.
        :rtype: float
        """
        try:
            return math.cosh(x)
        except OverflowError:
            return math.inf

    @classmethod
    def __tanh(cls, x: float) -> float:
        """
        Tangent hyperbolic function.

        Tangent hyperbolic function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is inf.
            3. If x is finite, the result is ``math.cosh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where tangent hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of tangent hyperbolic function.
        :rtype: float
        """
        return math.tanh(x)

    @classmethod
    def __csch(cls, x: float) -> float:
        """
        Cosecant hyperbolic function.

        Cosecant hyperbolic function with parameter x has following computation rules.
            1. If x is nan or 0, the result is nan.
            2. If x is +-inf, the result is 0.
            3. If x is finite, the result is ``1 / math.sinh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where cosecant hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of cosecant hyperbolic function.
        :rtype: float
        """
        try:
            return math.nan if x == 0 else 1 / math.sinh(x)
        except OverflowError:
            return 0

    @classmethod
    def __sech(cls, x: float) -> float:
        """
        Secant hyperbolic function.

        Secant hyperbolic function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is 0.
            3. If x is finite, the result is ``1 / math.cosh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where secant hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of secant hyperbolic function.
        :rtype: float
        """
        try:
            return 1 / math.cosh(x)
        except OverflowError:
            return 0

    @classmethod
    def __coth(cls, x: float) -> float:
        """
        Cotangent hyperbolic function.

        Cotangent hyperbolic function with parameter x has following computation rules.
            1. If x is nan or 0, the result is nan.
            2. If x is +-inf, the result is +-1, resp.
            3. If x is finite, the result is ``1 / math.tanh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where cotangent hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of cotangent hyperbolic function.
        :rtype: float
        """
        return math.nan if x == 0 else 1 / math.tanh(x)

    @classmethod
    def __asinh(cls, x: float) -> float:
        """
        Arcsine hyperbolic function.

        Arcsine hyperbolic function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is +-inf, resp.
            3. If x is finite, the result is ``math.asinh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where arcsine hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of arcsine hyperbolic function.
        :rtype: float
        """
        return math.asinh(x)

    @classmethod
    def __acosh(cls, x: float) -> float:
        """
        Arccosine hyperbolic function.

        Arccosine hyperbolic function with parameter x has following computation rules.
            1. If x is +inf, the result is inf.
            2. If x is -inf or nan, the result is nan
            3. If x is finite which is not in [1, inf), the result is nan.
            4. If x is finite which is in [1, inf), the result is ``math.acosh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where arccosine hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of arccosine hyperbolic function.
        :rtype: float
        """
        return math.nan if x < 1 else math.acosh(x)

    @classmethod
    def __atanh(cls, x: float) -> float:
        """
        Arctangent hyperbolic function.

        Arctangent hyperbolic function with parameter x has following computation rules.
            1. If x is +-inf or nan, the result is nan.
            2. If x is finite which is not in (-1, 1), the result is nan.
            3. If x is +-1, then the result is +-inf.
            4. If x is finite which is in (-1, 1), the result is ``math.atanh(x)``.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        :param x: Point where arctangent hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of arctangent hyperbolic function.
        :rtype: float
        """
        return math.nan if x < -1 or x > 1 else math.inf if x == 1 else -math.inf if x == -1 else math.atanh(x)

    @classmethod
    def __acsch(cls, x: float) -> float:
        """
        Arccosecant hyperbolic function.

        Arccosecant hyperbolic function with parameter x has following computation rules.
            1. If x is nan or 0, the result is nan.
            2. If x is +-inf, the result is 0.
            3. If x is finite, the result is ``math.asinh(1 / x)``.
        Here, the rule 3 is based on identity ``acsch(x) = asinh(1 / x)``.
        For detail and more identities, consult the reference below.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        **Reference**
            * https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions

        :param x: Point where arccosecant hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of arccosecant hyperbolic function.
        :rtype: float
        """
        return math.nan if x == 0 else math.asinh(1 / x)

    @classmethod
    def __asech(cls, x: float) -> float:
        """
        Arcsecant hyperbolic function.

        Arcsecant hyperbolic function with parameter x has following computation rules.
            1. If x is nan or +-inf, the result is nan.
            2. If x is 0, the result is inf.
            3. If x is finite not in (0, 1], the result is nan.
            4. If x is in (0, 1], the result is ``math.acosh(1 / x)``.
        Here, the rule 4 is based on identity ``asech(x) = acosh(1 / x)``.
        For detail and more identities, consult the reference below.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        **Reference**
            * https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions

        :param x: Point where arcsecant hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of arcsecant hyperbolic function.
        :rtype: float
        """
        return math.nan if x < 0 or x > 1 else math.inf if x == 0 else math.acosh(1 / x)

    @classmethod
    def __acoth(cls, x: float) -> float:
        """
        Arccotangent hyperbolic function.

        Arccotangent hyperbolic function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is 0.
            3. If x is +-1, the result is +-inf.
            4. If x is in (-1, 1), the result is nan.
            5. If x is finite not in [-1, 1], the result is ``math.atanh(1 / x)``.
        Here, the rule 5 is based on identity ``acoth(x) = atanh(1 / x)``.
        For detail and more identities, consult the reference below.

        This method is private and called internally as a helper of ``HyperTri.simplify``.
        For detailed description for simplification, refer to the comments of ``HyperTri.simplify``.

        **Reference**
            * https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions

        :param x: Point where arccotangent hyperbolic function is to be computed.
        :type x: float

        :return: Computed value of arccotangent hyperbolic function.
        :rtype: float
        """
        return math.nan if -1 < x < 1 else math.inf if x == 1 else -math.inf if x == -1 else math.atanh(1 / x)

    @classmethod
    def chk_t(cls, rt: Token.FunTok) -> Optional[List[Type.Sign]]:
        """
        Type checker for hyperbolic trigonometric functions.
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

    @classmethod
    def simplify(cls, rt: Token.FunTok) -> Tuple[Token.Tok, List[Warning.InterpWarn]]:
        """
        Simplifier for hyperbolic trigonometric functions.

        It does following simplifications.
            1. Constant folding.
            2. Dead expression stripping.
            3. Sign propagation.
        For details and detailed explanation of these optimization tricks, refer to the comments of
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

        if rt.v == Type.FunT.SINH:
            # Check for warnings.
            # Sine hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Sinh"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Sinh"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Sinh"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Sinh"))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__sinh``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__sinh(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Sinh[-x] = -Sinh[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.COSH:
            # Check for warnings.
            # Cosine hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Cosh"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Cosh"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Cosh"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Cosh"))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__cosh``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__cosh(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Cosh[-x] = Cosh[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.TANH:
            # Check for warnings.
            # Tangent hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Tanh"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Tanh"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Tanh"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Tanh"))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__tanh``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__tanh(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Tanh[-x] = -Tanh[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.CSCH:
            # Check for warnings.
            # Cosecant hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is 0. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Csch"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Csch"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Csch"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Csch"))
                elif rt.chd[0].v == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 33))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__csch``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__csch(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Csch[-x] = -Csch[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.SECH:
            # Check for warnings.
            # Secant hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Sech"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Sech"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Sech"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Sech"))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__sech``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__sech(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Sech[-x] = Sech[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.COTH:
            # Check for warnings.
            # Cotangent hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is 0. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Coth"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Coth"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Coth"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Coth"))
                elif rt.chd[0].v == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 34))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__coth``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__coth(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Coth[-x] = -Coth[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ASINH:
            # Check for warnings.
            # Arcsine hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Asinh"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Asinh"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Asinh"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Asinh"))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__asinh``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__asinh(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Asinh[-x] = -Asinh[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ACOSH:
            # Check for warnings.
            # Arccosine hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is not in [1, Inf). (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Acosh"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Acosh"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Acosh"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Acosh"))
                elif rt.chd[0].v < 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 21))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__acosh``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__acosh(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.ATANH:
            # Check for warnings.
            # Arctangent hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)'
            #   4. x is +-1. (POLE_DETECT)
            #   5. x is not in (-1, 1). (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Atanh"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Atanh"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Atanh"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Atanh"))
                elif abs(rt.chd[0].v) == 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 32))
                elif not (-1 < rt.chd[0].v < 1):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 22))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__atanh``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__atanh(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Atanh[-x] = -Atanh[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ACSCH:
            # Check for warnings.
            # Arccosecant hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is 0. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Acsch"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Acsch"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Acsch"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Acsch"))
                elif rt.chd[0].v == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 35))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__acsch``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__acsch(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Acsch[-x] = -Acsch[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ASECH:
            # Check for warnings.
            # Arcsecant hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is 0. (POLE_DETECT)
            #   5. x is not in (0, 1]. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Asech"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Asech"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Asech"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Asech"))
                elif rt.chd[0].v == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 37))
                elif not (0 < rt.chd[0].v <= 1):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 36))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__asech``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__asech(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        else:
            # Check for warnings.
            # Arccotangent hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is +-1. (POLE_DETECT)
            #   5. x is in (-1, 1). (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Acoth"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Acoth"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Acoth"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Acoth"))
                elif abs(rt.chd[0].v) == 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 39))
                elif -1 < rt.chd[0].v < 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 38))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``HyperTri.__acoth``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__acoth(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Acoth[-x] = -Acoth[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn

    @classmethod
    def test(cls, fun: Type.FunT, test_in: List[List[Decimal]]) -> List[Decimal]:
        """
        Test function for hyperbolic trigonometric function.

        It just call corresponding target function and evaluate it at test input points.

        :param fun: Function to be tested.
        :type fun: Type.FunT
        :param test_in: Test input.
        :type test_in: List[List[Decimal]]

        :return: Test output.
        :rtype: List[Decimal]
        """
        if fun == Type.FunT.SINH:
            return list(map(lambda x: Decimal(cls.__sinh(float(*x))), test_in))
        elif fun == Type.FunT.COSH:
            return list(map(lambda x: Decimal(cls.__cosh(float(*x))), test_in))
        elif fun == Type.FunT.TANH:
            return list(map(lambda x: Decimal(cls.__tanh(float(*x))), test_in))
        elif fun == Type.FunT.CSCH:
            return list(map(lambda x: Decimal(cls.__csch(float(*x))), test_in))
        elif fun == Type.FunT.SECH:
            return list(map(lambda x: Decimal(cls.__sech(float(*x))), test_in))
        elif fun == Type.FunT.COTH:
            return list(map(lambda x: Decimal(cls.__coth(float(*x))), test_in))
        elif fun == Type.FunT.ASINH:
            return list(map(lambda x: Decimal(cls.__asinh(float(*x))), test_in))
        elif fun == Type.FunT.ACOSH:
            return list(map(lambda x: Decimal(cls.__acosh(float(*x))), test_in))
        elif fun == Type.FunT.ATANH:
            return list(map(lambda x: Decimal(cls.__atanh(float(*x))), test_in))
        elif fun == Type.FunT.ACSCH:
            return list(map(lambda x: Decimal(cls.__acsch(float(*x))), test_in))
        elif fun == Type.FunT.ASECH:
            return list(map(lambda x: Decimal(cls.__asech(float(*x))), test_in))
        else:
            return list(map(lambda x: Decimal(cls.__acoth(float(*x))), test_in))
