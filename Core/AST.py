from __future__ import annotations

from typing import Dict, Tuple, List

from Core import Token
from Operator import *


class AST:
    """
    AST class which supports various string expression generation.

    Note that in this program, AST is also expression tree.
    For the concept of AST and expression tree, refer to the reference below.

    **Reference**
        * https://en.wikipedia.org/wiki/Abstract_syntax_tree
        * https://en.wikipedia.org/wiki/Binary_expression_tree

    :ivar __rt: Root token of AST.
    :ivar __line: Original user input string.
    """
    __var_tb: Dict[int, str] = {}

    def __init__(self, rt, line: str = None) -> None:
        self.__rt = rt
        self.__line: str = line

    def __str__(self) -> str:
        """
        Generate infix string expression of AST.

        It just calls its helper ``AST.__str_hlpr``.
        For detailed description of infix expression generation, refer to the comments in ``AST.__str_hlpr``.

        :return: Infix expression.
        :rtype: str
        """
        return self.__str_hlpr(self.__rt)

    @classmethod
    def var_name(cls, k: int) -> str:
        """
        Find variable from variable table with key.

        :param k: Key of variable to be found.
        :type k: int

        :return: Found variable.
        :rtype: str
        """
        return cls.__var_tb.get(k)

    @classmethod
    def add_var(cls, k: int, var: str) -> None:
        """
        Add variable with key in variable table.

        :param k: Key of variable to be added.
        :type k: int
        :param var: Variable to be added.
        :type var: str
        """
        cls.__var_tb[k] = var

    def __str_hlpr(self, rt) -> str:
        """
        Generate infix expression of partial AST.

        For construction, it uses inorder traversal of AST.
        It also handles parenthesis properly.
        For the concept and implementation of inorder traversal, consult the references below.

        This method is private and called internally as a helper of ``AST.__str__``.

        **Reference**
            * https://en.wikipedia.org/wiki/Tree_traversal#In-order_(LNR)
            * https://en.wikipedia.org/wiki/Binary_expression_tree#Infix_traversal

        :param rt: Root of partial AST whose infix expression is to be generated.
        :type rt: Token.Tok

        :return: Infix expression.
        :rtype: str
        """
        # For infix expression, it must determine whether parenthesis is needed.
        # This can be done by comparing the precedence b/w operator.
        # If outer precedence of parent operator is higher than inner precedence of child operator, there must be
        # parenthesis.
        # Otherwise, there is no need of parenthesis.
        # Also note that escape sequence of STR token should be unescaped.
        # The following logic is an implementation of these rules.
        tok_t: type = type(rt)

        if tok_t == Token.Op:
            buf: str = ''  # Buffer for operands.

            if rt.v in [Binary.Add, Binary.Mul, Binary.MatMul, Bool.And, Bool.Or, Bool.Xor]:
                for tok in rt.chd:
                    if type(tok) == Token.Op and rt.precd_in > tok.precd_in:
                        buf += f'({self.__str_hlpr(tok)}) {rt.v.sym()} '
                    else:
                        buf += f'{self.__str_hlpr(tok)} {rt.v.sym()} '

                return buf[:-len(rt.v.sym()) - 2]
            elif rt.v == Binary.Pow or rt.v.__base__ == Assign.AsgnOp:
                if type(rt.chd[0]) == Token.Op and rt.precd_in >= rt.chd[0].precd_in:
                    buf += f'({self.__str_hlpr(rt.chd[0])}) {rt.v.sym()} '
                else:
                    buf += f'{self.__str_hlpr(rt.chd[0])} {rt.v.sym()} '

                if type(rt.chd[1]) == Token.Op and rt.precd_in > rt.chd[1].precd_in:
                    buf += f'({self.__str_hlpr(rt.chd[1])})'
                else:
                    buf += self.__str_hlpr(rt.chd[1])

                return buf
            elif rt.v in [Unary.Plus, Unary.Minus, Bool.Neg]:
                if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                    return f'{rt.v.sym()}({self.__str_hlpr(rt.chd[0])})'
                else:
                    return f'{rt.v.sym()}{self.__str_hlpr(rt.chd[0])}'
            elif rt.v == Unary.Trans:
                if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in and rt.chd[0].v != Delimiter.Idx:
                    return f'({self.__str_hlpr(rt.chd[0])})\''
                else:
                    return f'{self.__str_hlpr(rt.chd[0])}\''
            elif rt.v == Delimiter.Seq:
                if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                    buf += f'({self.__str_hlpr(rt.chd[0])}):'
                else:
                    buf += f'{self.__str_hlpr(rt.chd[0])}:'
                if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                    buf += f'({self.__str_hlpr(rt.chd[1])})'
                else:
                    buf += self.__str_hlpr(rt.chd[1])

                return buf
            elif rt.v == Delimiter.Idx:
                if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                    buf += f'({self.__str_hlpr(rt.chd[0])})['
                else:
                    buf += f'{self.__str_hlpr(rt.chd[0])}['

                return buf + ', '.join([self.__str_hlpr(tok) for tok in rt.chd[1:]]) + ']'
            else:
                if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                    buf += f'({self.__str_hlpr(rt.chd[0])}) {rt.v.sym()} '
                else:
                    buf += f'{self.__str_hlpr(rt.chd[0])} {rt.v.sym()} '

                if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                    buf += f'({self.__str_hlpr(rt.chd[1])})'
                else:
                    buf += self.__str_hlpr(rt.chd[1])

                return buf
        elif tok_t == Token.Fun:
            return rt.v_str() + '[' + ', '.join([self.__str_hlpr(tok) for tok in rt.chd]) + ']'
        elif tok_t == Token.List:
            return '{' + ', '.join([self.__str_hlpr(tok) for tok in rt.chd]) + '}'
        else:
            return rt.v_str()

    def __str_pos_hlpr(self, rt: Token.Tok, target: Token.Tok) -> Tuple[str, bool, int]:
        tok_t: type = type(rt)

        if tok_t == Token.Op:
            if rt.v == Binary.Pow or rt.v.__base__ in [Assign.AsgnOp]:
                tmp_1: Tuple[str, bool, int] = self.__str_pos_hlpr(rt.chd[0], target)
                tmp_2: Tuple[str, bool, int] = self.__str_pos_hlpr(rt.chd[1], target)

                if rt == target:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in >= rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}) {rt.v.sym()} '
                        pos: int = tmp_1[2] + 3
                    else:
                        buf: str = f'{tmp_1[0]} {rt.v.sym()} '
                        pos: int = tmp_1[2] + 1

                    if type(rt.chd[1]) == Token.Op and rt.precd_in > rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, True, pos
                elif tmp_1[1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in >= rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}) {rt.v.sym()} '
                        pos: int = tmp_1[2] + 1
                    else:
                        buf: str = f'{tmp_1[0]} {rt.v.sym()} '
                        pos: int = tmp_1[2]

                    if type(rt.chd[1]) == Token.Op and rt.precd_in > rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, True, pos
                elif tmp_2[1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in >= rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}) {rt.v.sym()} '
                    else:
                        buf: str = f'{tmp_1[0]} {rt.v.sym()} '

                    if type(rt.chd[1]) == Token.Op and rt.precd_in > rt.chd[1].precd_in:
                        pos: int = len(buf) + tmp_2[2] + 1
                        buf += f'({tmp_2[0]})'
                    else:
                        pos: int = len(buf) + tmp_2[2]
                        buf += tmp_2[0]

                    return buf, True, pos
                else:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in >= rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}) {rt.v.sym()} '
                    else:
                        buf: str = f'{tmp_1[0]} {rt.v.sym()} '

                    if type(rt.chd[1]) == Token.Op and rt.precd_in > rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, False, len(buf)
            elif rt.v in [Unary.Plus, Unary.Minus, Bool.Neg]:
                tmp: Tuple[str, bool, int] = self.__str_pos_hlpr(rt.chd[0], target)

                if rt == target:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        return f'{rt.v.sym()}({tmp[0]})', True, 0
                    else:
                        return f'{rt.v.sym()}{tmp[0]}', True, 0
                elif tmp[1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        return f'{rt.v.sym()}({tmp[0]})', True, tmp[2] + 2
                    else:
                        return f'{rt.v.sym()}{tmp[0]}', True, tmp[2] + 1
                else:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        return f'{rt.v.sym()}({tmp[0]})', False, tmp[2] + 3
                    else:
                        return f'{rt.v.sym()}{tmp[0]}', False, tmp[2] + 1
            elif rt.v == Unary.Trans:
                tmp: Tuple[str, bool, int] = self.__str_pos_hlpr(rt.chd[0], target)

                if rt == target:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in and \
                            rt.chd[0].v != Delimiter.Idx:
                        return f'({tmp[0]})\'', True, tmp[2] + 2
                    else:
                        return f'{tmp[0]}\'', True, tmp[2]
                elif tmp[1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in and \
                            rt.chd[0].v != Delimiter.Idx:
                        return f'({tmp[0]})\'', True, tmp[2] + 1
                    else:
                        return f'{tmp[0]}\'', True, tmp[2]
                else:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        return f'({tmp[0]})\'', False, tmp[2] + 3
                    else:
                        return f'{tmp[0]}\'', False, tmp[2] + 1
            elif rt.v == Delimiter.Seq:
                tmp_1: Tuple[str, bool, int] = self.__str_pos_hlpr(rt.chd[0], target)
                tmp_2: Tuple[str, bool, int] = self.__str_pos_hlpr(rt.chd[1], target)

                if rt == target:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}):'
                        pos: int = tmp_1[2] + 2
                    else:
                        buf: str = f'{tmp_1[0]}:'
                        pos: int = tmp_1[2]

                    if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, True, pos
                elif tmp_1[1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}):'
                        pos: int = tmp_1[2] + 1
                    else:
                        buf: str = f'{tmp_1[0]}:'
                        pos: int = tmp_1[2]

                    if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, True, pos
                elif tmp_2[1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}):'
                    else:
                        buf: str = f'{tmp_1[0]}:'

                    if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                        pos: int = len(buf) + tmp_2[2] + 1
                        buf += f'({tmp_2[0]})'
                    else:
                        pos: int = len(buf) + tmp_2[2]
                        buf += tmp_2[0]

                    return buf, True, pos
                else:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}):'
                    else:
                        buf: str = f'{tmp_1[0]}:'

                    if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, False, len(buf)
            elif rt.v == Delimiter.Idx:
                tmp_l: List[Tuple[str, bool, int]] = [self.__str_pos_hlpr(tok, target) for tok in rt.chd]

                if rt == target:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_l[0][0]})['
                        pos: int = tmp_l[0][2] + 2
                    else:
                        buf: str = f'{tmp_l[0][0]}['
                        pos: int = tmp_l[0][2]

                    return buf + ', '.join([tmp[0] for tmp in tmp_l[1:]]) + ']', True, pos
                elif tmp_l[0][1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_l[0][0]})['
                        pos: int = tmp_l[0][2] + 1
                    else:
                        buf: str = f'{tmp_l[0][0]}['
                        pos: int = tmp_l[0][2]

                    return buf + ', '.join([tmp[0] for tmp in tmp_l[1:]]) + ']', True, pos

                if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                    buf: str = f'({tmp_l[0][0]})['
                else:
                    buf: str = f'{tmp_l[0][0]}['

                pos: int = len(buf)
                i: int = 1

                while i < len(tmp_l) and not tmp_l[i][1]:
                    pos += tmp_l[i][2] + 2
                    i += 1

                if i == len(tmp_l):
                    return buf + ', '.join([tmp[0] for tmp in tmp_l[1:]]) + ']', False, pos - 1 if i > 1 else pos + 1
                else:
                    return buf + ', '.join([tmp[0] for tmp in tmp_l[1:]]) + ']', True, pos
            else:
                tmp_1: Tuple[str, bool, int] = self.__str_pos_hlpr(rt.chd[0], target)
                tmp_2: Tuple[str, bool, int] = self.__str_pos_hlpr(rt.chd[1], target)

                if rt == target:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}) {rt.v.sym()} '
                        pos: int = tmp_1[2] + 3
                    else:
                        buf: str = f'{tmp_1[0]} {rt.v.sym()} '
                        pos: int = tmp_1[2] + 1

                    if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, True, pos
                elif tmp_1[1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}) {rt.v.sym()} '
                        pos: int = tmp_1[2] + 1
                    else:
                        buf: str = f'{tmp_1[0]} {rt.v.sym()} '
                        pos: int = tmp_1[2]

                    if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, True, pos
                elif tmp_2[1]:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}) {rt.v.sym()} '
                    else:
                        buf: str = f'{tmp_1[0]} {rt.v.sym()} '

                    if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                        pos: int = len(buf) + tmp_2[2] + 1
                        buf += f'({tmp_2[0]})'
                    else:
                        pos: int = len(buf) + tmp_2[2]
                        buf += tmp_2[0]

                    return buf, True, pos
                else:
                    if type(rt.chd[0]) == Token.Op and rt.precd_in > rt.chd[0].precd_in:
                        buf: str = f'({tmp_1[0]}) {rt.v.sym()} '
                    else:
                        buf: str = f'{tmp_1[0]} {rt.v.sym()} '

                    if type(rt.chd[1]) == Token.Op and rt.precd_in >= rt.chd[1].precd_in:
                        buf += f'({tmp_2[0]})'
                    else:
                        buf += tmp_2[0]

                    return buf, False, len(buf)
        elif tok_t == Token.Fun:
            tmp_l: List[Tuple[str, bool, int]] = [self.__str_pos_hlpr(tok, target) for tok in rt.chd]

            if rt == target:
                return rt.v_str() + '[' + ', '.join([tmp[0] for tmp in tmp_l]) + ']', True, 0

            buf: str = rt.v_str() + '['
            pos: int = len(buf)
            i: int = 0

            while i < len(tmp_l) and not tmp_l[i][1]:
                pos += tmp_l[i][2] + 2
                i += 1

            print(pos)

            if i == len(tmp_l):
                return buf + ', '.join([tmp[0] for tmp in tmp_l]) + ']', False, pos - 1 if i > 0 else pos + 1
            else:
                return buf + ', '.join([tmp[0] for tmp in tmp_l]) + ']', True, pos + tmp_l[i][2]
        elif tok_t == Token.List:
            tmp_l: List[Tuple[str, bool, int]] = [self.__str_pos_hlpr(tok, target) for tok in rt.chd]

            if rt == target:
                return '{' + ', '.join([tmp[0] for tmp in tmp_l]) + '}', True, 0

            buf: str = '{'
            pos: int = 1
            i: int = 0

            while i < len(tmp_l) and not tmp_l[i][1]:
                pos += tmp_l[i][2] + 2
                i += 1

            if i == len(tmp_l):
                return buf + ', '.join([tmp[0] for tmp in tmp_l]) + '}', False, pos - 1 if i > 0 else pos + 1
            else:
                return buf + ', '.join([tmp[0] for tmp in tmp_l]) + '}', True, pos
        else:
            buf: str = rt.v_str()

            return (buf, True, 0) if rt == target else (buf, False, len(buf))

    @property
    def rt(self):
        """
        Getter for root token of AST.

        :return: Root token.
        :rtype: Token.Tok
        """
        return self.__rt

    @property
    def line(self) -> str:
        """
        Getter for original user input string.

        :return: Original input string.
        :rtype: str
        """
        return self.__line

    @rt.setter
    def rt(self, tok) -> None:
        """
        Setter for root token of AST.

        :param tok: Token to be set as a root.
        :type tok: Token.Tok
        """
        self.__rt = tok

    def str_pos(self, tok: Token.Tok) -> Tuple[str, int]:
        res = self.__str_pos_hlpr(self.__rt, tok)

        return res[0], res[2]
