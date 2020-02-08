import math
from decimal import Decimal
from typing import Dict, List, Tuple, Optional, final

from Core import Type, Token, Warning
from Util.Macro import is_bigint, is_smallint


@final
class SpecialFunc:
    """
    Special function toolbox.

    :cvar __sign: Signatures of special functions.
    """
    __sign: Dict[Type.FunT, List[Type.Sign]] = {
        Type.FunT.GAMMA: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.GAMMA)],
        Type.FunT.LGAMMA: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.LGAMMA)],
        Type.FunT.ERF: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ERF)],
        Type.FunT.ERFC: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ERFC)]
    }

    def __init__(self) -> None:
        raise NotImplementedError

    def __del__(self) -> None:
        raise NotImplementedError

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
        Simplifier for hyperbolic trigonometric functions.

        It does following simplifications.
            1. Constant folding.
            2. Dead expression stripping.
            3. Sign propagation.
        For details and detailed explanation of optimization tricks, consult following references and comments of
        ``Operator.simplify``, ``Function.Trigonometric``, and references therein.

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

        if rt.v == Type.FunT.GAMMA:
            # Check for warnings.
            # Gamma function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max size. (BIG_INT)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite nonpositive integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Gamma"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 23))
                    rt.chd[0].v = 0
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Gamma"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Gamma"))
                elif rt.chd[0].v % 1 == 0 and rt.chd[0].v <= 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 23))

            # Constant folding.
            # Gamma function with parameter x has following rules.
            #   1. If x is nan or -inf, the result is nan.
            #   2. If x is +inf, the result is +inf.
            #   3. If x is finite nonpositive integer, the result is nan.
            #   4. If x is finite, the result is ``math.gamma(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if (math.isinf(rt.chd[0].v) or rt.chd[0].v % 1 == 0) and rt.chd[0].v <= 0:
                    rt.chd[0].v = math.nan
                else:
                    try:
                        rt.chd[0].v = math.gamma(rt.chd[0].v)
                    except OverflowError:
                        rt.chd[0].v = math.inf

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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Lgamma"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 24))
                    rt.chd[0].v = 0
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Lgamma"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Lgamma"))
                elif rt.chd[0].v % 1 == 0 and rt.chd[0].v <= 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 24))

            # Constant folding.
            # Loggamma function with parameter x has following rules.
            #   1. If x is nan or -inf, the result is nan.
            #   2. If x is +inf, the result is +inf.
            #   3. If x is finigte nonpositive integer, the result if nan.
            #   4. If x is finite, the result is ``math.lgamma(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if (math.isinf(rt.chd[0].v) or rt.chd[0].v % 1 == 0) and rt.chd[0].v <= 0:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.lgamma(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.ERF:
            # Check for warnings.
            # Error function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Erf"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Erf"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Erf"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Erf"))

            # Constant folding.
            # Error function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   1. If x is +-inf, the result is +-1, resp.
            #   3. If x is finite, the result is ``math.erf(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = math.erf(rt.chd[0].v)

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
        else:
            # Check for warnings.
            # Complementary error function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   3. x is nan. (NAN_DETECT)
            #   4. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Erfc"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Erfc"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Erfc"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Erfc"))

            # Constant folding.
            # Complementary error function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   2. If x is +-inf, the result is 0, 2, resp.
            #   3. If x is finite, the result is ``math.erfc(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = math.erfc(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn

    @classmethod
    def test(cls, fun: Type.FunT, test_in: List[Decimal]) -> List[Decimal]:
        """
        Test function for special function.

        It just call corresponding target function anc evaluate it at test input points.

        :param fun: Function to be tested.
        :type fun: Type.FunT
        :param test_in: Test input.
        :type test_in: List[Decimal]

        :return: Test output.
        :rtype: List[Decimal]
        """
        if fun == Type.FunT.GAMMA:
            return list(map(lambda x: Decimal(math.gamma(float(x))), test_in))
        elif fun == Type.FunT.LGAMMA:
            return list(map(lambda x: Decimal(math.lgamma(float(x))), test_in))
        elif fun == Type.FunT.ERF:
            return list(map(lambda x: Decimal(math.erf(float(x))), test_in))
        else:
            return list(map(lambda x: Decimal(math.erfc(float(x))), test_in))