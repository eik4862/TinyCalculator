import math
from typing import final, List, Tuple, Optional

from Core import Type, Token, Warning

from Util.Macro import is_bigint, is_smallint


@final
class Op:
    """
    Operator toolbox.

    Precedence and association rules.
        1. Precedence basically inherits that of C.
           ADD/SUB < MUL/DIV/REM < POW < PLUS/MINUS < FACT.
        2. Association rule also inherits that of C.
           ADD/SUB/MUL/DIV/REM: Left to right.
           POW/FACT/PLUS/MINUS: Right to left.

    :cvar __idx_l: Temporary index list for simplification.
    """
    __idx_l: List[int] = []

    def __init__(self) -> None:
        raise NotImplementedError

    def __del__(self) -> None:
        raise NotImplementedError

    @classmethod
    def chk_t(cls, rt: Token.OpTok) -> Optional[Token.Tok]:
        """
        Type checker for operators.
        It checks type of input operator token and assigns return type as type information of the token.

        :param rt: Token to be type checked.
        :type rt: Token.OpTok

        :return: None if type check is successful. Erroneous operand token if not.
        :rtype: Optional[Token.Tok]
        """
        # All children must be NUM type and the result type is also NUM type.
        for tok in rt.chd:
            if tok.t != Type.T.NUM:
                return tok

        rt.t = Type.T.NUM

        return None

    @classmethod
    def simplify(cls, rt: Token.OpTok, prn: Token.Tok) -> Tuple[Token.Tok, List[Warning.InterpWarn]]:
        """
        Simplifier for operators.
        
        It does following simplifications.
            1. Constant folding.
               Expressions like ``2 + 3`` or ``2 * 3`` can be reduced to ``5`` or ``6``, resp
               Thus complex expression may be folded into simple one NUM token.
            2. Sign propagation.
               In expression like ``(-x) * y`` or ``(-x) / y``, the minus sign can be propagated to outside as
               ``-(x * y)`` or ``-(x / y)``, resp.
               Although the # of operation does not reduce, minus sign can be disappear later by dead expression
               stripping.
            3. Dead expression stripping.
               In expression like ``x * 1`` or ``-(-x)``, multiplication by 1 or two contiguous minus sign is useless.
               Thus both can be reduced to ``x`` which is much simpler.
               Note that this with sign propagation can eliminate many sign inversions.
            4. Hoisting.
               Originally generated AST is binary tree.
               But from the associativity of ADD and MUL and equivalence relation of operators, ``x / y = x * (y^-1)``
               and ``x - y = x + (-y)``, it can be reformed to general tree with multiple children, reducing the height
               of tree.
            5. Packing.
               In expression like ``x + -y + -z`` or ``x * (y^-1) * (z^-1)``, if can be packed to ``x + -(y + z)`` or
               ``x * (y * z)^-1``, reducing the # of operations.
               From hoisting and unpacking, sign inversion and power of -1 may be frequently appear in an expression.
               But this packing optimization can reduce those.
            6. Unpacking.
               In expression like ``-(x + y)`` or ``-(x * y)``, it can be rewritten as ``(-x) + (-y)`` or
               ``x * y * -1``.
               At first glance, this might seem making expression more complex, not simplifying it.
               But with hoisting and sign propagation, this can be make the expression much simpler later.
               Also, packing will unwind this later, even if hoisting and sign propagation does not simplify these
               unwound minus signs.
        Most of these simplification tricks are originally part of compiler optimization and programing language scheme.
        For details, consult following references.

        **Reference**
            * https://en.wikipedia.org/wiki/Constant_folding
            * https://en.wikipedia.org/wiki/Dead_code_elimination
            * https://developer.mozilla.org/ko/docs/Glossary/Hoisting

        :param rt: Root of partial AST to be simplified.
        :type rt: Token.OpTok
        :param prn: Parent of root to be simplified.
        :type prn: Token.Tok

        :return: Root of simplified partial AST and list of generated warnings.
        :rtype: Tuple[Token.Tok, List[Warning.InterpWarn]]

        :raise NAN_DETECT: If nan is detected as one of operand.
        :raise INF_DETECT: If inf is detected as one of operand.
        :raise DOMAIN_OUT: If given operand is not in domain.
        :raise POLE_DETECT: If mathematical pole is detected.
        :raise BIG_INT: If given operand exceeds floating point max.
        :raise SMALL_INT: If given operand exceeds floating point min.
        """
        sgn: bool = False  # Flag for sign propagation. True means there is sign propagation.
        tmp: Token.Tok = None  # Temporary variable holding token.
        warn: List[Warning.InterpWarn] = []  # List of generated warnings.

        if rt.v == Type.OpT.ADD:
            # Hoisting.
            # For hoisting, it uses following rules.
            #   1. (a + ... + z) + (A + ... + Z) = a + ... + z + A + ... + Z
            #   2. (a + ... + z) + A = a + ... + z + A
            #   3. a + (A + ... + Z) = a + A + ... + Z
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.ADD:
                if rt.chd[1].v == Type.OpT.ADD:
                    rt.chd = rt.chd[0].chd + rt.chd[1].chd
                else:
                    rt.chd = rt.chd[0].chd + rt.chd[1:]
            elif rt.chd[1].v == Type.OpT.ADD:
                rt.chd = [rt.chd[0]] + rt.chd[1].chd

            # If there is parent which can handle hoisted children, let it handle.
            if prn and prn.v in [Type.OpT.ADD, Type.OpT.SUB]:
                return rt, warn

            cls.__idx_l.clear()

            for i in range(len(rt.chd)):
                if rt.chd[i].tok_t == Type.TokT.NUM:
                    cls.__idx_l.append(i)

            # If there are no numeric children, we are done.
            # Do packing and return.
            # For packing, it uses following rules.
            #   1. x + (-y) + (-z) = x + -(y + z)
            #   2. (-x) + (-y) = -(x + y)
            # The following logic is an implementation of these rules.
            if not cls.__idx_l:
                for i in range(len(rt.chd)):
                    if rt.chd[i].v == Type.OpT.MINUS:
                        cls.__idx_l.append(i)

                if 1 < len(cls.__idx_l) < len(rt.chd):
                    tmp = Token.OpTok(Type.OpT.MINUS)
                    tmp.add_chd(Token.OpTok(Type.OpT.ADD))

                    for idx in reversed(cls.__idx_l):
                        tmp.chd[0].add_chd(rt.chd[idx].chd[0])
                        rt.del_chd(idx)

                    rt.add_chd(tmp)

                    return rt, warn
                elif len(cls.__idx_l) == len(rt.chd):
                    for i in range(len(rt.chd)):
                        rt.swap_chd(rt.chd[i].chd[0], i)

                    tmp = Token.OpTok(Type.OpT.MINUS)
                    tmp.add_chd(rt)

                    return tmp, warn
                else:
                    return rt, warn

            # Check for warnings.
            # Addition generates warning for followings cases.
            #   1. Any operand exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. Any operand is nan. (NAN_DETECT)
            #   3. Any operand is inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            for idx in cls.__idx_l:
                if is_bigint(rt.chd[idx].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 18, arg_pos=idx + 1, handle='addition'))
                    rt.chd[idx].v = math.inf
                elif is_smallint(rt.chd[idx].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 19, arg_pos=idx + 1, handle='addition'))
                    rt.chd[idx].v = -math.inf
                elif math.isnan(rt.chd[idx].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 7, arg_pos=idx + 1, handle='addition'))
                elif math.isinf(rt.chd[idx].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 8, arg_pos=idx + 1, handle='addition'))

            # Constant folding.
            # Addition (b/w two operand left and right) has following rules.
            #   1. If any of left or right is nan, the result is nan.
            #   2. If left is +-inf and right is +-inf, the result is +-inf, resp.
            #   3. If left is +-inf and right is -+inf, the result is nan.
            #   5. If left is +-inf and right is finite, the result is +-inf, resp.
            #   7. If both left and right is finite, the result is left + right.
            # The following logic is an implementation of these rules.
            for idx in reversed(cls.__idx_l[1:]):
                rt.chd[cls.__idx_l[0]].v += rt.chd[idx].v
                rt.del_chd(idx)

            # Dead expr stripping.
            # For dead expr stripping, it uses following rule.
            #   1. x + 0 = x
            #   2. x + nan = nan
            # The following logic is an implementation of this rule.
            if len(rt.chd) > 1:
                if rt.chd[cls.__idx_l[0]].v == 0:
                    rt.del_chd(cls.__idx_l[0])
                elif math.isnan(rt.chd[cls.__idx_l[0]].v):
                    return rt.chd[cls.__idx_l[0]], warn

            # Packing.
            # For packing, it uses following rules.
            #   1. x + (-y) + (-z) = x + -(y + z)
            #   2. -x + n = -(x + -n)
            #   2. (-x) + (-y) = -(x + y)
            #   3. x + Nil = x
            # The following logic is an implementation of these rules.
            cls.__idx_l.clear()

            if len(rt.chd) == 1:
                return rt.chd[0], warn

            for i in range(len(rt.chd)):
                if rt.chd[i].v == Type.OpT.MINUS or rt.chd[i].tok_t == Type.TokT.NUM:
                    cls.__idx_l.append(i)

            if 1 < len(cls.__idx_l) < len(rt.chd):
                tmp = Token.OpTok(Type.OpT.MINUS)
                tmp.add_chd(Token.OpTok(Type.OpT.ADD))

                for idx in reversed(cls.__idx_l):
                    if rt.chd[idx].tok_t == Type.TokT.NUM:
                        rt.chd[idx].v *= -1
                        tmp.chd[0].add_chd(rt.chd[idx])
                    else:
                        tmp.chd[0].add_chd(rt.chd[idx].chd[0])

                    rt.del_chd(idx)

                rt.add_chd(tmp)

                return rt, warn
            elif len(cls.__idx_l) == len(rt.chd):
                for i in range(len(rt.chd)):
                    if rt.chd[i].tok_t == Type.TokT.NUM:
                        rt.chd[i].v *= -1
                    else:
                        rt.swap_chd(rt.chd[i].chd[0], i)

                tmp = Token.OpTok(Type.OpT.MINUS)
                tmp.add_chd(rt)

                return tmp, warn
            else:
                return rt, warn
        if rt.v == Type.OpT.SUB:
            # Hoisting.
            # For hoisting, it uses following rules with simple optimization -(-x) = x.
            #   1. (a + ... + z) - (A + ... + Z) = a + ... + z + (-A) + ... + (-Z)
            #   2. (a + ... + z) - A = a + ... + z + (-A)
            #   3. a - (A + ... + Z) = a + (-A) + ... + (-Z)
            #   4. a - A = a + (-A)
            # The following logic is an implementation of these rules.
            rt.v = Type.OpT.ADD

            if rt.chd[0].v == Type.OpT.ADD:
                if rt.chd[1].v == Type.OpT.ADD:
                    for i in range(len(rt.chd[1].chd)):
                        if rt.chd[1].chd[i].v == Type.OpT.MINUS:
                            rt.chd[1].swap_chd(
                                rt.chd[1].chd[i].chd[0], i)
                        elif rt.chd[1].chd[i].tok_t == Type.TokT.NUM:
                            rt.chd[1].chd[i].v *= -1
                        else:
                            tmp = Token.OpTok(Type.OpT.MINUS)
                            tmp.add_chd(rt.chd[1].chd[i])
                            rt.chd[1].swap_chd(tmp, i)

                    rt.chd = rt.chd[0].chd + rt.chd[1].chd
                else:
                    if rt.chd[1].v == Type.OpT.MINUS:
                        rt.swap_chd(rt.chd[1].chd[0], 1)
                    elif rt.chd[1].tok_t == Type.TokT.NUM:
                        rt.chd[1].v *= -1
                    else:
                        tmp = Token.OpTok(Type.OpT.MINUS)
                        tmp.add_chd(rt.chd[1])
                        rt.chd = rt.chd[0].chd
                        rt.add_chd(tmp)
            elif rt.chd[1].v == Type.OpT.ADD:
                for i in range(len(rt.chd[1].chd)):
                    if rt.chd[1].chd[i].v == Type.OpT.MINUS:
                        rt.chd[1].swap_chd(
                            rt.chd[1].chd[i].chd[0], i)
                    elif rt.chd[1].chd[i].tok_t == Type.TokT.NUM:
                        rt.chd[1].chd[i].v *= -1
                    else:
                        tmp = Token.OpTok(Type.OpT.MINUS)
                        tmp.add_chd(rt.chd[1].chd[i])
                        rt.chd[1].swap_chd(tmp, i)

                rt.chd = rt.chd[:-1] + rt.chd[1].chd
            else:
                if rt.chd[1].v == Type.OpT.MINUS:
                    rt.swap_chd(rt.chd[1].chd[0], 1)
                elif rt.chd[1].tok_t == Type.TokT.NUM:
                    rt.chd[1].v *= -1
                else:
                    tmp = Token.OpTok(Type.OpT.MINUS)
                    tmp.add_chd(rt.chd[1])
                    rt.swap_chd(tmp, 1)

            # If there is parent which can handle hoisted children, let it handle.
            # Otherwise, call simplify method for addition to handle.
            if prn and prn.v in [Type.OpT.ADD, Type.OpT.SUB]:
                return rt, warn
            else:
                return cls.simplify(rt, prn)
        elif rt.v == Type.OpT.MUL:
            # Hoisting.
            # For hoisting, it uses following rules.
            #   1. (a * ... * z) * (A * ... * Z) = a * ... * z * A * ... * Z
            #   2. (a * ... * z) * A = a * ... * z * A
            #   3. a * (A * ... * Z) = a * A * ... * Z
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MUL:
                if rt.chd[1].v == Type.OpT.MUL:
                    rt.chd = rt.chd[0].chd + rt.chd[1].chd
                else:
                    rt.chd = rt.chd[0].chd + rt.chd[1:]
            elif rt.chd[1].v == Type.OpT.MUL:
                rt.chd = [rt.chd[0]] + rt.chd[1].chd

            # If there is parent which can handle hoisted children, let it handle.
            if prn and prn.v == Type.OpT.MUL:
                return rt, warn

            cls.__idx_l.clear()

            # Sign propagation.
            # If the # of MINUS is odd, the sign can be propagated.
            for i in range(len(rt.chd)):
                if rt.chd[i].v == Type.OpT.MINUS:
                    sgn = not sgn
                    rt.swap_chd(rt.chd[i].chd[0], i)
                elif rt.chd[i].tok_t == Type.TokT.NUM:
                    cls.__idx_l.append(i)

            # Check for warnings.
            # Multiplication generates warning for followings cases.
            #   1. Any operand exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. Any operand is nan. (NAN_DETECT)
            #   3. Any operand is inf. (INF_DETECT)
            # The following logic is an implementation of these rules.
            for idx in cls.__idx_l:
                if is_bigint(rt.chd[idx].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 18, arg_pos=idx + 1, handle='multiplication'))
                    rt.chd[idx].v = math.inf
                elif is_smallint(rt.chd[idx].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 19, arg_pos=idx + 1, handle='multiplication'))
                    rt.chd[idx].v = -math.inf
                elif math.isnan(rt.chd[idx].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 7, arg_pos=idx + 1, handle='multiplication'))
                elif math.isinf(rt.chd[idx].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 8, arg_pos=idx + 1, handle='multiplication'))

            # If there are no numeric children, we are done.
            # Do packing and return.
            # For packing, it uses following rules with consideration of sign propagation.
            #   1. x * (y^-1) * (z^-1) = x * ((y * z)^-1)
            #   2. (x^-1) * (y^-1) = (x * y)^-1
            # The following logic is an implementation of these rules.
            if not cls.__idx_l:
                for i in range(len(rt.chd)):
                    if rt.chd[i].v == Type.OpT.POW and rt.chd[i].chd[1].v == -1:
                        cls.__idx_l.append(i)

                if sgn:
                    if 1 < len(cls.__idx_l) < len(rt.chd):
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [Token.OpTok(Type.OpT.MUL), rt.chd[cls.__idx_l[0]].chd[1]]

                        for idx in reversed(cls.__idx_l):
                            tmp.chd[0].add_chd(rt.chd[idx].chd[0])
                            rt.del_chd(idx)

                        rt.add_chd(tmp)
                        tmp = Token.OpTok(Type.OpT.MINUS)
                        tmp.add_chd(rt)

                        return tmp, warn
                    elif len(cls.__idx_l) == len(rt.chd):
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [Token.OpTok(Type.OpT.MUL), rt.chd[cls.__idx_l[0]].chd[1]]

                        for i in range(len(rt.chd)):
                            rt.swap_chd(rt.chd[i].chd[0], i)

                        tmp.chd[0].chd = rt.chd
                        rt, tmp = tmp, Token.OpTok(Type.OpT.MINUS)
                        tmp.add_chd(rt)

                        return tmp, warn
                    else:
                        tmp = Token.OpTok(Type.OpT.MINUS)
                        tmp.add_chd(rt)

                        return tmp, warn
                else:
                    if 1 < len(cls.__idx_l) < len(rt.chd):
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [Token.OpTok(Type.OpT.MUL), rt.chd[cls.__idx_l[0]].chd[1]]

                        for idx in reversed(cls.__idx_l):
                            tmp.chd[0].add_chd(rt.chd[idx].chd[0])
                            rt.del_chd(idx)

                        rt.add_chd(tmp)

                        return rt, warn
                    elif len(cls.__idx_l) == len(rt.chd):
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [Token.OpTok(Type.OpT.MUL), rt.chd[cls.__idx_l[0]].chd[1]]

                        for i in range(len(rt.chd)):
                            rt.swap_chd(rt.chd[i].chd[0], i)

                        tmp.chd[0].chd = rt.chd

                        return tmp, warn
                    else:
                        return rt, warn

            # Constant folding.
            # Multiplication (b/w two operand left and right) has following rules.
            #   1. If any of left or right is nan, the result is nan.
            #   2. If left is +-inf and right is +-inf, the result is +inf.
            #   3. If left is +-inf and right is -+inf, the result is -inf.
            #   4. If left is +-inf and right is 0, the result is nan.
            #   5. If left is +-inf and right is finite positive, the result is +-inf, resp.
            #   6. If left is +-inf and right is finite negative, the result is -+inf, resp.
            #   7. If both left and right is finite, the result is left * right.
            # The following logic is an implementation of these rules.
            for idx in reversed(cls.__idx_l[1:]):
                rt.chd[cls.__idx_l[0]].v *= rt.chd[idx].v
                rt.del_chd(idx)

            rt.chd[cls.__idx_l[0]].v *= -1 if sgn else 1
            sgn = False

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. x * 1 = x
            #   2. x * -1 = -x
            #   3. x * nan = nan
            # The following logic is an implementation of these rules.
            if len(rt.chd) > 1:
                if rt.chd[cls.__idx_l[0]].v == 1:
                    rt.del_chd(cls.__idx_l[0])
                elif rt.chd[cls.__idx_l[0]].v == -1:
                    sgn = True
                    rt.del_chd(cls.__idx_l[0])
                elif math.isnan(rt.chd[cls.__idx_l[0]].v):
                    return rt.chd[cls.__idx_l[0]], warn

            # Packing.
            # For packing, it uses following rules.
            #   1. x * (y^-1) * (z^-1) = x * ((y * z)^-1)
            #   2. (x^-1) * n = (x * n^-1)^-1
            #   2. (x^-1) * (y^-1) = (x * y)^-1
            #   3. x * Nil = x
            # The following logic is an implementation of these rules.
            cls.__idx_l.clear()

            if len(rt.chd) == 1:
                if sgn:
                    tmp = Token.OpTok(Type.OpT.MINUS)
                    tmp.add_chd(rt.chd[0])

                    return tmp, warn
                else:
                    return rt.chd[0], warn
            else:
                for i in range(len(rt.chd)):
                    if (rt.chd[i].v == Type.OpT.POW and rt.chd[i].chd[1].v == -1) or \
                            (rt.chd[i].tok_t == Type.TokT.NUM and rt.chd[i].v != 0):
                        cls.__idx_l.append(i)

                if sgn:
                    if 1 < len(cls.__idx_l) < len(rt.chd):
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [Token.OpTok(Type.OpT.MUL), Token.NumTok(-1)]

                        for idx in reversed(cls.__idx_l):
                            if rt.chd[idx].tok_t == Type.TokT.NUM:
                                rt.chd[idx].v **= -1
                                tmp.chd[0].add_chd(rt.chd[idx])
                            else:
                                tmp.chd[0].add_chd(rt.chd[idx].chd[0])

                            rt.del_chd(idx)

                        rt.add_chd(tmp)
                        tmp = Token.OpTok(Type.OpT.MINUS)
                        tmp.add_chd(rt)

                        return tmp, warn
                    elif len(cls.__idx_l) == len(rt.chd):
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [Token.OpTok(Type.OpT.MUL), Token.NumTok(-1)]

                        for i in range(len(rt.chd)):
                            if rt.chd[i].tok_t == Type.TokT.NUM:
                                rt.chd[i].v **= -1
                            else:
                                rt.swap_chd(rt.chd[i].chd[0], i)

                        tmp.chd[0].chd = rt.chd
                        rt, tmp = tmp, Token.OpTok(Type.OpT.MINUS)
                        tmp.add_chd(rt)

                        return tmp, warn
                    else:
                        tmp = Token.OpTok(Type.OpT.MINUS)
                        tmp.add_chd(rt)

                        return tmp, warn
                else:
                    if 1 < len(cls.__idx_l) < len(rt.chd):
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [Token.OpTok(Type.OpT.MUL), Token.NumTok(-1)]

                        for idx in reversed(cls.__idx_l):
                            if rt.chd[idx].tok_t == Type.TokT.NUM:
                                rt.chd[idx].v **= -1
                                tmp.chd[0].add_chd(rt.chd[idx])
                            else:
                                tmp.chd[0].add_chd(rt.chd[idx].chd[0])

                            rt.del_chd(idx)

                        rt.add_chd(tmp)

                        return rt, warn
                    elif len(cls.__idx_l) == len(rt.chd):
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [Token.OpTok(Type.OpT.MUL), Token.NumTok(-1)]

                        for i in range(len(rt.chd)):
                            if rt.chd[i].tok_t == Type.TokT.NUM:
                                rt.chd[i].v **= -1
                            else:
                                rt.swap_chd(rt.chd[i].chd[0], i)

                        tmp.chd[0].chd = rt.chd

                        return tmp, warn
                    else:
                        return rt, warn
        elif rt.v == Type.OpT.DIV:
            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. x / (-y) = -x / y
            #   2. (-x) / (-y) = x / y
            #   3. n / (-y) = (-n) / y
            #   4. (x * y) / -z = (x * y * -1) / z
            # The following logic is an implementation of this rule.
            if rt.chd[1].v == Type.OpT.MINUS:
                if rt.chd[0].v == Type.OpT.MINUS:
                    rt.swap_chd(rt.chd[0], 0)
                elif rt.chd[0].v == Type.OpT.MUL:
                    rt.chd[0].add_chd(Token.NumTok(-1))
                elif rt.chd[0].tok_t == Type.TokT.NUM:
                    rt.chd[0].v *= -1
                else:
                    tmp = Token.OpTok(Type.OpT.MINUS)
                    tmp.add_chd(rt.chd[0])
                    rt.swap_chd(tmp, 0)

                rt.swap_chd(rt.chd[1].chd[0], 1)

            # Hoisting.
            # For hoisting, it uses following rules with simple optimization (x^-1)^-1 = x, (x^y)^-1=x^(-y).
            #   1. (a * ... * z) / (A * ... * Z) = a * ... * z * (A^-1) * ... * (Z^-1)
            #   2. (a * ... * z) / A = a * ... * z * (A^-1)
            #   3. a / (A * ... * Z) = a * (A^-1) * ... * (Z^-1)
            #   4. a / A = a * (A^-1)
            # The following logic is an implementation of these rules.
            rt.v = Type.OpT.MUL

            if rt.chd[0].v == Type.OpT.MUL:
                if rt.chd[1].v == Type.OpT.MUL:
                    for i in range(len(rt.chd[1].chd)):
                        if rt.chd[1].chd[i].v == Type.OpT.POW:
                            if rt.chd[1].chd[i].chd[1].v == -1:
                                rt.chd[1].swap_chd(rt.chd[1].chd[i].chd[0], i)
                            else:
                                rt.chd[1].chd[i].chd[1].v *= -1
                        elif rt.chd[1].chd[i].tok_t == Type.TokT.NUM:
                            if is_bigint(rt.chd[1].chd[i].v) or is_smallint(rt.chd[1].chd[i].v):
                                rt.chd[1].chd[i].v = 0
                            elif rt.chd[1].chd[i].v == 0:
                                rt.chd[1].chd[i].v = math.nan
                            else:
                                rt.chd[1].chd[i].v **= -1
                        else:
                            tmp = Token.OpTok(Type.OpT.POW)
                            tmp.chd = [rt.chd[1].chd[i], Token.NumTok(-1)]
                            rt.chd[1].swap_chd(tmp, i)

                    rt.chd = rt.chd[0].chd + rt.chd[1].chd
                else:
                    if rt.chd[1].v == Type.OpT.POW:
                        if rt.chd[1].chd[1].v == -1:
                            rt.swap_chd(rt.chd[1].chd[0], 1)
                        else:
                            rt.chd[1].chd[1].v = -rt.chd[1].chd[1].v
                    elif rt.chd[1].tok_t == Type.TokT.NUM:
                        if is_bigint(rt.chd[1].v) or is_smallint(rt.chd[1].v):
                            rt.chd[1].v = 0
                        elif rt.chd[1].v == 0:
                            rt.chd[1].v = math.nan
                        else:
                            rt.chd[1].v **= -1
                    else:
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [rt.chd[1], Token.NumTok(-1)]
                        rt.chd = rt.chd[0].chd
                        rt.add_chd(tmp)
            elif rt.chd[1].v == Type.OpT.MUL:
                for i in range(len(rt.chd[1].chd)):
                    if rt.chd[1].chd[i].v == Type.OpT.POW:
                        if rt.chd[1].chd[i].chd[1].v == -1:
                            rt.chd[1].swap_chd(rt.chd[1].chd[i].chd[0], i)
                        else:
                            rt.chd[1].chd[i].chd[1].v *= -1
                    elif rt.chd[1].chd[i].tok_t == Type.TokT.NUM:
                        if is_bigint(rt.chd[1].chd[i].v) or is_smallint(rt.chd[1].chd[i].v):
                            rt.chd[1].chd[i].v = 0
                        elif rt.chd[1].chd[i].v == 0:
                            rt.chd[1].chd[i].v = math.nan
                        else:
                            rt.chd[1].chd[i].v **= -1
                    else:
                        tmp = Token.OpTok(Type.OpT.POW)
                        tmp.chd = [rt.chd[1].chd[i], Token.NumTok(-1)]
                        rt.chd[1].swap_chd(tmp, i)

                rt.chd = rt.chd[:-1] + rt.chd[1].chd
            else:
                if rt.chd[1].v == Type.OpT.POW:
                    if rt.chd[1].chd[1].v == -1:
                        rt.swap_chd(rt.chd[1].chd[0], 1)
                    else:
                        rt.chd[1].chd[1].v *= -1
                elif rt.chd[1].tok_t == Type.TokT.NUM:
                    if is_bigint(rt.chd[1].v) or is_smallint(rt.chd[1].v):
                        rt.chd[1].v = 0
                    elif rt.chd[1].v == 0:
                        rt.chd[1].v = math.nan
                    else:
                        rt.chd[1].v **= -1
                else:
                    tmp = Token.OpTok(Type.OpT.POW)
                    tmp.chd = [rt.chd[1], Token.NumTok(-1)]
                    rt.swap_chd(tmp, 1)

            # If there is parent which can handle hoisted children, let it handle.
            # Otherwise, call simplify method for addition to handle.
            if prn and prn.v in [Type.OpT.DIV, Type.OpT.MUL]:
                return rt, warn
            else:
                return cls.simplify(rt, prn)
        elif rt.v == Type.OpT.REM:
            # Sign propagation.
            # For sign propagation, it uses following rules.
            #   1. (-x) % (-y) = -(x % y)
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == rt.chd[1].v == Type.OpT.MINUS:
                sgn = True
                tmp = rt.chd[0]
                rt.chd = [rt.chd[0].chd[0], rt.chd[1].chd[0]]

            # Check for warnings.
            # Remainder operator generates warning for followings cases.
            #   1. Nominator or denominator exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. Nominator or denominator is nan. (NAN_DETECT)
            #   3. Nominator or denominator is inf. (INF_DETECT)
            #   4. Denominator is 0. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 18, arg_pos=1, handle='remainder operation'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 19, arg_pos=1, handle='remainder operation'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 7, arg_pos=1, handle='remainder operation'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 8, arg_pos=1, handle='remainder operation'))

            if rt.chd[1].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[1].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 18, arg_pos=2, handle='remainder operation'))
                    rt.chd[1].v = math.inf
                elif is_smallint(rt.chd[1].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 19, arg_pos=2, handle='remainder operation'))
                    rt.chd[1].v = -math.inf
                elif math.isnan(rt.chd[1].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 7, arg_pos=2, handle='remainder operation'))
                elif math.isinf(rt.chd[1].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 8, arg_pos=2, handle='remainder operation'))
                elif rt.chd[1].v == 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 10))

            # Constant folding.
            # Remainder operator has following rules.
            #   1. If any of nominator or denominator is nan, the result is nan.
            #   2. If nominator is +-inf or denominator is 0, the result is nan.
            #   3. If nominator is finite nonnegative and denominator is +inf, the result is nominator itself.
            #   4. If nominator is finite nonnegative and denominator is -inf, the result is -inf.
            #   5. If nominator is finite nonpositive and denominator is -inf, the result is nominator itself.
            #   6. If nominator is finite nonpositive and denominator is +inf, the result is +inf.
            #   7. If nominator is finite and denominator is finite nonzero, the result is nominator % denominator.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
                if rt.chd[1].v == 0:
                    rt.chd[0].v = math.nan
                else:
                    rt.chd[0].v = rt.chd[0].v % rt.chd[1].v

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. nan % x = nan
            #   2. x % nan = nan
            #   3. x % 0 = nan
            #   4. +-inf % x = nan
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if math.isnan(rt.chd[0].v):
                    return rt.chd[0], warn
                elif math.isinf(rt.chd[0].v):
                    rt.chd[0].v = math.nan

                    return rt.chd[0], warn
            elif rt.chd[1].tok_t == Type.TokT.NUM:
                if math.isnan(rt.chd[1].v):
                    return rt.chd[1], warn
                elif rt.chd[1].v == 0:
                    rt.chd[1].v = math.nan

                    return rt.chd[1], warn

            if sgn:
                tmp.swap_chd(rt, 0)
            else:
                tmp = rt

            return tmp, warn
        elif rt.v == Type.OpT.FACT:
            # Check for warnings.
            # Factorial operator generates warning for followings cases.
            #   1. Operand exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. Operand is nan. (NAN_DETECT)
            #   3. Nominator is inf. (INF_DETECT)
            #   4. Operand is negative integer. (POLE_DETECT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 18, arg_pos=1, handle='factorial operation'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 9))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 7, arg_pos=1, handle='factorial operation'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(
                        Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 8, arg_pos=1, handle='factorial operation'))
                elif rt.chd[0].v % 1 == 0 and rt.chd[0].v < 0:
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 9))

            # Constant folding.
            # Factorial operator has following rules.
            #   1. If operand is nan, the result is nan.
            #   2. If operand is +inf, the result is +inf.
            #   3. If operand is -inf or finite negative integer, the result is nan.
            #   4. If operand is finite nonnegative integer, the result is ``math.factorial(x)``.
            #   5. If operand is finite noninteger, the result is ``math.gamma(x + 1)``.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if rt.chd[0].v < 0 and math.isinf(rt.chd[0].v):
                    rt.chd[0].v = math.nan
                elif rt.chd[0].v % 1 == 0:
                    if rt.chd[0].v >= 0:
                        rt.chd[0].v = math.factorial(rt.chd[0].v)
                    else:
                        rt.chd[0].v = math.nan
                else:
                    try:
                        rt.chd[0].v = math.gamma(rt.chd[0].v + 1)
                    except OverflowError:
                        rt.chd[0].v = math.inf

                return rt.chd[0], warn

            return rt, warn
        elif rt.v == Type.OpT.POW:
            # Sign propagation.
            # For sign propagation, it uses following rule.
            #   1. (-x)^y = -(x^y) if y is odd.
            # The following logic is an implementation of this rule.
            if rt.chd[0].v == Type.OpT.MINUS and rt.chd[1].tok_t == Type.TokT.NUM and rt.chd[1].v % 2 == 1:
                sgn = True
                tmp = rt.chd[0]
                rt.swap_chd(tmp.chd[0], 0)

            # Check for warnings.
            # Power operator generates warning for followings cases.
            #   1. Base or exponent exceeds floating point max/min size. (BIG_INT/SMALL_INT, resp.)
            #   2. Base or exponent is nan. (NAN_DETECT)
            #   3. Base or exponent is inf. (INF_DETECT)
            #   4. Base is 0 and exponent is finite negative integer. (POLE_DETECT)
            #   5. Base is finite negative and exponent is finite noninteger. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 18, arg_pos=1, handle='power operation'))
                    rt.chd[0].v = math.inf
                elif is_smallint(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 19, arg_pos=1, handle='power operation'))
                    rt.chd[0].v = -math.inf
                elif math.isnan(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 7, arg_pos=1, handle='power operation'))
                elif math.isinf(rt.chd[0].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 8, arg_pos=1, handle='power operation'))

                if rt.chd[1].tok_t == Type.TokT.NUM:
                    if rt.chd[0].v == 0 and rt.chd[1].v < 0:
                        if rt.chd[1].v % 1 == 0:
                            warn.append(Warning.InterpWarn(Type.InterpWarnT.POLE_DETECT, 11))
                        else:
                            warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 11))
                    elif rt.chd[0].v < 0 and rt.chd[1].v % 1 != 0:
                        warn.append(Warning.InterpWarn(Type.InterpWarnT.DOMAIN_OUT, 12))

            if rt.chd[1].tok_t == Type.TokT.NUM:
                if is_bigint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.BIG_INT, 18, arg_pos=2, handle='power operation'))
                    rt.chd[1].v = math.inf
                elif is_smallint(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.SMALL_INT, 19, arg_pos=2, handle='power operation'))
                    rt.chd[1].v = -math.inf
                elif math.isnan(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.NAN_DETECT, 7, arg_pos=2, handle='power operation'))
                elif math.isinf(rt.chd[1].v):
                    warn.append(Warning.InterpWarn(Type.InterpWarnT.INF_DETECT, 8, arg_pos=2, handle='power operation'))

            # Hoisting.
            # For hoisting, it uses following rules with simple optimization (x^-1)^-1 = x, (x^y)^-1=x^(-y).
            #   1. (x^y)^z = x^(y * z)
            # The following logic is an implementation of these rules.
            # Note that hoisting occurs only for NUN token.
            if rt.chd[0].v == Type.OpT.POW and rt.chd[1].tok_t == rt.chd[0].chd[1].tok_t == Type.TokT.NUM:
                rt.chd[1].v *= rt.chd[0].chd[1].v
                rt.swap_chd(rt.chd[0].chd[0], 0)

            # Constant folding.
            # Power operator has following rules.
            #   1. If exponent is 0, the result is 1.
            #   2. If exponent is nan, the result is nan.
            #   3. If base is 0 and exponent is +inf, the result is 0.
            #   4. If base is 0 and exponent is -inf, the result is +inf.
            #   5. If base is nan and exponent is nonzero, the result is nan.
            #   6. If base is not nan and exponent is +inf, the result is +inf.
            #   7. If base is not nan and exponent is -inf, the result is 0.
            #   8. If base is +inf and exponent is finite positive, the result is +inf.
            #   9. If base is -inf and exponent is finite positive which is not odd integer, the result is +inf.
            #   10. If base is -inf and exponent is finite positive odd integer, the result is -inf.
            #   11. If base is +-inf and exponent is finite negative, the result is 0.
            #   12. If base is 0 and exponent is finite negative, the result is nan.
            #   13. If base is 0 and exponent is finite positive, the result is 0.
            #   14. If base is finite negative and exponent is finite noninteger, the result is nan.
            #   15. If base is finite negative and exponent is finite integer, the result is base ** exponent.
            #   16. If base is finite positive and exponent is finite, the result is base ** exponent.
            # The following logic is an implementation of these rules.
            if rt.chd[0].tok_t == rt.chd[1].tok_t == Type.TokT.NUM:
                if rt.chd[0].v == 0 and rt.chd[1].v < 0:
                    rt.chd[0].v = math.nan
                elif rt.chd[0].v < 0 and rt.chd[1].v % 1 != 0:
                    rt.chd[0].v = math.nan
                else:
                    try:
                        rt.chd[0].v = rt.chd[0].v ** rt.chd[1].v
                    except OverflowError:
                        rt.chd[0].v = math.inf

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. x^0 = 1
            #   2. x^1 = x
            #   3. (-x)^y = x^y if y is even.
            #   4. x^nan = nan
            # The following logic is an implementation of these rules.
            if rt.chd[1].tok_t == Type.TokT.NUM:
                if rt.chd[1].v == 0:
                    rt.chd[1].v = 1

                    return rt.chd[1], warn
                elif rt.chd[1].v == 1:
                    if sgn:
                        tmp.swap_chd(rt.chd[0], 0)
                    else:
                        tmp = rt.chd[0]

                    return tmp, warn
                elif rt.chd[0].v == Type.OpT.MINUS and rt.chd[1].v % 2 == 0:
                    rt.swap_chd(rt.chd[0].chd[0], 0)

                    return rt, warn
                elif math.isnan(rt.chd[1].v):
                    return rt.chd[1], warn

            if sgn:
                tmp.swap_chd(rt, 0)
            else:
                tmp = rt

            return tmp, warn
        elif rt.v == Type.OpT.PLUS:
            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. +x = x
            # The following logic is an implementation of these rules.
            return rt.chd[0], warn
        else:
            # Constant folding.
            if rt.chd[0].tok_t == Type.TokT.NUM:
                rt.chd[0].v = -rt.chd[0].v

                return rt.chd[0], warn

            # Dead expr stripping.
            # For dead expr stripping, it uses following rules.
            #   1. -(-x) = x
            #   2. -(x * n) = x * -n
            # The following logic is an implementation of these rules.
            if rt.chd[0].v == Type.OpT.MINUS:
                return rt.chd[0].chd[0], warn
            elif rt.chd[0].v == Type.OpT.MUL:
                for tok in rt.chd[0].chd:
                    if tok.tok_t == Type.TokT.NUM:
                        tok.v *= -1

                        return rt.chd[0], warn

            # Unpacking.
            # For distribution, it uses following rules with simple optimization -(-x) = x.
            #   1. -(a + ... + z) = (-a) + ... + (-z)
            #   2. -(a * ... * z) = a * ... * z * -1
            # The following logic is an implementation of these rules.
            if prn:
                if prn.v in [Type.OpT.ADD, Type.OpT.SUB] and rt.chd[0].v == Type.OpT.ADD:
                    for i in range(len(rt.chd[0].chd)):
                        if rt.chd[0].chd[i].v == Type.OpT.MINUS:
                            rt.chd[0].swap_chd(
                                rt.chd[0].chd[i].chd[0], i)
                        elif rt.chd[0].chd[i].tok_t == Type.TokT.NUM:
                            rt.chd[0].chd[i].v = -rt.chd[0].chd[i].v
                        else:
                            tmp = Token.OpTok(Type.OpT.MINUS)
                            tmp.add_chd(rt.chd[0].chd[i])
                            rt.chd[0].swap_chd(tmp, i)

                    return rt.chd[0], warn
                elif prn.v in [Type.OpT.MUL, Type.OpT.DIV] and rt.chd[0].v == Type.OpT.MUL:
                    rt.chd[0].add_chd(Token.NumTok(-1))

                    return rt.chd[0], warn
            return rt, warn
