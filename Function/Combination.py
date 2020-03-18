from __future__ import annotations

from typing import final, Dict, Optional

from Core import Token, TypeSystem
from Function import Function


class CombFun(Function.Fun):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError

    @classmethod
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t1: TypeSystem.T = rt.chd[0].t

        if t1.base:
            if type(t1) == TypeSystem.Sym:
                rt.t = t1
            elif type(t1) == TypeSystem.Real:
                rt.t = TypeSystem.Real
            else:
                return None
        else:
            return None

        return t_env


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
