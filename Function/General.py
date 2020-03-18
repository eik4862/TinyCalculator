from typing import final

from Function import Function


class GenFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class DiracDelta(GenFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class HeavisideTheta(GenFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class DiracComb(GenFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class HeavisidePi(GenFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class HeavisideLambda(GenFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
