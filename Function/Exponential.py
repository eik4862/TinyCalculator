from typing import final

from Function import Function


class ExpFun(Function.Fun):
    """
    Exponential and logarithm function toolbox.

    :cvar __sign: Signatures of exponential and logarithm functions.
    """

    def __new__(cls) -> None:
        raise NotImplementedError

    # @classmethod
    # def __exp(cls, x: float) -> float:
    #     """
    #     Exponential function.
    #
    #     Exponential function with parameter x has following computation rules.
    #         1. If x is nan, the result is nan.
    #         2. If x if -inf, the result is 0.
    #         3. If x is +inf, the result is +inf.
    #         4. If x is finite, the result is ``math.exp(x)``.
    #
    #     This method is private and called internally as a helper of ``Exp.simplify``.
    #     For detailed description for simplification, refer to the comments of ``Exp.simplify``.
    #
    #     :param x: Point where exponential function is to be computed.
    #     :type x: float
    #
    #     :return: Computed value of exponential function.
    #     :rtype: float
    #     """
    #     try:
    #         return math.exp(x)
    #     except OverflowError:
    #         return math.inf
    #
    # @classmethod
    # def __log(cls, x: float, y: float = None) -> float:
    #     """
    #     Log function.
    #
    #     Log function with exponent x has following computation rules.
    #         1. If x is nan or -inf, the result is nan.
    #         2. If x is +inf, the result is +inf.
    #         3. If x is finite negative, the result if nan.
    #         4. If x is 0, the result is -inf.
    #         5. If x is finite positive, the result is ``math.log2(x)``.
    #
    #     Log function with exponent x and base y has following computation rules.
    #         1. If x or y is nan or -inf, the result is nan.
    #         2. If x or y is finite negative, the result is nan.
    #         3. If y is 1, the result is nan.
    #         4. If x and y is inf, the result is nan.
    #         5. If x is inf and y is 0, the result is nan.
    #         6. If x is inf and y is finite which is in (0, 1), the result is -inf.
    #         7. If x is inf and y is finite which is greater than 1, the result is inf.
    #         8. If x is 0 and y is inf, the result is nan.
    #         9. If x is finite positive and y is inf, the result is 0.
    #         10. If x and y is 0, the result is nan.
    #         11. If x is 0 and y is finite which is in (0, 1), the result is inf.
    #         12. If x is 0 and y is finite which is greater than 1, the result is -inf.
    #         13. If x is finite positive and y is 0, the result is 0.
    #         14. If x is finite positive and y is finite positive which is not 1, the result is ``math.log(x, y)``.
    #
    #     This method is private and called internally as a helper of ``Exp.simplify``.
    #     For detailed description for simplification, refer to the comments of ``Exp.simplify``.
    #
    #     :param x: Exponent where log function is to be computed.
    #     :type x: float
    #     :param y: Base where log function is to be computed.
    #     :type y: float
    #
    #     :return: Computed value of log function.
    #     :rtype: float
    #     """
    #     if y is None:
    #         return math.nan if x < 0 else -math.inf if x == 0 else math.log(x)
    #     else:
    #         if math.isnan(x + y) or x < 0 or y < 0 or y == 1:
    #             return math.nan
    #         elif y == 0 or math.isinf(y):
    #             return math.nan if x == 0 or math.isinf(x) else 0
    #         else:
    #             return math.inf if x == 0 and y < 1 else -math.inf if x == 0 and y > 1 else math.log(x, y)
    #
    # @classmethod
    # def __pow(cls, x: float, y: float) -> float:
    #     """
    #     Power function.
    #
    #     Power function with base x and exponent y has following computation rules.
    #         1. If x or y is nan, the result is nan.
    #         2. If x is +-inf and y is -inf, the result is 0.
    #         3. If x and y is inf, the result is inf.
    #         4. If x is -inf and y is inf, the result is nan.
    #         5. If x is inf and y is 0, the result is nan.
    #         6. If x is inf and y is finite positive, the result is inf.
    #         7. If x is inf and y is finite negative, the result is 0.
    #         8. If x is -inf and y is 0 or finite noninteger, the result is nan.
    #         9. If x is -inf and y is finite negative integer, the result is 0.
    #         10. If x is -inf and y is finite even positive integer, the result is inf.
    #         11. If x is -inf and y is finite odd positive integer, the result is -inf.
    #         12. If x is 1 or y is 0, the result is 1.
    #         13. If x is finite which is in [-1, 0] and y is -inf, the result is nan.
    #         14. If x is finite which is in (0, 1) and y is -inf, the result is inf.
    #         15. If x is finite which is not in [-1, 1] and y is -inf, the result is 0.
    #         16. If x is finite which is less than or equal to -1 and y is inf, the result is nan.
    #         17. If x is finite which is in (-1, 1) and y is inf, the result is 0.
    #         18. If x is finite which is in greater than 1 and y is inf, the result is inf.
    #         19. If x is finite negative and y is finite noninteger, the result is nan.
    #         20. If x is finite positive and y is finite, the result is ``math.pow(x, y)``.
    #         21. If x is finite negative and y is finite integer, the result is ``math.pow(x, y)``.
    #
    #     This method is private and called internally as a helper of ``Exp.simplify``.
    #     For detailed description for simplification, refer to the comments of ``Exp.simplify``.
    #
    #     :param x: Base where power function is to be computed.
    #     :type x: float
    #     :param y: Exponent where power function is to be computed.
    #     :type y: float
    #
    #     :return: Computed value of power function.
    #     :rtype: float
    #     """
    #     if math.isnan(x + y) or (x < 0 and not is_int(y)):
    #         return math.nan
    #     elif (x <= -1 and y == math.inf) or (-1 <= x <= 0 and y == -math.inf) or (x == 0 and y < 0):
    #         return math.nan
    #     elif y == 0:
    #         return math.nan if math.isinf(x) else 1
    #     else:
    #         try:
    #             return math.pow(x, y)
    #         except OverflowError:
    #             return -math.inf if x < 0 and y % 2 == 1 else math.inf
    #
    # @classmethod
    # def __sqrt(cls, x: float) -> float:
    #     """
    #     Square root function.
    #
    #     Square root function with parameter x has following computation rules.
    #         1. If x is nan or -inf, the result is nan.
    #         2. If x is +inf, the result is +inf.
    #         3. If x is finite negative, the result if nan.
    #         4. If x is finite nonnegative, the result is ``math.sqrt(x)``.
    #
    #     This method is private and called internally as a helper of ``Exp.simplify``.
    #     For detailed description for simplification, refer to the comments of ``Exp.simplify``.
    #
    #     :param x: Point where square root function is to be computed.
    #     :type x: float
    #
    #     :return: Computed value of square root function.
    #     :rtype: float
    #     """
    #     return math.nan if x < 0 else math.sqrt(x)
    #
    # @classmethod
    # def __log2(cls, x: float) -> float:
    #     """
    #     Log function with base 2.
    #
    #     Log function with base 2 with parameter x has following computation rules.
    #         1. If x is nan or -inf, the result is nan.
    #         2. If x is +inf, the result is +inf.
    #         3. If x is finite negative, the result if nan.
    #         4. If x is 0, the result is -inf.
    #         5. If x is finite positive, the result is ``math.log2(x)``.
    #
    #     This method is private and called internally as a helper of ``Exp.simplify``.
    #     For detailed description for simplification, refer to the comments of ``Exp.simplify``.
    #
    #     :param x: Point where log function with base 2 is to be computed.
    #     :type x: float
    #
    #     :return: Computed value of log function with base 2.
    #     :rtype: float
    #     """
    #     return math.nan if x < 0 else -math.inf if x == 0 else math.log2(x)
    #
    # @classmethod
    # def __log10(cls, x: float) -> float:
    #     """
    #     Log function with base 10.
    #
    #     Log function with base 10 with parameter x has following computation rules.
    #         1. If x is nan or -inf, the result is nan.
    #         2. If x is +inf, the result is +inf.
    #         3. If x is finite negative, the result if nan.
    #         4. If x is 0, the result is -inf.
    #         5. If x is finite positive, the result is ``math.log10(x)``.
    #
    #     This method is private and called internally as a helper of ``Exp.simplify``.
    #     For detailed description for simplification, refer to the comments of ``Exp.simplify``.
    #
    #     :param x: Point where log function with base 10 is to be computed.
    #     :type x: float
    #
    #     :return: Computed value of log function with base 10.
    #     :rtype: float
    #     """
    #     return math.nan if x < 0 else -math.inf if x == 0 else math.log10(x)
    #
    # @classmethod
    # def chk_t(cls, rt: Token.Fun) -> Optional[List[Type.Sign]]:
    #     """
    #     Type checker for exponential and logarithm functions.
    #     It checks type of input function token and assigns return type as type information of the token.
    #
    #     :param rt: Token to be type checked.
    #     :type rt: Token.Fun
    #
    #     :return: None if type check is successful. Candidate signatures if not.
    #     :rtype: Optional[List[Type.Signature]]
    #     """
    #     cand: List[Type.Sign] = cls.__sign.get(rt.v)  # Candidate signatures
    #     infer: Type.Sign = Type.Sign([tok.t for tok in rt.chd], Type.T.REAL, rt.v)  # Inferred signature
    #
    #     # Inferred signature must be one of candidates and return type is NUM type.
    #     if infer in cand:
    #         rt.t = Type.T.REAL
    #
    #         return None
    #     else:
    #         return cand
    #
    # @classmethod
    # def simplify(cls, rt: Token.Fun) -> Tuple[Token.Tok, List[Warning.InterpWarn]]:
    #     """
    #     Simplifier for exponential and logarithm functions.
    #
    #     It does following simplifications.
    #         1. Constant folding.
    #         2. Dead expression stripping.
    #         3. Sign propagation.
    #     For details and detailed explanation of these optimization tricks, refer to the comments of
    #     ``Operator.simplify`` and references therein.
    #
    #     :param rt: Root of AST to be simplified.
    #     :type rt: Token.Fun
    #
    #     :return: Root of simplified AST and list of generated warnings.
    #     :rtype: Tuple[Token.Tok, List[Warning.InterpWarn]]
    #
    #     :raise NAN_DETECT: If nan is detected as a given parameter.
    #     :raise IFN_DETECT: If inf is detected as a given parameter.
    #     :raise DOMAIN_OUT: If given parameter is not in domain.
    #     :raise POLE_DETECT: If mathematical pole is detected.
    #     :raise BIG_INT: If given parameter exceeds floating point max.
    #     :raise SMALL_INT: If given parameter exceeds floating point min.
    #     """
    #     warn: List[Warning.InterpWarn] = []  # List of generated warnings.
    #
    #     if rt.v == Type.FunT.Exp:
    #         # Check for warnings.
    #         # Exponential function with parameter x generates warning for followings cases.
    #         #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   2. x is nan. (NAN_DETECT)
    #         #   3. x is +-inf. (INF_DETECT)
    #         # The following logic is an implementation of these rules.
    #         if rt.chd[0].tok_t == Type.TokT.NUM:
    #             if is_bigint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Exp"))
    #                 rt.chd[0].v = math.inf
    #             elif is_smallint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Exp"))
    #                 rt.chd[0].v = -math.inf
    #             elif math.isnan(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Exp"))
    #             elif math.isinf(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Exp"))
    #
    #         # Constant folding.
    #         # For detailed computation rule, refer to the comment in ``Exp.__exp``.
    #         if rt.chd[0].tok_t == Type.TokT.NUM:
    #             rt.chd[0].v = cls.__exp(rt.chd[0].v)
    #
    #             return rt.chd[0], warn
    #
    #         return rt, warn
    #     elif rt.v == Type.FunT.Log:
    #         # Check for warnings.
    #         # Log function with parameter x generates warning for followings cases.
    #         #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   2. x is nan. (NAN_DETECT)
    #         #   3. x is +-inf. (INF_DETECT)
    #         #   2. x is 0. (POLE_DETECT)
    #         #   3. x is finite negative. (DOMAIN_OUT)
    #         # Log function with parameter x and y generates warning for following cases.
    #         #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   2. x is nan. (NAN_DETECT)
    #         #   3. x is +-inf. (INF_DETECT)
    #         #   4. y exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   5. y is nan. (NAN_DETECT)
    #         #   6. y is +-inf. (INF_DETECT)
    #         #   7. x and y are finite but at least one of them is negative. (DOMAIN_OUT)
    #         #   8. x is 0 and y is finite nonnegative. (POLE_DETECT)
    #         #   9. x is finite positive and y is 0 or 1. (POLE_DETECT)
    #         # The following logic is an implementation of these rules.
    #         if rt.argc == 1:
    #             if rt.chd[0].tok_t == Type.TokT.NUM:
    #                 if is_bigint(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Log"))
    #                     rt.chd[0].v = math.inf
    #                 elif is_smallint(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Log"))
    #                     rt.chd[0].v = -math.inf
    #                 elif math.isnan(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Log"))
    #                 elif math.isinf(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Log"))
    #                 elif rt.chd[0].v == 0:
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 48))
    #                 elif rt.chd[0].v < 0:
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 49))
    #             elif rt.chd[0].tok_t == rt.chd[0].tok_t == Type.TokT.NUM:
    #                 if is_bigint(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Log"))
    #                     rt.chd[0].v = math.inf
    #                 elif is_smallint(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Log"))
    #                     rt.chd[0].v = -math.inf
    #                 elif math.isnan(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Log"))
    #                 elif math.isinf(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Log"))
    #
    #                 if is_bigint(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=2, handle="Log"))
    #                     rt.chd[0].v = math.inf
    #                 elif is_smallint(rt.chd[0].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=2, handle="Log"))
    #                     rt.chd[0].v = -math.inf
    #                 elif math.isnan(rt.chd[1].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=2, handle="Log"))
    #                 elif math.isinf(rt.chd[1].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=2, handle="Log"))
    #
    #                 if math.isfinite(rt.chd[0].v + rt.chd[1].v):
    #                     if rt.chd[0].v < 0 or rt.chd[0].v < 0:
    #                         warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 50))
    #                     elif rt.chd[0].v == 0:
    #                         warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 48))
    #                     elif rt.chd[1].v in [0, 1]:
    #                         warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 51))
    #
    #         # Constant folding.
    #         # For detailed computation rule, refer to the comment in ``Exp.__log``.
    #         if rt.argc == 1:
    #             if rt.chd[0].tok_t == Type.TokT.NUM:
    #                 rt.chd[0].v = cls.__log(rt.chd[0].v)
    #
    #                 return rt.chd[0], warn
    #         else:
    #             if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
    #                 rt.chd[0].v = cls.__log(rt.chd[0].v, rt.chd[1].v)
    #
    #                 return rt.chd[0], warn
    #
    #         # Dead expr stripping.
    #         # For dead expr stripping, it uses following rules.
    #         #   1. Log[nan, y] = nan
    #         #   2. Log[-inf, y] = nan
    #         #   3. Log[z, y] = nan
    #         #   4. Log[x, nan] = nan
    #         #   5. Log[x, -inf] = nan
    #         #   6. Log[x, z] = nan
    #         # where z is finite negative.
    #         # The following logic is an implementation of these rules.
    #         if rt.chd[0].tok_t == Type.TokT.NUM and not is_bigint(rt.chd[0].v):
    #             if rt.chd[0].v < 0 or math.isnan(rt.chd[0].v):
    #                 rt.chd[0].v = math.nan
    #
    #                 return rt.chd[0], warn
    #         elif rt.chd[1].tok_t == Type.TokT.NUM and not is_bigint(rt.chd[1].v):
    #             if rt.chd[1].v < 0 or math.isnan(rt.chd[1].v):
    #                 rt.chd[1].v = math.nan
    #
    #                 return rt.chd[1], warn
    #
    #         return rt, warn
    #     elif rt.v == Type.FunT.Pow:
    #         # Check for warnings.
    #         # Power function with parameter x and y generates warning for following cases.
    #         #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   2. x is nan. (NAN_DETECT)
    #         #   3. x is +-inf. (INF_DETECT)
    #         #   4. y exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   5. y is nan. (NAN_DETECT)
    #         #   6. y is +-inf. (INF_DETECT)
    #         #   7. x is finite negative and y is finite noninteger. (DOMAIN_OUT)
    #         #   8. x is 0 and y is finite nonpositive. (POLE_DETECT)
    #         # The following logic is an implementation of these rules.
    #         if rt.chd[0].tok_t == rt.chd[0].tok_t == Type.TokT.NUM:
    #             if is_bigint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Pow"))
    #                 rt.chd[0].v = math.inf
    #             elif is_smallint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Pow"))
    #                 rt.chd[0].v = -math.inf
    #             elif math.isnan(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Pow"))
    #             elif math.isinf(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Pow"))
    #
    #             if is_bigint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=2, handle="Pow"))
    #                 rt.chd[0].v = math.inf
    #             elif is_smallint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=2, handle="Pow"))
    #                 rt.chd[0].v = -math.inf
    #             elif math.isnan(rt.chd[1].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=2, handle="Pow"))
    #             elif math.isinf(rt.chd[1].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=2, handle="Pow"))
    #
    #             if math.isfinite(rt.chd[0].v + rt.chd[1].v):
    #                 if rt.chd[0].v < 0 or not is_int(rt.chd[1].v):
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 52))
    #                 elif rt.chd[0].v == 0 and rt.chd[1].v <= 0:
    #                     warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 53))
    #
    #         # Constant folding.
    #         # For detailed computation rule, refer to the comment in ``Exp.__pow``.
    #         if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
    #             rt.chd[0].v = cls.__pow(rt.chd[0].v, rt.chd[1].v)
    #
    #             return rt.chd[0], warn
    #
    #         # Dead expr stripping.
    #         # For dead expr stripping, it uses following rules.
    #         #   1. Pow[nan, y] = nan
    #         #   2. Pow[x, nan] = nan
    #         #   3. Pow[-x, n] = Pow[x, n]
    #         # where n is finite even integer.
    #         # The following logic is an implementation of these rules.
    #         if rt.chd[0].tok_t == Type.TokT.NUM and not (is_bigint(rt.chd[0].v) or is_smallint(rt.chd[1].v)):
    #             if math.isnan(rt.chd[0].v):
    #                 return rt.chd[0], warn
    #         elif rt.chd[1].tok_t == Type.TokT.NUM and not (is_bigint(rt.chd[1].v) or is_smallint(rt.chd[1].v)):
    #             if math.isnan(rt.chd[1].v):
    #                 return rt.chd[1], warn
    #             if rt.chd[1].v % 2 == 0 and rt.chd[0].v == Type.OpT.MINUS:
    #                 rt.swap_chd(rt.chd[0].chd[0], 0)
    #
    #                 return rt, warn
    #
    #         # Sign propagation.
    #         # For sign propagation, it uses following rule.
    #         #   1. Pow[-x, n] = -Pow[x, n]
    #         # where n is finite odd integer.
    #         # The following logic is an implementation of this rule.
    #         if rt.chd[1].tok_t == Type.TokT.NUM and not (is_bigint(rt.chd[1].v) or is_smallint(rt.chd[1].v)):
    #             if rt.chd[0].v == Type.OpT.MINUS and rt.chd[1].v % 2 == 1:
    #                 tmp = rt.chd[0]
    #                 rt.swap_chd(rt.chd[0].chd[0], 0)
    #                 tmp.swap_chd(rt, 0)
    #
    #                 return tmp, warn
    #
    #         return rt, warn
    #     elif rt.v == Type.FunT.Sqrt:
    #         # Check for warnings.
    #         # Square root function with parameter x generates warning for followings cases.
    #         #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   2. x is nan. (NAN_DETECT)
    #         #   3. x is +-inf. (INF_DETECT)
    #         #   4. x is finite negative. (DOMAIN_OUT)
    #         # The following logic is an implementation of these rules.
    #         if rt.chd[0].tok_t == Type.TokT.NUM:
    #             if is_bigint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Sqrt"))
    #                 rt.chd[0].v = math.inf
    #             elif is_smallint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Sqrt"))
    #                 rt.chd[0].v = -math.inf
    #             elif math.isnan(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Sqrt"))
    #             elif math.isinf(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Sqrt"))
    #             elif rt.chd[0].v < 0:
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 25))
    #
    #         # Constant folding.
    #         # For detailed computation rule, refer to the comment in ``Exp.__sqrt``.
    #         if rt.chd[0].tok_t == Type.TokT.NUM:
    #             rt.chd[0].v = cls.__sqrt(rt.chd[0].v)
    #
    #             return rt.chd[0], warn
    #
    #         return rt, warn
    #     elif rt.v == Type.FunT.Log2:
    #         # Check for warnings.
    #         # Log function with base 2 and parameter x generates warning for followings cases.
    #         #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   2. x is nan. (NAN_DETECT)
    #         #   3. x is +-inf. (INF_DETECT)
    #         #   4. x is 0. (POLE_DETECT)
    #         #   5. x is finite negative. (DOMAIN_OUT)
    #         # The following logic is an implementation of these rules.
    #         if rt.chd[0].tok_t == Type.TokT.NUM:
    #             if is_bigint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Log2"))
    #                 rt.chd[0].v = math.inf
    #             elif is_smallint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Log2"))
    #                 rt.chd[0].v = -math.inf
    #             elif math.isnan(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Log2"))
    #             elif math.isinf(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Log2"))
    #             elif rt.chd[0].v == 0:
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 54))
    #             elif rt.chd[0].v < 0:
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 55))
    #
    #         # Constant folding.
    #         # For detailed computation rule, refer to the comment in ``Exp.__log2``.
    #         if rt.chd[0].tok_t == Type.TokT.NUM:
    #             rt.chd[0].v = cls.__log2(rt.chd[0].v)
    #
    #             return rt.chd[0], warn
    #
    #         return rt, warn
    #     else:
    #         # Check for warnings.
    #         # Log function with base 10 and parameter x generates warning for followings cases.
    #         #   1. x exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
    #         #   2. x is nan. (NAN_DETECT)
    #         #   3. x is +-inf. (INF_DETECT)
    #         #   4. x is 0. (POLE_DETECT)
    #         #   5. x is finite negative. (DOMAIN_OUT)
    #         # The following logic is an implementation of these rules.
    #         if rt.chd[0].tok_t == Type.TokT.NUM:
    #             if is_bigint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 15, arg_pos=1, handle="Log10"))
    #                 rt.chd[0].v = math.inf
    #             elif is_smallint(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 16, arg_pos=1, handle="Log10"))
    #                 rt.chd[0].v = -math.inf
    #             elif math.isnan(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 1, arg_pos=1, handle="Log10"))
    #             elif math.isinf(rt.chd[0].v):
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 2, arg_pos=1, handle="Log10"))
    #             elif rt.chd[0].v == 0:
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 56))
    #             elif rt.chd[0].v < 0:
    #                 warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 57))
    #
    #         # Constant folding.
    #         # For detailed computation rule, refer to the comment in ``Exp.__log10``.
    #         if rt.chd[0].tok_t == Type.TokT.NUM:
    #             rt.chd[0].v = cls.__log10(rt.chd[0].v)
    #
    #             return rt.chd[0], warn
    #
    #         return rt, warn
    #
    # @classmethod
    # def test(cls, fun: Type.FunT, test_in: List[List[Decimal]]) -> List[Decimal]:
    #     """
    #     Test function for exponential and logarithm function.
    #
    #     It just call corresponding target function anc evaluate it at test input points.
    #
    #     :param fun: Function to be tested.
    #     :type fun: Type.FunT
    #     :param test_in: Test input.
    #     :type test_in: List[List[Decimal]]
    #
    #     :return: Test output.
    #     :rtype: List[Decimal]
    #     """
    #     if fun == Type.FunT.Exp:
    #         return list(map(lambda x: Decimal(cls.__exp(*list(map(float, x)))), test_in))
    #     elif fun == Type.FunT.Log:
    #         return list(map(lambda x: Decimal(cls.__log(*list(map(float, x)))), test_in))
    #     elif fun == Type.FunT.Pow:
    #         return list(map(lambda x: Decimal(cls.__pow(*list(map(float, x)))), test_in))
    #     elif fun == Type.FunT.Sqrt:
    #         return list(map(lambda x: Decimal(cls.__sqrt(*list(map(float, x)))), test_in))
    #     elif fun == Type.FunT.Log2:
    #         return list(map(lambda x: Decimal(cls.__log2(*list(map(float, x)))), test_in))
    #     else:
    #         return list(map(lambda x: Decimal(cls.__log10(*list(map(float, x)))), test_in))


@final
class Log(ExpFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Log2(ExpFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Log10(ExpFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Power(ExpFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Exp(ExpFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Sqrt(ExpFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class CubeRoot(ExpFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Surd(ExpFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
