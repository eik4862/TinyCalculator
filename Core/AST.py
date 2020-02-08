from typing import Dict

from Core import Type


# TODO: LATEX code generation
class AST:
    """
    AST class which supports various string expression generation.

    Note that in this program, AST is also expression tree.
    For the concept of AST and expression tree, refer to the reference below.

    **Reference**
        * https://en.wikipedia.org/wiki/Abstract_syntax_tree
        * https://en.wikipedia.org/wiki/Binary_expression_tree

    :cvar __var_tb: Variable hash table.

    :ivar __rt: Root token of AST.
    :ivar __line: Original user input string.
    """
    __var_tb: Dict[int, str] = {}

    def __init__(self, rt, line: str) -> None:
        self.__rt = rt
        self.__line: str = line

    def __del__(self) -> None:
        pass

    def __infix_hlpr(self, rt) -> str:
        """
        Generate infix expression of partial AST.

        For construction, it uses inorder traversal of AST.
        It also handles parenthesis properly.
        For the concept and implementation of inorder traversal, consult the references below.

        This method is private and called internally as a helper of ``AST.__infix``.

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
        #   1. If current operator has higher precedence, there must be parenthesis.
        #   2. If current operator has lower precedence, there is no need of parenthesis.
        #   3. If current operator and child operator has the same precedence, there is no need of parenthesis in
        #      general.
        #   4. Few exceptions of rule 3 is SUB, DIV, REM with same precedence operator as right child and POW operator
        #      with same precedence operator as left child.
        # The following logic is an implementation of these rules.
        if rt.tok_t in [Type.TokT.NUM, Type.TokT.VAR]:
            return str(rt.v)
        elif rt.tok_t == Type.TokT.STR:
            return f'\"{rt.v}\"'
        elif rt.tok_t == Type.TokT.OP:
            if rt.v in [Type.OpT.ADD, Type.OpT.PLUS]:
                op: str = '+'  # Operator.
            elif rt.v in [Type.OpT.SUB, Type.OpT.MINUS]:
                op: str = '-'  # Operator.
            elif rt.v == Type.OpT.MUL:
                op: str = '*'  # Operator.
            elif rt.v == Type.OpT.DIV:
                op: str = '/'  # Operator.
            elif rt.v == Type.OpT.REM:
                op: str = '%'  # Operator.
            elif rt.v == Type.OpT.POW:
                op: str = '^'  # Operator.
            else:
                op: str = '!'  # Operator.

            buf: str = ''  # Buffer for operands.

            if rt.v in [Type.OpT.ADD, Type.OpT.MUL]:
                for tok in rt.chd:
                    if tok.tok_t == Type.TokT.OP and rt.precd[0] > tok.precd[0]:
                        buf += f'({self.__infix_hlpr(tok)}) {op} '
                    else:
                        buf += f'{self.__infix_hlpr(tok)} {op} '

                return buf[:-3]
            elif rt.v in [Type.OpT.SUB, Type.OpT.DIV, Type.OpT.REM]:
                assert len(rt.chd) == 2

                if rt.chd[0].tok_t == Type.TokT.OP and rt.precd[0] > rt.chd[0].precd[0]:
                    buf = f'({self.__infix_hlpr(rt.chd[0])}) {op} '
                else:
                    buf = f'{self.__infix_hlpr(rt.chd[0])} {op} '

                if rt.chd[1].tok_t == Type.TokT.OP and rt.precd[0] >= rt.chd[1].precd[0]:
                    buf += f'({self.__infix_hlpr(rt.chd[1])})'
                else:
                    buf += self.__infix_hlpr(rt.chd[1])

                return buf
            elif rt.v == Type.OpT.POW:
                assert len(rt.chd) == 2

                if rt.chd[0].tok_t == Type.TokT.OP and rt.precd[0] >= rt.chd[0].precd[0]:
                    buf = f'({self.__infix_hlpr(rt.chd[0])}){op}'
                else:
                    buf = f'{self.__infix_hlpr(rt.chd[0])}{op}'

                if rt.chd[1].tok_t == Type.TokT.OP and rt.precd[0] > rt.chd[1].precd[0]:
                    buf += f'({self.__infix_hlpr(rt.chd[1])})'
                else:
                    buf += self.__infix_hlpr(rt.chd[1])

                return buf
            elif rt.v == Type.OpT.FACT:
                assert len(rt.chd) == 1

                if rt.chd[0].tok_t == Type.TokT.OP and rt.precd[0] > rt.chd[0].precd[0]:
                    return f'({self.__infix_hlpr(rt.chd[0])})!'
                else:
                    return f'{self.__infix_hlpr(rt.chd[0])}!'
            else:
                assert len(rt.chd) == 1

                if rt.chd[0].tok_t == Type.TokT.OP and rt.precd[0] > rt.chd[0].precd[0]:
                    return f'{op}({self.__infix_hlpr(rt.chd[0])})'
                else:
                    return op + self.__infix_hlpr(rt.chd[0])
        elif rt.tok_t in [Type.TokT.FUN, Type.TokT.CMD]:
            assert len(rt.chd) == rt.argc

            buf: str = f'{str(rt.v).capitalize()}['  # Buffer for output.
            buf += ', '.join([self.__infix_hlpr(tok) for tok in rt.chd])

            return f'{buf}]'
        else:
            return ''

    def __postfix_hlpr(self, rt) -> str:
        """
        Generate postfix expression of partial AST.

        For construction, it uses postfix traversal of AST.
        For the concept and implementation of postfix traversal, consult the references below.

        This method is private and called internally as a helper of ``AST.__postfix``.

        **Reference**
            * https://en.wikipedia.org/wiki/Tree_traversal#Post-order_(LRN)
            * https://en.wikipedia.org/wiki/Binary_expression_tree#Postfix_traversal

        :param rt: Root of partial AST whose postfix expression is to be generated.
        :type rt: Token.Tok

        :return: Postfix expression.
        :rtype: str
        """
        # In postfix expression, there is no need of parenthesis, which makes the logic pretty simple.
        if rt.tok_t in [Type.TokT.NUM, Type.TokT.VAR]:
            return str(rt.v)
        elif rt.tok_t == Type.TokT.STR:
            return f'\"{rt.v}\"'
        elif rt.tok_t == Type.TokT.OP:
            buf: str = ''  # Buffer for output.

            for tok in rt.chd:
                buf += f'{self.__postfix_hlpr(tok)} '

            if rt.v in [Type.OpT.ADD, Type.OpT.PLUS]:
                return f'{buf}+'
            elif rt.v in [Type.OpT.SUB, Type.OpT.MINUS]:
                return f'{buf}-'
            elif rt.v == Type.OpT.MUL:
                return f'{buf}*'
            elif rt.v == Type.OpT.DIV:
                return f'{buf}/'
            elif rt.v == Type.OpT.REM:
                return f'{buf}%'
            elif rt.v == Type.OpT.POW:
                return f'{buf}^'
            else:
                return f'{buf}!'
        else:
            if rt.chd:
                buf: str = ' '.join([self.__postfix_hlpr(tok) for tok in rt.chd])  # Buffer for output.

                return f'{buf} {str(rt.v).capitalize()}'
            else:
                return str(rt.v).capitalize()

    def __prefix_hlpr(self, rt) -> str:
        """
       Generate postfix expression of partial AST.

        For construction, it uses prefix traversal of AST.
        For the concept and implementation of prefix traversal, consult the references below.

        This method is private and called internally as a helper of ``AST.__prefix``.

        **Reference**
            * https://en.wikipedia.org/wiki/Tree_traversal#Pre-order_(NLR)
            * https://en.wikipedia.org/wiki/Binary_expression_tree#Prefix_traversal

        :param rt: Root of partial AST whose prefix expression is to be generated.
        :type rt: Token.Tok

        :return: Prefix expression.
        :rtype: str
        """
        # In prefix expression, there is no need of parenthesis, which makes the logic pretty simple.
        if rt.tok_t in [Type.TokT.NUM, Type.TokT.VAR]:
            return str(rt.v)
        elif rt.tok_t == Type.TokT.STR:
            return f'\"{rt.v}\"'
        elif rt.tok_t == Type.TokT.OP:
            if rt.v in [Type.OpT.ADD, Type.OpT.PLUS]:
                buf: str = '+'  # Buffer for output.
            elif rt.v in [Type.OpT.SUB, Type.OpT.MINUS]:
                buf: str = '-'  # Buffer for output.
            elif rt.v == Type.OpT.MUL:
                buf: str = '*'  # Buffer for output.
            elif rt.v == Type.OpT.DIV:
                buf: str = '/'  # Buffer for output.
            elif rt.v == Type.OpT.REM:
                buf: str = '%'  # Buffer for output.
            elif rt.v == Type.OpT.POW:
                buf: str = '^'  # Buffer for output.
            else:
                buf: str = '!'  # Buffer for output.

            for tok in rt.chd:
                buf += f' {self.__postfix_hlpr(tok)}'

            return buf
        else:
            buf: str = f'{str(rt.v).capitalize()} '  # Buffer for output.

            if rt.chd:
                buf += ' '.join([self.__prefix_hlpr(tok) for tok in rt.chd])

            return buf

    @classmethod
    def find_var(cls, k: int) -> str:
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

    def infix(self) -> str:
        """
        Generate infix expression of AST.

        It just calls its helper ``AST.__infix_hlpr``.
        For detailed description of infix expression generation, refer to the comments in ``AST.__infix_hlpr``.

        :return: Infix expression.
        :rtype: str
        """
        return self.__infix_hlpr(self.__rt)

    def postfix(self) -> str:
        """
        Generate postfix expression of AST.

        It just calls its helper ``AST.__postfix_hlpr``.
        For detailed description of postfix expression generation, refer to the comments in ``AST.__postfix_hlpr``.

        :return: Postfix expression.
        :rtype: str
        """
        return self.__postfix_hlpr(self.__rt)

    def prefix(self) -> str:
        """
        Generate prefix expression of AST.

        It just calls its helper ``AST.__prefix_hlpr``.
        For detailed description of prefix expression generation, refer to the comments in ``AST.__prefix_hlpr``.

        :return: Prefix expression.
        :rtype: str
        """
        return self.__prefix_hlpr(self.__rt)
