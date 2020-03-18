from __future__ import annotations

from typing import final, Final, Tuple, Dict, Optional, List

from Core import Token, TypeSystem
from Operator import Operator


class BinOp(Operator.Op):
    __ARGC: Final[int] = 2

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

                if type(res_t) in [TypeSystem.Real, TypeSystem.Cmplx, TypeSystem.Sym]:
                    rt.t = res_t
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2.chd_t)

                if type(res_t) in [TypeSystem.Real, TypeSystem.Cmplx, TypeSystem.Sym]:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t2, res_t)
                else:
                    return None
        else:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1.chd_t, t2)

                if type(res_t) in [TypeSystem.Real, TypeSystem.Cmplx, TypeSystem.Sym]:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, res_t)
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if res_t and type(res_t.chd_t) in [TypeSystem.Real, TypeSystem.Cmplx]:
                    rt.t = res_t
                else:
                    return None

        return t_env


@final
class Add(BinOp):
    __PRECD: Final[Tuple[int, int]] = (12, 11)
    __SYM: Final[str] = '+'
    __SGN: Final[List[str]] = ['Real + Real -> Real',
                               'Cmplx + Cmplx -> Cmplx',
                               'Sym + Sym -> Sym',
                               'Real + List of Real (n fold) -> List of Real (n fold)',
                               'Cmplx + List of Cmplx (n fold) -> List of Cmplx (n fold)',
                               'List of Real (n fold) + Real -> List of Real (n fold)',
                               'List of Cmplx (n fold) + Cmplx -> List of Cmplx (n fold)',
                               'List of Real (n fold) + List of Real (n fold) -> List of Real (n fold)',
                               'List of Cmplx (n fold) + List of Cmplx (n fold) -> List of Cmplx (n fold)']

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
class Sub(BinOp):
    __PRECD: Final[Tuple[int, int]] = (12, 11)
    __SYM: Final[str] = '-'
    __SGN: Final[List[str]] = ['Real - Real -> Real',
                               'Cmplx - Cmplx -> Cmplx',
                               'Sym - Sym -> Sym',
                               'Real - List of Real (n fold) -> List of Real (n fold)',
                               'Cmplx - List of Cmplx (n fold) -> List of Cmplx (n fold)',
                               'List of Real (n fold) - Real -> List of Real (n fold)',
                               'List of Cmplx (n fold) - Cmplx -> List of Cmplx (n fold)',
                               'List of Real (n fold) - List of Real (n fold) -> List of Real (n fold)',
                               'List of Cmplx (n fold) - List of Cmplx (n fold) -> List of Cmplx (n fold)']

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
class Mul(BinOp):
    __PRECD: Final[Tuple[int, int]] = (14, 13)
    __SYM: Final[str] = '*'
    __SGN: Final[List[str]] = ['Real * Real -> Real',
                               'Cmplx * Cmplx -> Cmplx',
                               'Sym * Sym -> Sym',
                               'Real * List of Real (n fold) -> List of Real (n fold)',
                               'Cmplx * List of Cmplx (n fold) -> List of Cmplx (n fold)',
                               'List of Real (n fold) * Real -> List of Real (n fold)',
                               'List of Cmplx (n fold) * Cmplx -> List of Cmplx (n fold)',
                               'List of Real (n fold) * List of Real (n fold) -> List of Real (n fold)',
                               'List of Cmplx (n fold) * List of Cmplx (n fold) -> List of Cmplx (n fold)']

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
class MatMul(BinOp):
    __PRECD: Final[Tuple[int, int]] = (14, 13)
    __SYM: Final[str] = '%*%'
    __SGN: Final[List[str]] = ['Sym %*% Sym -> Sym',
                               'List of Real (2 fold) %*% List of Real (n fold) -> List of Real (n fold)       given that n >= 2',
                               'List of Cmplx (2 fold) %*% List of Cmplx (n fold) -> List of Cmplx (n fold)    given that n >= 2',
                               'List of Real (n fold) %*% List of Real (2 fold) -> List of Real (n fold)       given that n > 2',
                               'List of Cmplx (n fold) %*% List of Cmplx (2 fold) -> List of Cmplx (n fold)    given that n > 2',
                               'List of Real (n fold) %*% List of Real (n fold) -> List of Real (n fold)       given that n > 2',
                               'List of Cmplx (n fold) %*% List of Cmplx (n fold) -> List of Cmplx (n fold)    given that n > 2']

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
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t1: TypeSystem.T = rt.chd[0].t
        t2: TypeSystem.T = rt.chd[1].t

        if t1.base:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if type(res_t) == TypeSystem.Sym:
                    rt.t = res_t
                else:
                    return None
            else:
                if type(t1) == TypeSystem.Sym:
                    rt.t = t1
                else:
                    return None
        else:
            if t2.base:
                if type(t2) == TypeSystem.Sym:
                    rt.t = t2
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if res_t and type(res_t.chd_t) in [TypeSystem.Real, TypeSystem.Cmplx]:
                    if t1.fold > 1:
                        rt.t = res_t
                    else:
                        return None
                else:
                    res_t = TypeSystem.T.supt(t1.chd_t, t2.chd_t)

                    if type(res_t) in [TypeSystem.Real, TypeSystem.Cmplx]:
                        if t1.fold == 2 and t2.fold > 2:
                            rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t2, res_t)
                        elif t1.fold > 2 and t2.fold == 2:
                            rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, res_t)
                        else:
                            return None
                    else:
                        return None

        return t_env


