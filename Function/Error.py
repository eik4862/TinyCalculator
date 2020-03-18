from typing import final

from Function import Function


class ErrorFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Erf(ErrorFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Erfc(ErrorFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
