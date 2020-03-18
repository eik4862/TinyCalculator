from typing import final, Tuple

from Error import Error
from Operator import *


@final
class EmptyExpr(Error.ParserErr):
    def __init__(self, errno: int) -> None:
        super().__init__(errno)


@final
class InvalidTok(Error.ParserErr):
    def __init__(self, errno: int, line: str, pos: int) -> None:
        super().__init__(errno)
        self.__line: str = line
        self.__pos: int = pos

    @property
    def line(self) -> str:
        return self.__line

    @property
    def pos(self) -> int:
        return self.__pos


@final
class InvalidExpr(Error.ParserErr):
    def __init__(self, errno: int, line: str, pos: int, err_op: Tuple[Operator.Op, Operator.Op] = None) -> None:
        super().__init__(errno)
        self.__line: str = line
        self.__pos: int = pos
        self.__err_op: Tuple[Operator.Op, Operator.Op] = err_op

    @property
    def line(self) -> str:
        return self.__line

    @property
    def pos(self) -> int:
        return self.__pos

    @property
    def err_op(self) -> Tuple[Operator.Op, Operator.Op]:
        """
        Getter for pair of erroneous operators.

        :return: Pair of erroneous operators.
        :rtype: Tuple[Operator.Op, Operator.Op]
        """
        return self.__err_op
