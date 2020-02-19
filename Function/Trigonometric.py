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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Tan"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Tan"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Tan"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Tan"))
                elif (rt.chd[0].v - math.pi / 2) % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 5))

            # Constant folding.
            # Tangent function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is integer multiple of pi+pi/2, the result is nan.
            #   3. If x is finite which is not integer multiple of pi+pi/2, the result is ``math.tan(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v) or (rt.chd[0].v - math.pi / 2) % math.pi == 0:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.tan(rt.chd[0].v)

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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Csc"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Csc"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Csc"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Csc"))
                elif rt.chd[0].v % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 26))

            # Constant folding.
            # Cosecant function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is integer multiple of pi, the result is nan.
            #   3. If x is finite which is not integer multiple of pi, the result is ``1 / math.sin(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v) or rt.chd[0].v % math.pi == 0:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = 1 / math.sin(rt.chd[0].v)

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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Sec"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Sec"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Sec"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Sec"))
                elif (rt.chd[0].v - math.pi / 2) % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 27))

            # Constant folding.
            # Secant function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is integer multiple of pi+pi/2, the result is nan.
            #   3. If x is finite which is not integer multiple of pi+pi/2, the result is ``1 / math.cos(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v) or (rt.chd[0].v - math.pi / 2) % math.pi == 0:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = 1 / math.cos(rt.chd[0].v)

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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Cot"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Cot"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Cot"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Cot"))
                elif rt.chd[0].v % math.pi == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 28))

            # Constant folding.
            # Cotangent function with parameter x has following rules.
            #   1. If x is +-inf or nan, the result is nan.
            #   2. If x is finite which is integer multiple of pi, the result is nan.
            #   3. If x is finite which is not integer multiple of pi, the result is ``1 / math.tan(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v) or rt.chd[0].v % math.pi == 0:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = 1 / math.tan(rt.chd[0].v)

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
        elif rt.v == Type.FunT.ATAN:
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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Acsc"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Acsc"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Acsc"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Acsc"))
                elif -1 < rt.chd[0].v < 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 29))

            # Constant folding.
            # Arccosecant function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   2. If x is +-inf, the result is 0.
            #   3. If x is in (-1, 1), the result is nan.
            #   4. If x is finite which is not in (-1, 1), the result is ``math.asin(1 / x)``.
            # Here, the rule 4 is based on identity ``acsc(x) = asin(1 / x)``.
            # For detail and more identities, consult the reference below.
            # The following logic is an implementation of these rules.
            #
            # **Reference**
            #   * https://en.wikipedia.org/wiki/Inverse_trigonometric_functions
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v):
                    rt.chd[0].v = 0
                elif -1 < rt.chd[0].v < 1:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.asin(1 / rt.chd[0].v)

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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Asec"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Asec"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Asec"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Asec"))
                elif -1 < rt.chd[0].v < 1:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 30))

            # Constant folding.
            # Arccosecant function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   2. If x is +-inf, the result is pi/2.
            #   3. If x is in (-1, 1), the result is nan.
            #   4. If x is finite which is not in (-1, 1), the result is ``math.acos(1 / x)``.
            # Here, the rule 4 is based on identity ``asec(x) = acos(1 / x)``.
            # For detail and more identities, consult the reference below.
            # The following logic is an implementation of these rules.
            #
            # **Reference**
            #   * https://en.wikipedia.org/wiki/Inverse_trigonometric_functions
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v):
                    rt.chd[0].v = math.pi / 2
                elif -1 < rt.chd[0].v < 1:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.acos(1 / rt.chd[0].v)

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
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Acot"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Acot"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Acot"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Acot"))

            # Constant folding.
            # Arccotagent function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   2. If x is +-inf, the result is 0.
            #   3. If x is finite negative, the result is ``-(math.pi / 2 + math.atan(x))``.
            #   4. If x is nonnegative, the result is ``math.pi / 2 - math.atan(x)``.
            # Here, the rule 3 and 4 are based on identity ``acot(x) = -pi / 2 - atan(x)`` for negative x and
            # ``acot(x) = pi / 2 - atan(x)`` for nonnegative x.
            # For detail and more identities, consult the reference below.
            # The following logic is an implementation of these rules.
            #
            # **Reference**
            #   * https://en.wikipedia.org/wiki/Inverse_trigonometric_functions
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isinf(rt.chd[0].v):
                    rt.chd[0].v = 0
                elif rt.chd[0].v < 0:
                    rt.chd[0].v = -(math.pi / 2 + math.atan(rt.chd[0].v))
                else:
                    rt.chd[0].v = math.pi / 2 - math.atan(rt.chd[0].v)

                return rt.chd[0], warn

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
        elif fun == Type.FunT.CSC:
            return list(map(lambda x: Decimal(1 / math.sin(float(x))), test_in))
        elif fun == Type.FunT.SEC:
            return list(map(lambda x: Decimal(1 / math.cos(float(x))), test_in))
        elif fun == Type.FunT.COT:
            return list(map(lambda x: Decimal(1 / math.tan(float(x))), test_in))
        elif fun == Type.FunT.ASIN:
            return list(map(lambda x: Decimal(math.asin(float(x))), test_in))
        elif fun == Type.FunT.ACOS:
            return list(map(lambda x: Decimal(math.acos(float(x))), test_in))
        elif fun == Type.FunT.ATAN:
            return list(map(lambda x: Decimal(math.atan(float(x))), test_in))
        elif fun == Type.FunT.ACSC:
            return list(map(lambda x: Decimal(math.asin(1 / float(x))), test_in))
        elif fun == Type.FunT.ASEC:
            return list(map(lambda x: Decimal(math.acos(1 / float(x))), test_in))
        else:
            return list(map(lambda x: Decimal(
                -(math.pi / 2 + math.atan(float(x))) if x < 0 else Decimal(math.pi / 2 - math.atan(float(x)))),
                            test_in))
