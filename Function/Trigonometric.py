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
        Type.FunT.ASIN: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ASIN)],
        Type.FunT.ACOS: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ACOS)],
        Type.FunT.ATAN: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.ATAN)]
    }

    def __init__(self) -> None:
        raise NotImplementedError

    def __del__(self) -> None:
        raise NotImplementedError

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

    @classmethod
    def simplify(cls, rt: Token.FunTok) -> Tuple[Token.Tok, List[Warning.InterpWarn]]:
        """
        Simplifier for trigonometric functions.

        It does following simplifications.
            1. Constant folding.
            2. Dead expression stripping.
            3. Function coalescing.
               Some functions have inverse relation with other function and using this, the expression can be reduced.
               For example, ``Sin[Asin[2]]`` can be reduced to simple one NUM token ``2``.
               Note that this does not necessarily mean ``Asin[Sin[2]]`` can be reduced to ``2`` since the range of
               arcsine is [-pi/2, pi/2].
            4. Sign propagation.
        Function coalescing is originally part of optimization trick in dynamic memory allocation.
        For details and detailed explanation of other optimization tricks, consult following references and comments of
        ``Operator.simplify`` and references therein.

        **Reference**
            * https://en.wikipedia.org/wiki/Coalescing_(computer_science)

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

        if rt.v == Type.FunT.SIN:
            # Check for warnings.
            # Sine function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Sin"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Sin"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Sin"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Sin"))

            # Constant folding.
            # Sine function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite, the result is ``math.sin(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v):
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.sin(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Sin[-x] = -Sin[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                sgn = True
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)

            # Function coalescing.
            # For function coalescing, it uses following rule.
            #   1. Sin[Asin[x]] = x
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.FunT.ASIN:
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
        elif rt.v == Type.FunT.COS:
            # Check for warnings.
            # Cosine function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Cos"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Cos"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Cos"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Cos"))

            # Constant folding.
            # Cosine function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite, the result is ``math.cos(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v):
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.cos(rt.chd[0].v)

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. Cos[-x] = Cos[x]
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                rt.chd = rt.chd[0].chd

            # Function coalescing.
            # For function coalescing, it uses following rule.
            #   1. Cos[Acos[x]] = x
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.FunT.ACOS:
                return rt.chd[0].chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.TAN:
            # Check for warnings.
            # Tangent function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is integer multiple of pi/2. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Tan"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Tan"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Tan"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Tan"))
                elif rt.chd[0].v % (math.pi / 2) == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 5))

            # Constant folding.
            # Tangent function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is integer multiple of pi/2, the result is nan.
            #   3. If x is finite which is not integer multiple of pi/2, the result is ``math.tan(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v):
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.tan(rt.chd[0].v)

                return rt.chd[0], warn

            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. Tan[-x] = -Tan[x]
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS:
                sgn = True
                tmp = rt.chd[0]
                rt.swap_chd(rt.chd[0].chd[0], 0)

            # Function coalescing.
            # For function coalescing, it uses following rule.
            #   1. Tan[Atan[x]] = x
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.FunT.ATAN:
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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Asin"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Asin"))
                elif not (-1 <= rt.chd[0].v <= 1):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 3))

            # Constant folding.
            # Arcsine function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is not in [-1, 1], the result is nan.
            #   3. If x is finite which is in [-1. 1], the result is ``math.asin(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v) or not (-1 <= rt.chd[0].v <= 1):
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.asin(rt.chd[0].v)

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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Acos"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Acos"))
                elif not (-1 <= rt.chd[0].v <= 1):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 4))

            # Constant folding.
            # Arccosine function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is not in [-1, 1], the result is nan.
            #   3. If x is finite which is in [-1. 1], the result is ``math.acos(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v) or not (-1 <= rt.chd[0].v <= 1):
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.acos(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        else:
            # Check for warnings.
            # Arctangent function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Atan"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Atan"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Atan"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Atan"))

            # Constant folding.
            # Arctangent function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   2. If x is +-inf, the result is +-pi/2, resp.
            #   3. If x is finite, the result is ``math.atan(x)``
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = math.atan(rt.chd[0].v)

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

    @classmethod
    def test(cls, fun: Type.FunT, test_in: List[Decimal]) -> List[Decimal]:
        """
        Test function for trigonometric function.

        It just call corresponding target function anc evaluate it at test input points.

        :param fun: Function to be tested.
        :type fun: Type.FunT
        :param test_in: Test input.
        :type test_in: List[Decimal]

        :return: Test output.
        :rtype: List[Decimal]
        """
        if fun == Type.FunT.SIN:
            return list(map(lambda x: Decimal(math.sin(float(x))), test_in))
        elif fun == Type.FunT.COS:
            return list(map(lambda x: Decimal(math.cos(float(x))), test_in))
        elif fun == Type.FunT.TAN:
            return list(map(lambda x: Decimal(math.tan(float(x))), test_in))
        elif fun == Type.FunT.ASIN:
            return list(map(lambda x: Decimal(math.asin(float(x))), test_in))
        elif fun == Type.FunT.ACOS:
            return list(map(lambda x: Decimal(math.acos(float(x))), test_in))
        else:
            return list(map(lambda x: Decimal(math.atan(float(x))), test_in))
