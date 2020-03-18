from __future__ import annotations

from typing import final, Final, Tuple, Dict, Optional, List

from Core import Token, TypeSystem
from Operator import Operator


class CompOp(Operator.Op):
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

                if not res_t or type(res_t) in [TypeSystem.Cmplx, TypeSystem.Void]:
                    return None
                elif type(res_t) == TypeSystem.Sym:
                    rt.t = res_t
                else:
                    rt.t = TypeSystem.Bool.inst()
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2.chd_t)

                if not res_t or type(res_t) in [TypeSystem.Cmplx, TypeSystem.Void]:
                    return None
                elif type(res_t) == TypeSystem.Sym:
                    rt.t = res_t
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t2, TypeSystem.Bool.inst())
        else:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1.chd_t, t2)

                if not res_t or type(res_t) in [TypeSystem.Cmplx, TypeSystem.Void]:
                    return None
                elif type(res_t) == TypeSystem.Sym:
                    rt.t = res_t
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, TypeSystem.Bool.inst())
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if not res_t or type(res_t.chd_t) in [TypeSystem.Cmplx, TypeSystem.Void]:
                    return None
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, TypeSystem.Bool.inst())

        return t_env


@final
class Eq(CompOp):
    __PRECD: Final[Tuple[int, int]] = (8, 7)
    __SYM: Final[str] = '=='
    __SGN: Final[List[str]] = ['Real == Real -> Bool',
                               'Cmplx == Cmplx -> Bool',
                               'Str == Str -> Bool',
                               'Bool == Bool -> Bool',
                               'Sym == Sym -> Bool',
                               'Real == List of Real (n fold) -> List of Bool (n fold)',
                               'Cmplx == List of Cmplx (n fold) -> List of Bool (n fold)',
                               'Str == List of Str (n fold) -> List of Bool (n fold)',
                               'Bool == List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Real (n fold) == Real -> List of Bool (n fold)',
                               'List of Cmplx (n fold) == Cmplx -> List of Bool (n fold)',
                               'List of Str (n fold) == Str -> List of Bool (n fold)',
                               'List of Bool (n fold) == Bool -> List of Bool (n fold)',
                               'List of Real (n fold) == List of Real (n fold) -> List of Bool (n fold)',
                               'List of Cmplx (n fold) == List of Cmplx (n fold) -> List of Bool (n fold)',
                               'List of Str (n fold) == List of Str (n fold) -> List of Bool (n fold)',
                               'List of Bool (n fold) == List of Bool (n fold) -> List of Bool (n fold)']

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

                if not res_t or type(res_t) == TypeSystem.Void:
                    return None
                else:
                    rt.t = TypeSystem.Bool.inst()
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2.chd_t)

                if not res_t or type(res_t) == TypeSystem.Void:
                    return None
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t2, TypeSystem.Bool.inst())
        else:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1.chd_t, t2)

                if not res_t or type(res_t) == TypeSystem.Void:
                    return None
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, TypeSystem.Bool.inst())
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if not res_t or type(res_t.chd_t) == TypeSystem.Void:
                    return None
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, TypeSystem.Bool.inst())

        return t_env


@final
class Diff(CompOp):
    __PRECD: Final[Tuple[int, int]] = (8, 7)
    __SYM: Final[str] = '!='
    __SGN: Final[List[str]] = ['Real == Real -> Bool',
                               'Cmplx == Cmplx -> Bool',
                               'Str == Str -> Bool',
                               'Bool == Bool -> Bool',
                               'Sym == Sym -> Sym',
                               'Real == List of Real (n fold) -> List of Bool (n fold)',
                               'Cmplx == List of Cmplx (n fold) -> List of Bool (n fold)',
                               'Str == List of Str (n fold) -> List of Bool (n fold)',
                               'Bool == List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Real (n fold) == Real -> List of Bool (n fold)',
                               'List of Cmplx (n fold) == Cmplx -> List of Bool (n fold)',
                               'List of Str (n fold) == Str -> List of Bool (n fold)',
                               'List of Bool (n fold) == Bool -> List of Bool (n fold)',
                               'List of Real (n fold) == List of Real (n fold) -> List of Bool (n fold)',
                               'List of Cmplx (n fold) == List of Cmplx (n fold) -> List of Bool (n fold)',
                               'List of Str (n fold) == List of Str (n fold) -> List of Bool (n fold)',
                               'List of Bool (n fold) == List of Bool (n fold) -> List of Bool (n fold)']

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

                if not res_t or type(res_t) == TypeSystem.Void:
                    return None
                else:
                    rt.t = TypeSystem.Bool.inst()
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2.chd_t)

                if not res_t or type(res_t) == TypeSystem.Void:
                    return None
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t2, TypeSystem.Bool.inst())
        else:
            if t2.base:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1.chd_t, t2)

                if not res_t or type(res_t) == TypeSystem.Void:
                    return None
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, TypeSystem.Bool.inst())
            else:
                res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

                if not res_t.chd_t or type(res_t.chd_t) == TypeSystem.Void:
                    return None
                else:
                    rt.t = TypeSystem.ArrFact.inst().coerce_arr_t(t1, TypeSystem.Bool.inst())

        return t_env


