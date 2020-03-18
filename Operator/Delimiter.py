from __future__ import annotations

from sys import maxsize
from typing import final, Final, Tuple, Dict, Optional, List

from Core import Token, TypeSystem
from Operator import Operator


class DelimOp(Operator.Op):
    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class Lpar(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (0, maxsize)
    __SYM: Final[str] = '('

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


@final
class Rpar(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (0, maxsize)
    __SYM: Final[str] = ')'

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


@final
class SqrLpar(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (0, maxsize)
    __SYM: Final[str] = '['

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


@final
class SqrRpar(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (0, maxsize)
    __SYM: Final[str] = ']'

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


@final
class CrlLpar(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (0, maxsize)
    __SYM: Final[str] = '{'

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


@final
class CrlRpar(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (0, maxsize)
    __SYM: Final[str] = '}'

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


@final
class Com(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (0, maxsize)
    __SYM: Final[str] = ','

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


@final
class Seq(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (16, 15)
    __SYM: Final[str] = ':'
    __SGN: Final[List[str]] = ['Real:Real -> List of Real (1 fold)',
                               'Real:Real:Real -> List of Real (1 fold)',
                               'Sym:Sym -> Sym',
                               'Sym:Sym:Sym -> Sym']
    __ARGC: Final[int] = 2

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
        t1: TypeSystem.T = rt.chd[0].t
        t2: TypeSystem.T = rt.chd[1].t

        if t1.base and t2.base:
            res_t: TypeSystem.T = TypeSystem.T.supt(t1, t2)

            if type(res_t) == TypeSystem.Real:
                rt.t = TypeSystem.Tens(res_t, [None])
            elif type(res_t) == TypeSystem.Sym:
                rt.t = res_t
            else:
                return None
        else:
            return None

        return t_env


@final
class Idx(DelimOp):
    __PRECD: Final[Tuple[int, int]] = (22, 21)
    __SYM: Final[str] = 'IDX'
    __SGN: Final[List[str]] = ['Sym[Any] -> Sym',
                               'List of Any (1 fold) [Real] -> Any',
                               'List of Any (n fold) [Real] -> List of Any (n - 1 fold)         given that n > 1',
                               'List of Any (n fold) [List of Real (1 fold)] -> List of Any (n fold)',
                               'List of Any (n fold) [List of Bool (1 fold)] -> List of Any (n fold)',
                               'List of Any[Sym] -> Sym',
                               'Sym[Any, ..., Any] = Sym[Any]...[Any]',
                               'List of Any (n fold)[Any, ..., Any] = List of Any[Any]...[Any]  given that # of idx <= n']

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
    def __chk_t_hlpr(cls, src_t: TypeSystem.T, idx_t: TypeSystem.T) -> Optional[TypeSystem.T]:
        if src_t.base:
            if type(src_t) == TypeSystem.Sym:
                return src_t
            else:
                return None
        else:
            if idx_t.base:
                if type(idx_t) == TypeSystem.Real:
                    return TypeSystem.ArrFact.inst().idx_arr_t(src_t)
                elif type(idx_t) == TypeSystem.Sym:
                    return idx_t
                else:
                    return None
            else:
                if type(idx_t.chd_t) in [TypeSystem.Real, TypeSystem.Bool] and idx_t.fold == 1:
                    return src_t
                else:
                    return None

    @classmethod
    def chk_t(cls, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Optional[Dict[int, TypeSystem.T]]:
        t1: TypeSystem.T = rt.chd[0].t

        if any(map(lambda x: type(x.t) == TypeSystem.Sym, rt.chd)):
            rt.t = TypeSystem.Sym.inst()

            return t_env

        if t1.base or t1.fold < rt.argc - 1:
            return None

        for tok in rt.chd[1:]:
            t1 = cls.__chk_t_hlpr(t1, tok.t)

            if not t1:
                return None

        rt.t = t1

        return t_env