@final
class Div(BinOp):
    __PRECD: Final[Tuple[int, int]] = (14, 13)
    __SYM: Final[str] = '/'
    __SGN: Final[List[str]] = ['Real / Real -> Real',
                               'Cmplx / Cmplx -> Cmplx',
                               'Sym / Sym -> Sym',
                               'Real / List of Real (n fold) -> List of Real (n fold)',
                               'Cmplx / List of Cmplx (n fold) -> List of Cmplx (n fold)',
                               'List of Real (n fold) / Real -> List of Real (n fold)',
                               'List of Cmplx (n fold) / Cmplx -> List of Cmplx (n fold)',
                               'List of Real (n fold) / List of Real (n fold) -> List of Real (n fold)',
                               'List of Cmplx (n fold) / List of Cmplx (n fold) -> List of Cmplx (n fold)']

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
class Rem(BinOp):
    __PRECD: Final[Tuple[int, int]] = (14, 13)
    __SYM: Final[str] = '%'
    __SGN: Final[List[str]] = ['Real % Real -> Real',
                               'Sym % Sym -> Sym',
                               'Real % List of Real (n fold) -> List of Real (n fold)',
                               'List of Real (n fold) % Real -> List of Real (n fold)',
                               'List of Real (n fold) % List of Real (n fold) -> List of Real (n fold)']

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
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t1: TypeSystem.T = rt.chd[0].t
        t2: TypeSystem.T = rt.chd[1].t

        if t1.base:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if type(res_t) in [TypeSystem.Real, TypeSystem.Sym]:
                    rt.t = res_t
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2.chd_t)

                if type(res_t) in [TypeSystem.Real, TypeSystem.Sym]:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t2, res_t)
                else:
                    return None
        else:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1.chd_t, t2)

                if type(res_t) in [TypeSystem.Real, TypeSystem.Sym]:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, res_t)
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if res_t and type(res_t.chd_t) == TypeSystem.Real:
                    rt.t = res_t
                else:
                    return None

        return t_env


@final
class Quot(BinOp):
    __PRECD: Final[Tuple[int, int]] = (14, 13)
    __SYM: Final[str] = '//'
    __SGN: Final[List[str]] = ['Real // Real -> Real',
                               'Sym // Sym -> Sym',
                               'Real // List of Real (n fold) -> List of Real (n fold)',
                               'List of Real (n fold) // Real -> List of Real (n fold)',
                               'List of Real (n fold) // List of Real (n fold) -> List of Real (n fold)']

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
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t1: TypeSystem.T = rt.chd[0].t
        t2: TypeSystem.T = rt.chd[1].t

        if t1.base:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if type(res_t) in [TypeSystem.Real, TypeSystem.Sym]:
                    rt.t = res_t
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2.chd_t)

                if type(res_t) in [TypeSystem.Real, TypeSystem.Sym]:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t2, res_t)
                else:
                    return None
        else:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1.chd_t, t2)

                if type(res_t) in [TypeSystem.Real, TypeSystem.Sym]:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, res_t)
                else:
                    return None
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if res_t and type(res_t.chd_t) == TypeSystem.Real:
                    rt.t = res_t
                else:
                    return None

        return t_env


@final
class Pow(BinOp):
    __PRECD: Final[Tuple[int, int]] = (17, 18)
    __SYM: Final[str] = '**'
    __SGN: Final[List[str]] = ['Real ** Real -> Real',
                               'Cmplx ** Cmplx -> Cmplx',
                               'Sym ** Sym -> Sym',
                               'Real ** List of Real (n fold) -> List of Real (n fold)',
                               'Cmplx ** List of Cmplx (n fold) -> List of Cmplx (n fold)',
                               'List of Real (n fold) ** Real -> List of Real (n fold)',
                               'List of Cmplx (n fold) ** Cmplx -> List of Cmplx (n fold)',
                               'List of Real (n fold) ** List of Real (n fold) -> List of Real (n fold)',
                               'List of Cmplx (n fold) ** List of Cmplx (n fold) -> List of Cmplx (n fold)']

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