@final
class Abv(CompOp):
    __PRECD: Final[Tuple[int, int]] = (10, 9)
    __SYM: Final[str] = '<'
    __SGN: Final[List[str]] = ['Real < Real -> Bool',
                               'Str < Str -> Bool',
                               'Bool < Bool -> Bool',
                               'Sym < Sym -> Sym',
                               'Real < List of Real (n fold) -> List of Bool (n fold)',
                               'Str < List of Str (n fold) -> List of Bool (n fold)',
                               'Bool < List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Real (n fold) < Real -> List of Bool (n fold)',
                               'List of Str (n fold) < Str -> List of Bool (n fold)',
                               'List of Bool (n fold) < Bool -> List of Bool (n fold)',
                               'List of Real (n fold) < List of Real (n fold) -> List of Bool (n fold)',
                               'List of Str (n fold) < List of Str (n fold) -> List of Str (n fold)',
                               'List of Bool (n fold) < List of Bool (n fold) -> List of Bool (n fold)']

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
class Blw(CompOp):
    __PRECD: Final[Tuple[int, int]] = (10, 9)
    __SYM: Final[str] = '>'
    __SGN: Final[List[str]] = ['Real > Real -> Bool',
                               'Str > Str -> Bool',
                               'Bool > Bool -> Bool',
                               'Sym > Sym -> Sym',
                               'Real > List of Real (n fold) -> List of Bool (n fold)',
                               'Str > List of Str (n fold) -> List of Bool (n fold)',
                               'Bool > List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Real (n fold) > Real -> List of Bool (n fold)',
                               'List of Str (n fold) > Str -> List of Bool (n fold)',
                               'List of Bool (n fold) > Bool -> List of Bool (n fold)',
                               'List of Real (n fold) > List of Real (n fold) -> List of Bool (n fold)',
                               'List of Str (n fold) > List of Str (n fold) -> List of Str (n fold)',
                               'List of Bool (n fold) > List of Bool (n fold) -> List of Bool (n fold)']

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
class Geq(CompOp):
    __PRECD: Final[Tuple[int, int]] = (10, 9)
    __SYM: Final[str] = '<='
    __SGN: Final[List[str]] = ['Real <= Real -> Bool',
                               'Str <= Str -> Bool',
                               'Bool <= Bool -> Bool',
                               'Sym <= Sym -> Sym',
                               'Real <= List of Real (n fold) -> List of Bool (n fold)',
                               'Str <= List of Str (n fold) -> List of Bool (n fold)',
                               'Bool <= List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Real (n fold) <= Real -> List of Bool (n fold)',
                               'List of Str (n fold) <= Str -> List of Bool (n fold)',
                               'List of Bool (n fold) <= Bool -> List of Bool (n fold)',
                               'List of Real (n fold) <= List of Real (n fold) -> List of Bool (n fold)',
                               'List of Str (n fold) <= List of Str (n fold) -> List of Str (n fold)',
                               'List of Bool (n fold) <= List of Bool (n fold) -> List of Bool (n fold)']

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
class Leq(CompOp):
    __PRECD: Final[Tuple[int, int]] = (10, 9)
    __SYM: Final[str] = '>='
    __SGN: Final[List[str]] = ['Real >= Real -> Bool',
                               'Str >= Str -> Bool',
                               'Bool >= Bool -> Bool',
                               'Sym >= Sym -> Sym',
                               'Real >= List of Real (n fold) -> List of Bool (n fold)',
                               'Str >= List of Str (n fold) -> List of Bool (n fold)',
                               'Bool >= List of Bool (n fold) -> List of Bool (n fold)',
                               'List of Real (n fold) >= Real -> List of Bool (n fold)',
                               'List of Str (n fold) >= Str -> List of Bool (n fold)',
                               'List of Bool (n fold) >= Bool -> List of Bool (n fold)',
                               'List of Real (n fold) >= List of Real (n fold) -> List of Bool (n fold)',
                               'List of Str (n fold) >= List of Str (n fold) -> List of Str (n fold)',
                               'List of Bool (n fold) >= List of Bool (n fold) -> List of Bool (n fold)']

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
