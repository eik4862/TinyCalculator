from typing import final

from Function import Function


class CombFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Factorial(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class DoubleFactorial(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Pochhammer(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Binom(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Multinom(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Subfactorial(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class FacotirlaPower(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class AlternatingFactorial(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class CatalanNum(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class PolygonNum(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Bell(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Fibonacci(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Lucas(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Harmonic(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Stirling1(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Stiling2(CombFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
