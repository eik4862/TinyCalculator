import math
from decimal import Decimal
from typing import Dict, List, Tuple, Optional, final

from Core import Type, Token, Warning
from Util.Macro import is_bigint, is_smallint, is_int


@final
class SpecialFun:
    """
    Special function toolbox.

    :cvar __sign: Signatures of special functions.
    """
    __sign: Dict[Type.FunT, List[Type.Sign]] = {
        Type.FunT.ERF: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ERF)],
        Type.FunT.ERFC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ERFC)],
        Type.FunT.GAMMA: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.GAMMA)],
        Type.FunT.LGAMMA: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.LGAMMA)],
        Type.FunT.RECIGAMMA: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.RECIGAMMA)],
        Type.FunT.BESSELCLIFFORD: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.BESSELCLIFFORD)],
        Type.FunT.BETA: [Type.Sign([Type.T.NUM, Type.T.NUM], Type.T.NUM, Type.FunT.BETA)],
        Type.FunT.CENTRALBETA: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.CENTRALBETA)],
        Type.FunT.SINC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.SINC)],
        Type.FunT.TANC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.TANC)],
        Type.FunT.SINHC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.SINHC)],
        Type.FunT.COSHC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.COSHC)],
        Type.FunT.TANHC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.TANHC)],
        Type.FunT.DIRICHLETKERNEL: [Type.Sign([Type.T.NUM, Type.T.NUM], Type.T.NUM, Type.FunT.DIRICHLETKERNEL)],
        Type.FunT.FEJERKERNEL: [Type.Sign([Type.T.NUM, Type.T.NUM], Type.T.NUM, Type.FunT.FEJERKERNEL)],
        Type.FunT.TOPOLOGISTSIN: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.TOPOLOGISTSIN)]
    }

    def __init__(self) -> None:
        raise NotImplementedError

    def __del__(self) -> None:
        raise NotImplementedError

    @classmethod
    def __erf(cls, x: float) -> float:
        """
        Error function.

        Error function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is +-1, resp.
            3. If x is finite, the result is ``math.erf(x)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where error function is to be computed.
        :type x: float

        :return: Computed value of error function.
        :rtype: float
        """
        return math.erf(x)

    @classmethod
    def __erfc(cls, x: float) -> float:
        """
        Complementary error function.

        Complementary error function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is 0, 2, resp.
            3. If x is finite, the result is ``math.erfc(x)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where complementary error function is to be computed.
        :type x: float

        :return: Computed value of complementary error function.
        :rtype: float
        """
        return math.erfc(x)

    @classmethod
    def __gamma(cls, x: float) -> float:
        """
        Gamma function.

        Gamma function with parameter x has following computation rules.
            1. If x is nan or -inf, the result is nan.
            2. If x is +inf, the result is +inf.
            3. If x is finite nonpositive integer, the result is nan.
            4. If x is finite, the result is ``math.gamma(x)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where gamma function is to be computed.
        :type x: float

        :return: Computed value of gamma function.
        :rtype: float
        """
        if x == -math.inf or (is_int(x) and x <= 0):
            return math.nan
        else:
            try:
                return math.gamma(x)
            except OverflowError:
                return math.inf

    @classmethod
    def __lgamma(cls, x: float) -> float:
        """
        Log gamma function.

        Log gamma function with parameter x has following computation rules.
            1. If x is nan or -inf, the result is nan.
            2. If x is +inf, the result is +inf.
            3. If x is finite nonpositive integer, the result if nan.
            4. If x is finite, the result is ``math.lgamma(x)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where log gamma function is to be computed.
        :type x: float

        :return: Computed value of log gamma function.
        :rtype: float
        """
        return math.nan if x == -math.inf or (is_int(x) and x <= 0) else math.lgamma(x)

    @classmethod
    def __recigamma(cls, x: float) -> float:
        """
        Reciprocal gamma function.

        Reciprocal gamma function with parameter x has following computation rules.
            1. If x is nan or -inf, the result is nan.
            2. If x is +inf, the result is 0.
            3. If x is finite, the result is ``1 / math.gamma(x)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where reciprocal gamma function is to be computed.
        :type x: float

        :return: Computed value of reciprocal gamma function.
        :rtype: float
        """
        if math.isinf(x):
            return math.nan if x < 0 else 0
        elif is_int(x) and x <= 0:
            return 0
        else:
            try:
                return 1 / math.gamma(x)
            except OverflowError:
                return 0

    @classmethod
    def __bessel_clifford(cls, x: float) -> float:
        """
        Bessel-Clifford function.

        Bessel-Clifford function with parameter x has following computation rules.
            1. If x is nan or -inf, the result is nan.
            2. If x is +inf, the result is 0.
            3. If x is finite, the result is ``1 / math.gamma(x + 1)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where Bessel-Clifford function is to be computed.
        :type x: float

        :return: Computed value of Bessel-Clifford function.
        :rtype: float
        """
        if math.isinf(x):
            return math.nan if x < 0 else 0
        elif is_int(x) and x < 0:
            return 0
        else:
            try:
                return 1 / math.gamma(x + 1)
            except OverflowError:
                return 0

    @classmethod
    def __beta(cls, x: float, y: float) -> float:
        """
        Beta function.

        Beta function with parameter x and y has following computation rules.
            1. If x or y is nan, -inf, or finite nonpositive integer, the result is nan.
            2. If x and y are both inf, the result is 0.
            3. If x is inf and y is either finite positive or in (2n, 2n+1) for some finite negative integer n, the
               result is inf.
            4. If x is inf and y is in (2n-1, 2n) for some finite nonpositive integer n, the result is -inf.
            5. If y is inf and x is either finite positive or in (2n, 2n+1) for some finite negative integer n, the
               result is inf.
            6. If y is inf and x is in (2n-1, 2n) for some finite nonpositive integer n, the result is -inf.
            7. If x and y are both either finite positive or finite negative noninteger, the result is
               ``math.exp(math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y))`` multiplied by proper sign.
        Here, rule 7 is based on the identity ``B(x, y) = gamma(x) * gamma(y) / gamma(x + y)``.
        Since this identity is vulnerable to overflow, we take logarithm and take exponential again.
        Before taking logarithm, we must take absolute value first and the lost sign information can be recovered
        latter using the fact that ``gamma(x)`` is positive iff x is finite positive or in (2n, 2n+1) for some finite
        negative integer n.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: First coordinate of point where beta function is to be computed.
        :type x: float
        :param y: Second coordinate of point where beta function is to be computed.
        :type y: float

        :return: Computed value of beta function.
        :rtype: float
        """
        if ((is_int(x) or math.isinf(x)) and x <= 0) or ((is_int(y) or math.isinf(y)) and y <= 0):
            return math.nan
        elif math.isinf(x):
            return 0 if math.isinf(y) else math.inf if y > 0 or math.ceil(y) % 2 == 1 else -math.inf
        elif math.isinf(y):
            return math.inf if x > 0 or math.ceil(x) % 2 == 1 else -math.inf
        elif is_int(x + y) and (x + y) <= 0:
            return 0
        else:
            sgn = 1

            if x < 0 and math.ceil(x) % 2 == 0:
                sgn *= -1

            if y < 0 and math.ceil(y) % 2 == 0:
                sgn *= -1

            if x + y < 0 and math.ceil(x + y) % 2 == 0:
                sgn *= -1

            try:
                return sgn * math.exp(math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y))
            except OverflowError:
                return sgn * math.inf

    @classmethod
    def __cenbeta(cls, x: float) -> float:
        """
        Central beta function.

        Central beta function with parameter x has following computation rules.
            1. If x is nan or -inf, the result is nan.
            2. If x is +inf, the result is 0.
            3. If x is finite nonpositive integer, the result is nan.
            4. If x is either finite positive or finite negative nonintger, the result is
               ``math.exp(math.lgamma(x) * 2 - math.lgamma(2 * x))``.
        Here, rule 4 is based on the identity ``B(x, x) = gamma(x)^2 / gamma(2x)``.
        Since this identity is vulnerable to overflow, we take logarithm and take exponential again.
        Before taking logarithm, we must take absolute value first and the lost sign information can be recovered
        latter using the fact that ``gamma(x)`` is positive iff x is finite positive or in (2n, 2n+1) for some finite
        negative integer n.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where central beta function is to be computed.
        :type x: float

        :return: Computed value of central beta function.
        :rtype: float
        """
        if x == math.inf:
            return 0
        elif is_int(x) and x <= 0:
            return math.nan
        elif 2 * is_int(x) and x <= 0:
            return 0
        else:
            sgn = 1 if x > 0 or x % 1 < 0.5 else -1

            try:
                return sgn * math.exp(math.lgamma(x) * 2 - math.lgamma(2 * x))
            except OverflowError:
                return sgn * math.inf

    @classmethod
    def __sinc(cls, x: float) -> float:
        """
        Sinc function.

        Sinc function with parameter x has following computation rules.
            1. If x is nan, the result is nan.
            2. If x is +-inf, the result is 0.
            3. If x is 0, the result is 1.
            4. If x is finite nonzero, the result is ``math.sin(x) / x``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where sinc function is to be computed.
        :type x: float

        :return: Computed value of sinc function.
        :rtype: float
        """
        return 1 if x == 0 else math.sin(x) / x

    @classmethod
    def __tanc(cls, x: float) -> float:
        """
        Tanc function.

        Tanc function with parameter x has following computation rules.
           1. If x is nan or +-inf, the result is nan.
           2. If x is finite integer multiple of pi + pi/2, the result is nan.
           3. If x is 0, the result is 1.
           4. If x is finite nonzero and not integer multiple of pi + pi/2, the result is ``math.tan(x) / x``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where tanc function is to be computed.
        :type x: float

        :return: Computed value of tanc function.
        :rtype: float
        """
        return math.nan if math.isinf(x) or (x - math.pi / 2) % math.pi == 0 else 0 if x == 0 else math.tan(x) / x

    @classmethod
    def __sinhc(cls, x: float) -> float:
        """
        Sinhc function.

        Sinhc function with parameter x has following computation rules.
           1. If x is nan, the result is nan.
           2. If x is +-inf, the result is inf.
           3. If x is 0, the result is 1.
           4. If x is finite nonzero, the result is ``math.sinh(x) / x``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where sinhc function is to be computed.
        :type x: float

        :return: Computed value of sinhc function.
        :rtype: float
        """
        try:
            return 1 if x == 0 else math.sinh(x) / x
        except OverflowError:
            return math.inf

    @classmethod
    def __coshc(cls, x: float) -> float:
        """
        Coshc function.

        Coshc function with parameter x has following computation rules.
           1. If x is nan, the result is nan.
           2. If x is +-inf, the result is +-inf, resp.
           3. If x is 0, the result is nan.
           4. If x is finite nonzero, the result is ``math.cosh(x) / x``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where coshc function is to be computed.
        :type x: float

        :return: Computed value of coshc function.
        :rtype: float
        """
        try:
            return math.nan if x == 0 else math.cosh(x) / x
        except OverflowError:
            return math.inf if x > 0 else -math.inf

    @classmethod
    def __tanhc(cls, x: float) -> float:
        """
        Tanhc function.

        Tanhc function with parameter x has following computation rules.
           1. If x is nan, the result is nan.
           2. If x is +-inf, the result is 0≥
           3. If x is 0, the result is 1.
           4. If x is finite nonzero, the result is ``math.tanh(x) / x``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where tanhc function is to be computed.
        :type x: float

        :return: Computed value of tanhc function.
        :rtype: float
        """
        return 1 if x == 0 else math.tanh(x) / x

    @classmethod
    def __dirichlet_ker(cls, x: float, n: int) -> float:
        """
        Dirichlet kernel function.

        Dirichlet kernel function with parameter x and n has following computation rules.
           1. If x is nan or +-inf, the result is nan.
           2. If n is nan or +-inf, the result is nan.
           3. If n is not nonnegative integer, the result is nan.
           4. If n is 0, the result is 0.
           5. If x is finite and n is finite positive integer, the result is
              ``math.sin((n + 0.5) * x) / math.sin(x / 2)``.
        Here, rule 4 is based on the identity ``D_n(x) = sin((n + 1 / 2)x) / sin(x / 2)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where Dirichlet kernel function is to be computed.
        :type x: float

        :return: Computed value of Dirichlet kernel function.
        :rtype: float
        """
        if not math.isfinite(x + n) or n < 0 or not is_int(n):
            return math.nan
        else:
            return 1 if n == 0 else 2 * n + 1 if x % (2 * math.pi) == 0 else math.sin((n + 0.5) * x) / math.sin(x / 2)

    @classmethod
    def __fejer_ker(cls, x: float, n: int) -> float:
        """
        Fejer kernel function.

        Fejer kernel function with parameter x and n has following computation rules.
           1. If x is nan or +-inf, the result is nan.
           2. If n is nan or +-inf, the result is nan.
           3. If n is not positive integer, the result is nan.
           4. If n is 1, the result is 1.
           5. If x is finite and n is finite positive integer, the result is
              ``(1 - math.cos(n * x)) / (1 - math.cos(x)) / n``.
        Here, rule 4 is based on the identity ``F_n(x) = gamma(x)^2 / gamma(2x)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where Fejer kernel function is to be computed.
        :type x: float

        :return: Computed value of Fejer kernel function.
        :rtype: float
        """
        if not math.isfinite(x + n) or n <= 0:
            return math.nan
        else:
            return 1 if n == 1 else n if x % (2 * math.pi) == 0 else (1 - math.cos(n * x)) / (1 - math.cos(x)) / n

    @classmethod
    def __topo_sin(cls, x: float) -> float:
        """
        Topologist sine function.

        Topologist sine function with parameter x has following computation rules.
           1. If x is nan or -inf, the result is nan.
           2. If x is inf, the result is 0.
           3. If x is finite nonpositive, the result is nan.
           4. If x is finite positive, the result is ``math.sin(1 / x)``.

        This method is private and called internally as a helper of ``SpeiclFun.simplify``.
        For detailed description for simplification, refer to the comments of ``SpeiclFun.simplify``.

        :param x: Point where topologist sine function is to be computed.
        :type x: float

        :return: Computed value of topologist sine function.
        :rtype: float
        """
        return math.nan if x <= 0 else math.sin(1 / x)

    @classmethod
    def chk_t(cls, rt: Token.FunTok) -> Optional[List[Type.Sign]]:
        """
        Type checker for special functions.
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
        Simplifier for special functions.

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

        if rt.v == Type.FunT.ERF:
            # Check for warnings.
            # Error function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Erf'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Erf'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Erf'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Erf'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__erf``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__erf(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Erf[-x] = -Erf[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ERFC:
            # Check for warnings.
            # Complementary error function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Erfc'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Erfc'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Erfc'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Erfc'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__erfc``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__erfc(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.GAMMA:
            # Check for warnings.
            # Gamma function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite nonpositive integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Gamma'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Gamma'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Gamma'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Gamma'))
                elif is_int(rt.chd[0].v) and rt.chd[0].v <= 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 23))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__gamma``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__gamma(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.LGAMMA:
            # Check for warnings.
            # Loggamma function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite nonpositive integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Lgamma'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Lgamma'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Lgamma'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Lgamma'))
                elif is_int(rt.chd[0].v) and rt.chd[0].v <= 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 24))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__lgamma``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__lgamma(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.RECIGAMMA:
            # Check for warnings.
            # Reciprocal gamma function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Recigamma'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Recigamma'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Recigamma'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Recigamma'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__recigamma``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__recigamma(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.BESSELCLIFFORD:
            # Check for warnings.
            # Bessel-Clifford function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Besselclifford'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Besselclifford'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Besselclifford'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Besselclifford'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__bessel_clifford``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__bessel_clifford(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.BETA:
            # Check for warnings.
            # Beta function with parameter x and y generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   1. y exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   5. y is nan. (NAN_DETECT)
            #   6. y is +-inf. (INF_DETECT)
            #   7. x is finite nonpositive integer and y is finite. (POLE_DETECT)
            #   8. x is finite and y is finite nonpositive integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Beta'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Beta'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Beta'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Beta'))

                if is_bigint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=2, handle='Beta'))
                    rt.chd[1].v = math.inf
                elif is_smallint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=2, handle='Beta'))
                    rt.chd[1].v = -math.inf
                elif math.isnan(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=2, handle='Beta'))
                elif math.isinf(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=2, handle='Beta'))

                if math.isfinite(rt.chd[0].v + rt.chd[1].v):
                    if rt.chd[0].v <= 0 and is_int(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 31))
                    elif rt.chd[1].v <= 0 and is_int(rt.chd[1].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 31))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__beta``.
            if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__beta(rt.chd[0].v, rt.chd[1].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Beta[nan, y] = nan
            #   2. Beta[-inf, y] = nan
            #   3. Beta[n, y] = nan
            #   4. Beta[x, nan] = nan
            #   5. Beta[x, -inf] = nan
            #   6. Beta[x, n] = nan
            # where n is finite nonpositive integer.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM and not is_bigint(rt.chd[0].v):
                if is_smallint(rt.chd[0].v) or math.isnan(rt.chd[0].v) or rt.chd[0].v == -math.inf or \
                        (is_int(rt.chd[0].v) and rt.chd[0].v <= 0):
                    rt.chd[0].v = math.nan

                    return rt.chd[0], warn
            elif rt.chd[1].tok_t == Type.TokT.NUM and not is_bigint(rt.chd[1].v):
                if is_smallint(rt.chd[1].v) or math.isnan(rt.chd[1].v) or rt.chd[1].v == -math.inf or \
                        (is_int(rt.chd[1].v) and rt.chd[1].v <= 0):
                    rt.chd[1].v = math.nan

                    return rt.chd[1], warn

            return rt, warn
        elif rt.v == Type.FunT.CENTRALBETA:
            # Check for warnings.
            # Central beta function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite nonpositive integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Centralbeta'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Centralbeta'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Centralbeta'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Centralbeta'))
                elif is_int(rt.chd[0].v) and rt.chd[0].v <= 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 40))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__cenbeta``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__cenbeta(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.SINC:
            # Check for warnings.
            # Sinc function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Sinc'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Sinc'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Sinc'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Sinc'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__sinc``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__sinc(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Sinc[-x] = Sinc[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.TANC:
            # Check for warnings.
            # Tanc function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is integer multiple of pi + pi/2. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Tanc'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Tanc'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Tanc'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Tanc'))
                elif (rt.chd[0].v - math.pi / 2) % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 41))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__tanc``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__tanc(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Tanc[-x] = Tanc[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.SINHC:
            # Check for warnings.
            # Sinhc function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Sinhc'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Sinhc'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Sinhc'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Sinhc'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__sinhc``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__sinhc(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Sinhc[-x] = Sinhc[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.COSHC:
            # Check for warnings.
            # Coshc function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is 0. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Coshc'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Coshc'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Coshc'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Coshc'))
                elif rt.chd[0].v == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 42))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__coshc``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__coshc(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Coshc[-x] = -Coshc[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)
                tmp.swap_chd(rt, 0)

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.TANHC:
            # Check for warnings.
            # Tanhc function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Tanhc'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Tanhc'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Tanhc'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Tanhc'))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__tanhc``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__tanhc(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Tanhc[-x] = Tanhc[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.DIRICHLETKERNEL:
            # Check for warnings.
            # Dirichlet kernel with parameter x and n generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. n exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   5. n is nan. (NAN_DETECT)
            #   6. n is +-inf. (INF_DETECT)
            #   7. n is not nonnegative integer. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Dirichletkernel'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Dirichletkernel'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Dirichletkernel'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Dirichletkernel'))

                if is_bigint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=2, handle='Dirichletkernel'))
                    rt.chd[1].v = math.inf
                elif is_smallint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=2, handle='Dirichletkernel'))
                    rt.chd[1].v = -math.inf
                elif math.isnan(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=2, handle='Dirichletkernel'))
                elif math.isinf(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=2, handle='Dirichletkernel'))
                elif rt.chd[1].v < 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 44))
                elif not is_int(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 45))
                    rt.chd[1].v = round(rt.chd[1].v)

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__dirichlet_ker``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__dirichlet_ker(rt.chd[0].v, rt.chd[1].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Dirichletkernel[nan, n] = nan
            #   2. Dirichletkernel[+-inf, n] = nan
            #   3. Dirichletkernel[x, nan] = nan
            #   4. Dirichletkernel[x, +-inf] = nan
            #   5. Dirichletkernel[x, y] = nan
            #   6. Dirichletkernel[-x, n] = Dirichletkernel[x, n]
            # where y is finite negative.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v) or is_smallint(rt.chd[0].v) or math.isnan(rt.chd[0].v) or \
                        math.isinf(rt.chd[0].v):
                    rt.chd[0].v = math.nan

                    return rt.chd[0], warn
            elif rt.chd[1].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[1].v) or is_smallint(rt.chd[1].v) or math.isnan(rt.chd[1].v) or \
                        math.isinf(rt.chd[1].v) or rt.chd[1].v < 0:
                    rt.chd[1].v = math.nan

                    return rt.chd[1], warn
            elif rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        elif rt.v == Type.FunT.FEJERKERNEL:
            # Check for warnings.
            # Fejer kernel with parameter x and n generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. n exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   5. n is nan. (NAN_DETECT)
            #   6. n is +-inf. (INF_DETECT)
            #   7. n is not positive integer. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Fejerkernel'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Fejerkernel'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Fejerkernel'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Fejerkernel'))

                if is_bigint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=2, handle='Fejerkernel'))
                    rt.chd[1].v = math.inf
                elif is_smallint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=2, handle='Fejerkernel'))
                    rt.chd[1].v = -math.inf
                elif math.isnan(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=2, handle='Fejerkernel'))
                elif math.isinf(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=2, handle='Fejerkernel'))
                elif rt.chd[1].v < 0.5:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 46))
                elif not is_int(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 47))
                    rt.chd[1].v = round(rt.chd[1].v)

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__fejer_ker``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__fejer_ker(rt.chd[0].v, rt.chd[1].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Fejerkernel[nan, n] = nan
            #   2. Fejerkernel[+-inf, n] = nan
            #   3. Fejerkernel[x, nan] = nan
            #   4. Fejerkernel[x, +-inf] = nan
            #   5. Fejerkernel[x, y] = nan
            #   6. Fejerkernel[-x, n] = Fejerkernel[x, n]
            # where y is finite real less than 0.5.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v) or is_smallint(rt.chd[0].v) or math.isnan(rt.chd[0].v) or \
                        math.isinf(rt.chd[0].v):
                    rt.chd[0].v = math.nan

                    return rt.chd[0], warn
            elif rt.chd[1].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[1].v) or is_smallint(rt.chd[1].v) or math.isnan(rt.chd[1].v) or \
                        math.isinf(rt.chd[1].v) or rt.chd[1].v < 0.5:
                    rt.chd[1].v = math.nan

                    return rt.chd[1], warn
            elif rt.chd[0].v == Type.OpT.MINUS:
                rt.swap_chd(rt.chd[0].chd[0], 0)

                return rt, warn

            return rt, warn
        else:
            # Check for warnings.
            # Topologist's sine function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite nonpositive. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Topologistsin'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle='Topologistsin'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Topologistsin'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Topologistsin'))
                elif rt.chd[0].v <= 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 43))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__topo_sin``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__topo_sin(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn

    @classmethod
    def test(cls, fun: Type.FunT, test_in: List[List[Decimal]]) -> List[Decimal]:
        """
        Test function for special function.

        It just call corresponding target function and evaluate it at test input points.

        :param fun: Function to be tested.
        :type fun: Type.FunT
        :param test_in: Test input.
        :type test_in: List[List[Decimal]]

        :return: Test output.
        :rtype: List[Decimal]
        """
        if fun == Type.FunT.ERF:
            return list(map(lambda x: Decimal(cls.__erf(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.ERFC:
            return list(map(lambda x: Decimal(cls.__erfc(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.GAMMA:
            return list(map(lambda x: Decimal(cls.__gamma(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.LGAMMA:
            return list(map(lambda x: Decimal(cls.__lgamma(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.RECIGAMMA:
            return list(map(lambda x: Decimal(cls.__recigamma(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.BESSELCLIFFORD:
            return list(map(lambda x: Decimal(cls.__bessel_clifford(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.BETA:
            return list(map(lambda x: Decimal(cls.__beta(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.CENTRALBETA:
            return list(map(lambda x: Decimal(cls.__cenbeta(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.SINC:
            return list(map(lambda x: Decimal(cls.__sinc(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.TANC:
            return list(map(lambda x: Decimal(cls.__tanc(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.SINHC:
            return list(map(lambda x: Decimal(cls.__sinhc(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.COSHC:
            return list(map(lambda x: Decimal(cls.__coshc(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.TANHC:
            return list(map(lambda x: Decimal(cls.__tanhc(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.DIRICHLETKERNEL:
            return list(map(lambda x: Decimal(cls.__dirichlet_ker(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.FEJERKERNEL:
            return list(map(lambda x: Decimal(cls.__fejer_ker(*list(map(float, x)))), test_in))
        elif fun == Type.FunT.TOPOLOGISTSIN:
            return list(map(lambda x: Decimal(cls.__topo_sin(*list(map(float, x)))), test_in))
