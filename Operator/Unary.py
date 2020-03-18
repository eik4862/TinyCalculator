from __future__ import annotations

from typing import final, Final, Tuple, Dict, Optional, List

from Core import TypeSystem, Token
from Operator import Operator


class UniOp(Operator.Op):
    __ARGC: Final[int] = 1

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError

    @classmethod
    def argc(cls) -> int:
        return cls.__ARGC

    @classmethod
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t: TypeSystem.T = rt.chd[0].t

        if t.base:
            if type(t) in [TypeSystem.Real, TypeSystem.Cmplx, TypeSystem.Sym]:
                rt.t = t

                return t_env
            else:
                return None
        else:
            if type(t.chd_t) in [TypeSystem.Real, TypeSystem.Cmplx]:
                rt.t = t

                return t_env
            else:
                return None


@final
class Plus(UniOp):
    __PRECD: Final[Tuple[int, int]] = (19, 20)
    __SYM: Final[str] = '+'
    __SGN: Final[List[str]] = ['+Real -> Real',
                               '+Cmplx -> Cmplx',
                               '+Sym -> Sym',
                               '+List of Real (n fold) -> List of Real (n fold)'
                               '+List of Cmplx (n fold) -> List of Cmplx (n fold)']

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError

    @classmethod
    def precd_in(cls) -> int:
        return cls.__PRECD[0]

    @classmethod
    def precd_out(cls) -> int:
        return cls.__PRECD[1]

    @classmethod
    def sym(cls) -> str:
        return cls.__SYM

    @classmethod
    def sgn(cls) -> List[str]:
        return cls.__SGN


@final
class Minus(UniOp):
    __PRECD: Final[Tuple[int, int]] = (19, 20)
    __SYM: Final[str] = '-'
    __SGN: Final[List[str]] = ['-Real -> Real',
                               '-Cmplx -> Cmplx',
                               '-Sym -> Sym',
                               '-List of Real (n fold) -> List of Real (n fold)'
                               '-List of Cmplx (n fold) -> List of Cmplx (n fold)']

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError

    @classmethod
    def precd_in(cls) -> int:
        return cls.__PRECD[0]

    @classmethod
    def precd_out(cls) -> int:
        return cls.__PRECD[1]

    @classmethod
    def sym(cls) -> str:
        return cls.__SYM

    @classmethod
    def sgn(cls) -> List[str]:
        return cls.__SGN


@final
class Trans(UniOp):
    __PRECD: Final[Tuple[int, int]] = (24, 23)
    __SYM: Final[str] = '\''
    __SGN: Final[List[str]] = ['Sym\' -> Sym',
                               'List of Real (n fold)\' -> List of Real (n fold) given that n >= 2',
                               'List of Cmplx (n fold)\' -> List of Cmplx (n fold) given that n >= 2',
                               'List of Str (n fold)\' -> List of Str (n fold)',
                               'List of Bool (n fold)\' -> List of Bool (n fold)']

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError

    @classmethod
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t: TypeSystem.T = rt.chd[0].t

        if t.base:
            if type(t) == TypeSystem.Sym:
                rt.t = t

                return t_env
            else:
                return None
        else:
            if type(t.chd_t) == TypeSystem.Void or t.fold == 1:
                return None
            else:
                rt.t = t

                return t_env

    @classmethod
    def precd_in(cls) -> int:
        return cls.__PRECD[0]

    @classmethod
    def precd_out(cls) -> int:
        return cls.__PRECD[1]

    @classmethod
    def sym(cls) -> str:
        return cls.__SYM

    @classmethod
    def sgn(cls) -> List[str]:
        return cls.__SGN
