import math
from decimal import Decimal
from typing import Dict, List, Tuple, Optional, final

from Core import Type, Token, Warning
from Util.Macro import is_bigint, is_smallint


@final
class Exp:
    """
    Exponential and logarithm function toolbox.

    :cvar __sign: Signatures of exponential and logarithm functions.
    """
    __sign: Dict[Type.FunT, List[Type.Sign]] = {
        Type.FunT.EXP: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.EXP)],
        Type.FunT.LOG: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.LOG),
                        Type.Sign([Type.T.NUM, Type.T.NUM], Type.T.NUM, Type.FunT.LOG)],
        Type.FunT.SQRT: [Type.Sign([Type.T.NUM], Type.T.NUM, Type.FunT.SQRT)]
    }

    def __init__(self) -> None:
        raise NotImplementedError

    def __del__(self) -> None:
        raise NotImplementedError

    @classmethod
    def chk_t(cls, rt: Token.FunTok) -> Optional[List[Type.Sign]]:
        """
        Type checker for exponential and logarithm functions.
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
        Simplifier for exponential and logarithm functions.

        It does following simplifications.
            1. Constant folding.
            2. Dead expression stripping.
            3. Function coalescing.
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

        if rt.v == Type.FunT.EXP:
            # Check for warnings.
            # Exponential function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Exp"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Exp"))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Exp"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Exp"))

            # Constant folding.
            # Exponential function with parameter x has following rules.
            #   1. If x is nan, the result is nan.
            #   2. If x is +-inf, the result is +inf and 0, resp.
            #   4. If x is finite, the result is ``math.exp(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                try:
                    rt.chd[0].v = math.exp(rt.chd[0].v)
                except OverflowError:
                    rt.chd[0].v = math.inf

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.FunT.SQRT:
            # Check for warnings.
            # Square root function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max size. (BIG_INT)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite negative. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Sqrt"))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 25))
                    rt.chd[0].v = -1
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Sqrt"))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Sqrt"))
                elif rt.chd[0].v <= 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 25))

            # Constant folding.
            # Square root function with parameter x has following rules.
            #   1. If x is nan or -inf, the result is nan.
            #   2. If x is +inf, the result is +inf.
            #   3. If x is finite negative, the result if nan.
            #   4. If x is finite nonnegative, the result is ``math.sqrt(x)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if rt.chd[0].v < 0:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = math.sqrt(rt.chd[0].v)

                return rt.chd[0], warn

            return rt, warn
        else:
            # Check for warnings.
            # Log function with parameter x generates warning for followings cases.
            #   1. x exceeds floating point max size. (BIG_INT)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is +-inf. (INF_DETECT)
            #   4. x is finite negative. (DOMAIN_OUT)
            #   5. x is 0. (POLE_DETECT)
            # Log function with parameter x and y generates warning for following cases.
            #   1. x or y exceeds floating point max size. (BIG_INT)
            #   2. x or y is nan. (NAN_DETECT)
            #   3. x or y is +-inf. (INT_DETECT)
            #   4. x is finite negative. (DOMAIN_OUT)
            #   5. x is 0. (POLE_DETECT)
            #   6. y is finite negative. (DOMAIN_OUT)
            #   7. y is 1. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.argc == 1:
                if rt.chd[0].tok_t == Type.TokT.NUM:
                    if is_bigint(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Log"))
                        rt.chd[0].v = math.inf
                    elif is_smallint(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 16, arg_pos=1, handle="Log"))
                        rt.chd[0].v = -1
                    elif math.isnan(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Log"))
                    elif math.isinf(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Log"))
                    elif rt.chd[0].v < 0:
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 2))
            else:
                if rt.chd[0].tok_t == Type.TokT.NUM:
                    if is_bigint(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Log"))
                        rt.chd[0].v = math.inf
                    elif is_smallint(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 16, arg_pos=1, handle="Log"))
                        rt.chd[0].v = -1
                    elif math.isnan(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Log"))
                    elif math.isinf(rt.chd[0].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Log"))

                if rt.chd[0].tok_t == Type.TokT.NUM:
                    if is_bigint(rt.chd[1].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=2, handle="Log"))
                        rt.chk[1].v = math.inf
                    elif is_smallint(rt.chd[1].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 16, arg_pos=2, handle="Log"))
                        rt.chd[0].v = -1
                    elif math.isnan(rt.chd[1].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=2, handle="Log"))
                    elif math.isinf(rt.chd[1].v):
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=2, handle="Log"))

            # TODO: complete this logic
            # Constant folding.
            # Log function with parameter x has following rules.
            #   1. If x is nan or -inf, the result is nan.
            #   2. If x is +inf, the result is +inf.
            #   3. If x is finite negative, the result is nan.
            #   4. IF x is 0, the result is -inf.
            #   5. If x is finite positive, the result is ``math.log(x)``.
            # Log function with parameter x and y has following rules.
            #   1. If any of x or y is nan or -inf, the result is nan.
            #   2. If any of x or y is finite negative, the result is nan.
            #   3. If x and y are both +inf, the result is nan.
            #   4. If y is 0 or 1, the result is nan.
            #   5. If x is +inf and y is finite positive less than 1, the result is -inf.
            #   6. If x is +inf and y is finite positive greater than 1, the result is +inf.
            #   7. If x is finite positive and y is +inf, the result is 0.
            #   8. If x is 0 and y is +inf, the result is nan.
            #   9. If x is 0 and y is finite positive less than 1, the result is +inf.
            #   10. If x is 0 and y is finite positive greater than 1, the result is -inf.
            #   11. If x is finite positive and y is finite positive which is not 1, the result is ``math.log(x, y)``.
            # The following logic is an implementation of these rules.
            if rt.argc == 1:
                if rt.chd[0].tok_t == Type.TokT.NUM:
                    if rt.chd[0].v < 0:
                        rt.chd[0].v = math.nan
                    elif rt.chd[0].v == 0:
                        rt.chd[0].v = -math.inf
                    else:
                        rt.chd[0].v = math.log(rt.chd[0].v)

                return rt.chd[0], warn
            elif rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
                if rt.chd[0].v < 0 or rt.chd[1].v <= 0 or rt.chd[1].v == 1:
                    rt.chd[0].v = math.nan
                elif rt.chd[0].v == 0:
                    if rt.chd[1].v > 1:
                        rt.chd[0].v = math.inf
                    elif rt.chd[1].v < 1:
                        rt.chd[0].v = -math.inf
                else:
                    rt.chd[0].v = math.log(rt.chd[0].v, rt.chd[1].v)

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

    @classmethod
    def test(cls, fun: Type.FunT, test_in: List[Decimal]) -> List[Decimal]:
        """
        Test function for exponential and logarithm function.

        It just call corresponding target function anc evaluate it at test input points.

        :param fun: Function to be tested.
        :type fun: Type.FunT
        :param test_in: Test input.
        :type test_in: List[Decimal]

        :return: Test output.
        :rtype: List[Decimal]
        """
        if fun == Type.FunT.EXP:
            return list(map(lambda x: Decimal(math.exp(float(x))), test_in))
        elif fun == Type.FunT.SQRT:
            return list(map(lambda x: Decimal(math.sqrt(float(x))), test_in))
        else:
            return list(map(lambda x: Decimal(math.log(float(x))), test_in))
