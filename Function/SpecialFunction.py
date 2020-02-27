import math
import sys
from decimal import Decimal
from typing import Dict, List, Tuple, Optional, final

from Core import Type, Token, Warning
from Util.Macro import is_bigint, is_smallint


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
        Type.FunT.BETA: [Type.Sign([Type.T.NUM, Type.T.NUM], Type.T.NUM, Type.FunT.BETA)]
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
        if (math.isinf(x) or x % 1 == 0) and x <= 0:
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
        return math.nan if (math.isinf(x) or x % 1 == 0) and x <= 0 else math.lgamma(x)

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
        if (x % 1 == 0 and x <= 0) or (y % 1 == 0 and y <= 0):
            return math.nan
        elif math.isinf(x):
            return 0 if math.isinf(y) else math.inf if y > 0 or math.ceil(y) % 2 == 1 else -math.inf
        elif math.isinf(y):
            return math.inf if x > 0 or math.ceil(x) % 2 == 1 else -math.inf
        elif (x + y) % 1 == 0 and (x + y) <= 0:
            return 0
        else:
            sgn = 1

            if x < 0 and math.ceil(x) % 2 == 0:
                sgn *= -1

            if y < 0 and math.ceil(y) % 2 == 0:
                sgn *= -1

            if x + y < 0 and math.ceil(x + y) % 2 == 0:
                sgn *= -1

            return sgn * math.exp(math.lgamma(x) + math.lgamma(y) - math.lgamma(x + y))

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
        For details and detailed explanation of optimization tricks, consult following references and comments of
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

                return tmp, warn

            return rt, warn
        elif rt.v == Type.FunT.ERFC:
            # Check for warnings.
            # Complementary error function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   3. x is nan. (NAN_DETECT)
            #   4. x is +-inf. (INF_DETECT)
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
            #   1. x exceeds floating point max size. (BIG_INT)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite nonpositive integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Gamma'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 23))
                    rt.chd[0].v = 0
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Gamma'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Gamma'))
                elif rt.chd[0].v % 1 == 0 and rt.chd[0].v <= 0:
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
            #   1. x exceeds floating point max size. (BIG_INT)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite nonpositive integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Lgamma'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 24))
                    rt.chd[0].v = 0
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Lgamma'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Lgamma'))
                elif rt.chd[0].v % 1 == 0 and rt.chd[0].v <= 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 24))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__lgamma``.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__lgamma(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        else:
            # Check for warnings.
            # Beta function with parameter x and y generates warning for followings cases.
            #   1. x exceeds floating point max size. (BIG_INT)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. y exceeds floating point max size. (BIG_INT)
            #   5. y is nan. (NAN_DETECT)
            #   6. y is +-inf. (INF_DETECT)
            #   7. x is finite nonpositive integer and y is finite. (POLE_DETECT)
            #   8. x is finite and y is finite nonpositive integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle='Beta'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    rt.chd[0].v = -1
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle='Beta'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle='Beta'))

            if rt.chd[1].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=2, handle='Beta'))
                    rt.chd[1].v = math.inf
                elif is_smallint(rt.chd[1].v):
                    rt.chd[1].v = -1
                elif math.isnan(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=2, handle='Beta'))
                elif math.isinf(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=2, handle='Beta'))

            if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM and math.isfinite(rt.chd[0].v + rt.chd[1].v):
                if rt.chd[0].v <= 0 and rt.chd[0].v % 1 == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 31))
                elif rt.chd[1].v <= 0 and rt.chd[1].v % 1 == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 31))

            # Constant folding.
            # For detailed computation rule, refer to the comment in ``SpecialFun.__beta``.
            if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
                rt.chd[0].v = cls.__beta(rt.chd[0].v, rt.chd[1].v)

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
        else:
            return list(map(lambda x: Decimal(cls.__beta(*list(map(float, x)))), test_in))
