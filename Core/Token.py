from sys import maxsize
from typing import List, Tuple, final, Union

from Core import Type, AST


class Tok:
    """
    Token class.

    :ivar __tok_t: Token type.
    :ivar __v: Value of token. (Default: None)
    :ivar __pos: Position in the raw input string where token is derived. (Default: None)
    :ivar __t: Type information for type checking.
    """

    def __init__(self, tok_t: Type.TokT, v: Union[float, int, str, Type.OpT, Type.CmdT, Type.DelimT, Type.FunT] = None,
                 pos: int = None) -> None:
        self.__tok_t: Type.TokT = tok_t
        self.__v: Union[float, int, str, Type.OpT, Type.CmdT, Type.DelimT, Type.FunT] = v
        self.__pos: int = pos
        self.__t: Type.T = None

    def __del__(self) -> None:
        pass

    @property
    def tok_t(self) -> Type.TokT:
        """
        Getter for token type.

        :return: Token type.
        :rtype: Type.TokT
        """
        return self.__tok_t

    @property
    def v(self) -> Union[float, int, str, Type.OpT, Type.CmdT, Type.DelimT]:
        """
        Getter for the value of token.
        Value of void token is `none`.

        :return: Token value.
        :rtype: Union[float, int, str, Type.OpType, Type.CmdType, Type.DelimType]
        """
        return self.__v

    @property
    def pos(self) -> int:
        """
        Getter for the position in the raw input string where token is derived.

        :return: The position where token is derived.
        :rtype: int
        """
        return self.__pos

    @property
    def t(self) -> Type.T:
        """
        Getter for type information for type checking.

        :return: Type information.
        :rtype: Type.T
        """
        return self.__t

    @v.setter
    def v(self, v: Union[float, int, str, Type.OpT, Type.CmdT, Type.DelimT]) -> None:
        """
        Setter for token value.

        :param v: Token value to be set.
        :type v: Union[float, int, str, Type.OpType, Type.CmdType, Type.DelimType]
        """
        self.__v = v

    @t.setter
    def t(self, type: Type.T) -> None:
        """
        Setter for type information.

        :param type: Type information to be set.
        :type type: Type.T
        """
        self.__t = type


@final
class NumTok(Tok):
    """
    Numeric token class.
    """

    def __init__(self, v: float, pos: int = None) -> None:
        super().__init__(Type.TokT.NUM, v, pos)

    def __del__(self) -> None:
        pass


@final
class OpTok(Tok):
    """
    Operator token class.

    :ivar __chd: List of children tokens.
    :ivar __precd: Tuple of inner and outer precedence.
    """

    def __init__(self, v: Type.OpT, pos: int = None) -> None:
        super().__init__(Type.TokT.OP, v, pos)
        self.__chd: List[Tok] = []

        # DO NOT MODIFY!
        # These precedences are delicately chosen so that it accounts for precedence and association rules b/w
        # operators.
        if v in [Type.OpT.ADD, Type.OpT.SUB]:
            self.__precd: Tuple[int, int] = (2, 1)
        elif v in [Type.OpT.MUL, Type.OpT.DIV, Type.OpT.REM]:
            self.__precd: Tuple[int, int] = (4, 3)
        elif v == Type.OpT.POW:
            self.__precd: Tuple[int, int] = (5, 6)
        elif v == Type.OpT.FACT:
            self.__precd: Tuple[int, int] = (7, 8)
        elif v in [Type.OpT.LPAR, Type.OpT.RPAR]:
            self.__precd: Tuple[int, int] = (0, maxsize)
        else:
            self.__precd: Tuple[int, int] = (9, 10)

    def __del__(self) -> None:
        pass

    @property
    def precd(self) -> Tuple[int, int]:
        """
        Getter for precedence information.

        :return: Precedence information.
        :rtype: Tuple[int, int]
        """
        return self.__precd

    @property
    def chd(self) -> List[Tok]:
        """
        Getter for child list.

        :return: Child list.
        :rtype: List[Tok]
        """
        return self.__chd

    @Tok.v.setter
    def v(self, v: Type.OpT) -> None:
        """
        Setter for token value.
        It automatically update precedence information for new value.

        This method overrides the `Token.val` setter in base class.

        :param v: Value of token to be set.
        :type v: Type.OpT
        """
        Tok.v.fset(self, v)

        if v in [Type.OpT.ADD, Type.OpT.SUB]:
            self.__precd = (2, 1)
        elif v in [Type.OpT.MUL, Type.OpT.DIV, Type.OpT.REM]:
            self.__precd = (4, 3)
        elif v == Type.OpT.POW:
            self.__precd = (5, 6)
        elif v == Type.OpT.FACT:
            self.__precd = (7, 8)
        elif v in [Type.OpT.LPAR, Type.OpT.RPAR]:
            self.__precd = (0, maxsize)
        else:
            self.__precd = (9, 10)

    @chd.setter
    def chd(self, child: List[Tok]) -> None:
        """
        Setter for child list.

        :param child: Child list to be set.
        :type: List[Token]
        """
        self.__chd = child

    def add_chd(self, tok: Tok) -> None:
        """
        Append child to the child list.

        :param tok: Child to be appended.
        :type tok: Tok
        """
        self.__chd.append(tok)

    def swap_chd(self, tok: Tok, idx: int) -> None:
        """
        Replace child at specific position in child list.

        :param tok: New token to be replaced with.
        :type tok: Tok
        :param idx: Position in child list to be replaced.
        :type idx: int
        """
        self.__chd[idx] = tok

    def del_chd(self, idx: int) -> None:
        """
        Delete child at specific position in child list.

        :param idx: Position in child list to be deleted.
        :type idx: int
        """
        del self.__chd[idx]


