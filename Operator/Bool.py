from __future__ import annotations

from typing import final, Final, Tuple, Dict, Optional, List

from Core import Token, TypeSystem
from Operator import Operator


class BoolOp(Operator.Op):
    __ARGC: int = 2

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError

    @classmethod
    def argc(cls) -> int:
        return cls.__ARGC

    @classmethod
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t1: TypeSystem.T = rt.chd[0].t
        t2: TypeSystem.T = rt.chd[1].t

        if t1.base:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if type(res_t) in [TypeSystem.Bool, TypeSystem.Sym]:
                    rt.t = res_t
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2.chd_t)

                if type(res_t) in [TypeSystem.Bool, TypeSystem.Sym]:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t2, res_t)
                else:
                    return None
        else:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1.chd_t, t2)

                if type(res_t) in [TypeSystem.Bool, TypeSystem.Sym]:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, res_t)
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if res_t and type(res_t.chd_t) == TypeSystem.Bool:
                    rt.t = res_t
                else:
                    return None

        return t_env


@final
class Neg(BoolOp):
    __PRECD: Final[Tuple[int, int]] = (19, 20)
    __SYM: Final[str] = '!'
    __SGN: Final[List[str]] = ['!Bool -> Bool',
                               '!Sym -> Sym',
                               '!List of Bool (n fold) -> List of Bool (n fold)']
    __ARGC: Final[int] = 1

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

    @classmethod
    def argc(cls) -> int:
        return cls.__ARGC

    @classmethod
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t: TypeSystem.T = rt.chd[0].t

        if t.base:
            if type(t) not in [TypeSystem.Bool, TypeSystem.Sym]:
                return None
            else:
                rt.t = TypeSystem.Bool.inst()
        else:
            if type(t.chd_t) != TypeSystem.Bool:
                return None
            else:
                rt.t = TypeSystem.Bool.inst()

        return t_env


@final
class And(BoolOp):
    __PRECD: Final[Tuple[int, int]] = (6, 5)
    __SYM: Final[str] = '&'
    __SGN: Final[List[str]] = ['Bool & Bool -> Bool',
                               'Sym & Sym -> Sym',
                               'Bool & List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Bool (n fold) & Bool -> List of Bool (n fold)',
                               'List of Bool (n fold) & List of Bool (n fold) -> List of Bool (n fold)']

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
class Or(BoolOp):
    __PRECD: Final[Tuple[int, int]] = (4, 3)
    __SYM: Final[str] = '|'
    __SGN: Final[List[str]] = ['Bool | Bool -> Bool',
                               'Sym | Sym -> Sym',
                               'Bool | List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Bool (n fold) | Bool -> List of Bool (n fold)',
                               'List of Bool (n fold) | List of Bool (n fold) -> List of Bool (n fold)']

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
class Xor(BoolOp):
    __PRECD: Final[Tuple[int, int]] = (4, 3)
    __SYM: Final[str] = '^'
    __SGN: Final[List[str]] = ['Bool ^ Bool -> Bool',
                               'Sym ^ Sym -> Sym',
                               'Bool ^ List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Bool (n fold) ^ Bool -> List of Bool (n fold)',
                               'List of Bool (n fold) ^ List of Bool (n fold) -> List of Bool (n fold)']

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
