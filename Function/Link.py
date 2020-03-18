from typing import final

from Function import Function


class LinkFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Logit(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Reciprocal(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class InverseSquare(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Probit(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Cauchit(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class LogLog(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class LogComplement(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class LogLogComplement(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class OddsPower(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class NegBinomLink(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class PowerLink(LinkFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
