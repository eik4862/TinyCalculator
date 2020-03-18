from typing import final

from Operator import Operator


class DelimOp(Operator.Op):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Lpar(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Rpar(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class SqrLpar(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class SqrRpar(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class CrlLpar(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class CrlRpar(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Com(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Seq(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Idx(DelimOp):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
