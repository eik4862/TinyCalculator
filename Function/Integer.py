from typing import final

from Function import Function


class IntFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Ceil(IntFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Floor(IntFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Round(IntFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class IntPart(IntFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class IntPart(IntFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class FracPart(IntFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Abs(IntFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Sgn(IntFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
