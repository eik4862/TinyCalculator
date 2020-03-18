from typing import final

from Function import Function


class DivFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Mod(DivFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class PowerMod(DivFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Quotient(DivFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
