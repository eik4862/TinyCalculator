from typing import final, Final, List

from Function import Function


class SigFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Ramp(SigFun):
    __SGN: Final[List[str]] = ['Ramp[Real] -> Real', 'Ramp[Sym] -> Sym']

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Unitize(SigFun):
    __SGN: Final[List[str]] = ['Unitize[Real] -> Real',
                               'Unitize[Sym] -> Sym',
                               'Unitize[Real, Real] -> Real',
                               'Unitize[Sym, Sym] -> Sym']

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Logistic(SigFun):
    __SGN: Final[List[str]] = ['Logistic[Real] -> Real', 'Logistic[Sym] -> Sym']

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class SquareWave(SigFun):
    __SGN: Final[List[str]] = ['SquareWave[Real, Real (Optional), Real (Optional)] -> Real',
                               'SquareWave[Sym, Sym (Optional), Sym (Optional)] -> Sym']

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class TriangleWave(SigFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class SawtoothWave(SigFun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError
