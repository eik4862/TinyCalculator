from typing import final

from Function import Function


class GammaFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Gamma(GammaFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class LogGamma(GammaFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Beta(GammaFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
