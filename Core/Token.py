from __future__ import annotations

from typing import List, final, Union, Any, Dict

from Core import AST, TypeSystem, TypeChecker
from Function import *
from Operator import *


class Tok:
    """
    Token class.

    :ivar __v: Value of token. (Default: None)
    :ivar __pos: Position in the raw input string where token is derived. (Default: None)
    """

    def __init__(self, v: Union[int, float, complex, str, bool, Operator.Op, Function.Fun] = None,
                 pos: int = None) -> None:
        self.__v: Union[int, float, complex, str, bool, Operator.Op, Function.Fun] = v
        self.__pos: int = pos
        self.__t: TypeSystem.T = None
        self.__t_var: TypeChecker.TVar = None

    @property
    def v(self) -> Union[int, float, complex, str, bool, Operator.Op, Function.Fun]:
        """
        Getter for the value of token.
        Value of void token is ``none``.

        :return: Token value.
        :rtype: Union[int, float, complex, str, bool, Operator.Op, Function.Fun]
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
    def t(self) -> TypeSystem.T:
        return self.__t

    @property
    def t_var(self) -> TypeChecker.TVar:
        return self.__t_var

    @v.setter
    def v(self, v: Union[int, float, complex, str, bool, Operator.Op, Function.Fun]) -> None:
        """
        Setter for token value.

        :param v: Token value to be set.
        :type v: Union[int, float, complex, str, bool, Operator.Op, Function.Fun]
        """
        self.__v = v

    @t.setter
    def t(self, t: TypeSystem.T) -> None:
        self.__t = t

    @t_var.setter
    def t_var(self, t_var: TypeChecker.TVar) -> None:
        self.__t_var = t_var

    def v_str(self) -> str:
        return str(self.__v)


@final
class Num(Tok):
    """
    Numeric token class.
    """

    def __init__(self, v: Union[int, float, complex], pos: int = None) -> None:
        super().__init__(v, pos)


@final
class Op(Tok):
    """
    Operator token class.

    :ivar __chd: List of children tokens.
    :ivar __argc: # of operands.
    """

    def __init__(self, v: Operator.Op, pos: int = None) -> None:
        super().__init__(v, pos)
        self.__chd: List[Tok] = []
        self.__argc: int = v.argc()

    @property
    def precd_in(self) -> int:
        """
        Getter for inner precedence.

        :return: Inner precedence.
        :rtype: int
        """
        return super().v.precd_in()

    @property
    def precd_out(self) -> int:
        """
       Getter for outer precedence.

       :return: Outer precedence.
       :rtype: int
       """
        return super().v.precd_out()

    @property
    def chd(self) -> List[Tok]:
        """
        Getter for child list.

        :return: Child list.
        :rtype: List[Tok]
        """
        return self.__chd

    @property
    def argc(self) -> int:
        """
        Getter for operand #.

        :return: Operand #.
        :rtype: int
        """
        return self.__argc

    @Tok.v.setter
    def v(self, v: Operator.Op) -> None:
        Tok.v.fset(self, v)
        self.__argc: int = v.argc()

    @chd.setter
    def chd(self, chd: List[Tok]) -> None:
        """
        Setter for child list.

        :param chd: Child list to be set.
        :type: List[Token]
        """
        self.__chd = chd

    @argc.setter
    def argc(self, argc: int) -> None:
        """
        Setter for operand #.

        :param argc: The # of operand to be set.
        :type argc: int
        """
        self.__argc = argc

    def v_str(self) -> str:
        return super().v.__name__.upper()

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


@final
class Var(Tok):
    """
    Variable token class.
    """

    def __init__(self, v: int, pos: int = None) -> None:
        super().__init__(v, pos)

    def __del__(self) -> None:
        pass

    def v_str(self) -> str:
        return AST.AST.var_name(super().v)


@final
class Fun(Tok):
    """
    Function token class.

    :ivar __chd: Child list.
    :ivar __argc: # of arguments.
    """

    def __init__(self, v: Function.Fun, pos: int = None) -> None:
        super().__init__(v, pos)
        self.__chd: List[Tok] = []
        self.__argc: int = 0

    @property
    def precd_in(self) -> int:
        """
        Getter for inner precedence.

        :return: Inner precedence.
        :rtype: int
        """
        return super().v.precd_in()

    @property
    def precd_out(self) -> int:
        """
       Getter for outer precedence.

       :return: Outer precedence.
       :rtype: int
       """
        return super().v.precd_out()

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

    def v_str(self) -> str:
        return super().v.__name__

    @argc.setter
    def argc(self, argc: int) -> None:
        """
        Setter for argument #.

        :param argc: The # of arguments to be set.
        :type argc: int
        """
        self.__argc = argc

    @chd.setter
    def chd(self, chd: List[Tok]) -> None:
        """
        Setter for child list.

        :param chd: Child list to be set.
        :type: List[Token]
        """
        self.__chd = chd

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


@final
class Str(Tok):
    """
    String token class.
    """

    def __init__(self, v: str, pos: int = None) -> None:
        super().__init__(v, pos)

    def v_str(self) -> str:
        v: str = super().v
        buf: str = '"'  # Buffer for unescaped string.
        i: int = 0

        while i < len(v):
            if v[i] == '\\':
                buf += '\\\\'
            elif v[i] == '\n':
                buf += '\\n'
            elif v[i] == '\t':
                buf += '\\t'
            elif v[i] == '"':
                buf += '\\"'
            else:
                buf += v[i]

            i += 1

        return buf + '"'


@final
class Bool(Tok):
    """
    Boolean token class.
    """

    def __init__(self, v: bool, pos: int = None) -> None:
        super().__init__(v, pos)


@final
class List(Tok):
    """
    List token class.

    :ivar __chd: Child list.
    :ivar __argc: # of items.
    """

    def __init__(self, pos: int = None, argc: int = 0) -> None:
        super().__init__(pos=pos)
        self.__chd: List[Tok] = []
        self.__argc: int = argc

    @property
    def argc(self) -> int:
        """
        Getter for the # of items.

        :return: # of items.
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

    def add_chd(self, tok: Tok) -> None:
        """
        Append child to the child list.

        :param tok: Child to be appended.
        :type tok: Tok
        """
        self.__chd.append(tok)


@final
class Void(Tok):
    """
    Void token class.
    """

    def __init__(self) -> None:
        super().__init__()

    def v_str(self) -> str:
        return ''


@final
class Ter(Tok):
    """
    Terminal token class.

    This class is only used as temporarily to check the terminal condition of expression.
    """

    def __init__(self) -> None:
        super().__init__()