class VarTok(Tok):
    """
    Variable token class.
    """

    def __init__(self, v: int, pos: int = None) -> None:
        super().__init__(Type.TokT.VAR, v, pos)

    def __del__(self) -> None:
        pass

    @property
    def v(self) -> str:
        """
        Getter for the value of token.

        Note that variable token stores hashed value of variable, not variable itself for optimization.
        Thus it first look up hash table to restore original value.

        This method overrides the `Token.val` setter in base class.

        :return: Token value.
        :rtype: str
        """
        return AST.AST.find_var(super().v)


class FunTok(Tok):
    """
    Function token class.

    :ivar __chd: Child list.
    :ivar __precd: Precedence information.
    :ivar __argc: # of arguments.
    """

    def __init__(self, v: Type.FunT, pos: int = None) -> None:
        super().__init__(Type.TokT.FUN, v, pos)
        self.__chd: List[Tok] = []
        self.__precd: Tuple[int, int] = (0, maxsize)
        self.__argc: int = 0

    def __del__(self) -> None:
        pass

    @property
    def precd(self) -> Tuple[int, int]:
        """
        Getter for precedence information.

        :return: Precedence information.
        :rtype: Tuple[int, int]
        """
        return self.__precd

    @property
    def argc(self) -> int:
        """
        Getter for argument #.

        :return: Argument #.
        :rtype: int
        """
        return self.__argc

    @property
    def chd(self) -> List[Tok]:
        """
        Getter for child list.

        :return: Child list.
        :rtype: List[Tok]
        """
        return self.__chd

    @argc.setter
    def argc(self, argc: int) -> None:
        """
        Setter for argument #.

        :param argc: The # of arguments to be set.
        :type argc: int
        """
        self.__argc = argc

    @chd.setter
    def chd(self, child: List[Tok]) -> None:
        """
        Setter for child list.

        :param child: Child list to be set.
        :type: List[Token]
        """
        self.__chd = child

    def add_chd(self, tok: Tok) -> None:
        """
        Append child to the child list.

        :param tok: Child to be appended.
        :type tok: Tok
        """
        self.__chd.append(tok)

    def swap_chd(self, tok: Tok, idx: int) -> None:
        """
        Set child at specific position in child list.

        :param tok: Token to be set as children.
        :type tok: Tok
        :param idx: Position in child list to be set.
        :type idx: int
        """
        self.__chd[idx] = tok


class DelimTok(Tok):
    """
    Delimiter token class.

    :ivar __precd: Precedence information.
    """

    def __init__(self, v: Type.DelimT, pos: int = None) -> None:
        super().__init__(Type.TokT.DELIM, v, pos)
        self.__precd: Tuple[int, int] = (0, maxsize)

    def __del__(self) -> None:
        pass

    @property
    def precd(self) -> Tuple[int, int]:
        """
        Getter for precedence information.

        :return: Precedence information.
        :rtype: Tuple[int, int]
        """
        return self.__precd


class CmdTok(Tok):
    """
    Command token class.

    :ivar __chd: Child list.
    :ivar __precd: Precedence information.
    :ivar __argc: # of arguments.
    """

    def __init__(self, v: Type.CmdT, pos: int = None) -> None:
        super().__init__(Type.TokT.CMD, v, pos)
        self.__chd: List[Tok] = []
        self.__precd: Tuple[int, int] = (0, maxsize)
        self.__argc: int = 0

    def __del__(self) -> None:
        pass

    @property
    def precd(self) -> Tuple[int, int]:
        """
        Getter for precedence information.

        :return: Precedence information.
        :rtype: Tuple[int, int]
        """
        return self.__precd

    @property
    def argc(self) -> int:
        """
        Getter for argument #.

        :return: Argument #.
        :rtype: int
        """
        return self.__argc

    @property
    def chd(self) -> List[Tok]:
        """
         Getter for child list.

         :return: Child list.
         :rtype: List[Tok]
         """
        return self.__chd

    @argc.setter
    def argc(self, argc: int) -> None:
        """
        Setter for argument #.

        :param argc: The # of arguments to be set.
        :type argc: int
        """
        self.__argc = argc

    @chd.setter
    def chd(self, child: List[Tok]) -> None:
        """
        Setter for child list.

        :param child: Child list to be set.
        :type: List[Token]
        """
        self.__chd = child

    def add_chd(self, tok: Tok) -> None:
        """
        Append child to the child list.

        :param tok: Child to be appended.
        :type tok: Tok
        """
        self.__chd.append(tok)

    def swap_chd(self, tok: Tok, idx: int) -> None:
        """
        Replace child at specific position in child list.

        :param tok: New token to be replaced with.
        :type tok: Tok
        :param idx: Position in child list to be replaced.
        :type idx: int
        """
        self.__chd[idx] = tok


class StrTok(Tok):
    """
    String token class.
    """

    def __init__(self, v: str, pos: int = None) -> None:
        super().__init__(Type.TokT.STR, v, pos)

    def __del__(self) -> None:
        pass


class VoidTok(Tok):
    """
    Void token class.
    """

    def __init__(self, pos: int = None) -> None:
        super().__init__(Type.TokT.VOID, pos=pos)

    def __del__(self) -> None:
        pass
