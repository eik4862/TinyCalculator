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
            3. Function coalescing.
            4. Sign propagation.
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
        sgn: bool = False  # Flag for sign propagation. True means there is sign propagation.
        tmp: Token.Tok = None  # Temporary variable holding token.
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
            # Sine hyperbolic function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   2. If x is +-inf, the result is +-inf, resp.
            #   3. If x is finite, the result is ``math.sinh(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = math.sinh(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Sinh[-x] = -Sinh[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                sgn = True
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)

            # Function coalescing.
            # For function coalescing, it uses following rule.
            #   1. Sinh[Asinh[x]] = x
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.FunT.ASINH:
                if sgn:
                    tmp.chd = rt.chd[0].chd

                    return tmp, warn
                else:
                    return rt.chd[0].chd[0], warn

            if sgn:
                tmp.swap_chd(rt, 0)

                return tmp, warn
            else:
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
            # Cosine hyperbolic function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   2. If x is +-inf, the result is +inf.
            #   3. If x is finite, the result is ``math.cosh(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = math.cosh(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Cosh[-x] = Cosh[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.chd = rt.chd[0].chd

            # Function coalescing.
            # For function coalescing, it uses following rule.
            #   1. Cosh[Acosh[x]] = x
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.FunT.ACOSH:
                return rt.chd[0].chd[0], warn

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
            # Tangent hyperbolic function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   1. If x is +-inf, the result is +-1, resp.
            #   3. If x is finite, the result is ``math.tanh(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = math.tanh(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Tanh[-x] = -Tanh[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                sgn = True
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)

            # Function coalescing.
            # For function coalescing, it uses following rule.
            #   1. Tanh[Atanh[x]] = x
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.FunT.ATANH:
                if sgn:
                    tmp.chd = rt.chd[0].chd
                else:
                    tmp = rt.chd[0].chd[0]

                return tmp, warn

            if sgn:
                tmp.swap_chd(rt, 0)

                return tmp, warn
            else:
                return rt, warn
        elif rt.v == Type.FunT.ASINH:
            # Check for warnings.
            # Arcsine hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   3. x is nan. (NAN_DETECT)
            #   4. x is +-inf. (INF_DETECT)
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
            # Arcsine hyperbolic function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is not in [-1, 1], the result is nan.
            #   3. If x is finite which is in [-1. 1], the result is ``math.asinh(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = math.asinh(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Asinh[-x] = -Asinh[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                sgn = True
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)

            # Function coalescing.
            # For function coalescing, it uses following rule.
            #   1. Asinh[Sinh[x]] = x
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.FunT.SINH:
                if sgn:
                    tmp.chd = rt.chd[0].chd

                    return tmp, warn
                else:
                    return rt.chd[0].chd[0], warn

            if sgn:
                tmp.swap_chd(rt, 0)

                return tmp, warn
            else:
                return rt, warn
        elif rt.v == Type.FunT.ACOSH:
            # Check for warnings.
            # Arccosine hyperbolic function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max. (BIG_INT)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is not in [1, Inf). (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Acosh"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 21))
                    rt.chd[0].v = 0
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Acosh"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Acosh"))
                elif rt.chd[0].v < 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 21))

            # Constant folding.
            # Arccosine hyperbolic function with parameter x has following rules.
            #   1. If x is +inf, the result is inf.
            #   2. If x is -inf or nan, the result is nan
            #   3. If x is finite which is not in [1, inf), the result is nan.
            #   4. If x is finite which is in [1, inf), the result is ``math.acosh(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if rt.chd[0].v < 1:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.acosh(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        else:
            # Check for warnings.
            # Arctangent hyperbolic function with parameter x generates warning for followings cases.
            #   1. x is nan. (NAN_DETECT)
            #   2. x is +-inf. (INF_DETECT)
            #   3. x is not in (-1, 1). (DOMAIN_OUT)
            #   4. x is +-1. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 22))
                    rt.chd[0].v = 2
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 22))
                    rt.chd[0].v = -2
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Atanh"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Atanh"))
                elif not (-1 < rt.chd[0].v < 1):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 22))
                elif abs(rt.chd[0].v) == 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 22))

            # Constant folding.
            # Arctangent hyperbolic function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is not in (-1, 1), the result is nan.
            #   3. If x is +-1, then the result is +-inf.
            #   4. If x is finite which is in (-1, 1), the result is ``math.atanh(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if not (-1 <= rt.chd[0].v <= 1):
                    rt.chd[0].v = math.nan
                elif rt.chd[0].v == -1:
                    rt.chd[0].v = -math.inf
                elif rt.chd[0].v == 1:
                    rt.chd[0].v = math.inf
                else:
                    rt.chd[0].v = math.atanh(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Atanh[-x] = -Atanh[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                sgn = True
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)

            # Function coalescing.
            # For function coalescing, it uses following rule.
            #   1. Atanh[Tanh[x]] = x
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.FunT.TANH:
                if sgn:
                    tmp.chd = rt.chd[0].chd

                    return tmp, warn
                else:
                    return rt.chd[0].chd[0], warn

            if sgn:
                tmp.swap_chd(rt, 0)

                return tmp, warn
            else:
                return rt, warn

    @classmethod
    def test(cls, fun: Type.FunT, test_in: List[Decimal]) -> List[Decimal]:
        """
        Test function for hyperbolic trigonometric function.

        It just call corresponding target function anc evaluate it at test input points.

        :param fun: Function to be tested.
        :type fun: Type.FunT
        :param test_in: Test input.
        :type test_in: List[Decimal]

        :return: Test output.
        :rtype: List[Decimal]
        """
        if fun == Type.FunT.SINH:
            return list(map(lambda x: Decimal(math.sinh(float(x))), test_in))
        elif fun == Type.FunT.COSH:
            return list(map(lambda x: Decimal(math.cosh(float(x))), test_in))
        elif fun == Type.FunT.TANH:
            return list(map(lambda x: Decimal(math.tanh(float(x))), test_in))
        elif fun == Type.FunT.ASINH:
            return list(map(lambda x: Decimal(math.asinh(float(x))), test_in))
        elif fun == Type.FunT.ACOSH:
            return list(map(lambda x: Decimal(math.acosh(float(x))), test_in))
        else:
            return list(map(lambda x: Decimal(math.atanh(float(x))), test_in))
