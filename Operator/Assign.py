from __future__ import annotations

from typing import final, Final, Tuple, Dict, Optional, List

from Core import Token, TypeSystem
from Operator import Operator


class AsgnOp(Operator.Op):
    __ARGC: Final[int] = 2

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError

    @classmethod
    def argc(cls) -> int:
        return cls.__ARGC


@final
class Asgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '='
    __SGN: Final[List[str]] = ['Sym = Real -> Real',
                               'Sym = Cmplx -> Cmplx',
                               'Sym = Str -> Str',
                               'Sym = Bool -> Bool',
                               'Sym = Sym -> Sym',
                               'Sym = List of Real (n fold) -> List of Real (n fold)',
                               'Sym = List of Cmplx (n fold) -> List of Cmplx (n fold)',
                               'Sym = List of Str (n fold) -> List of Str (n fold)',
                               'Sym = List of Bool (n fold) -> List of Bool (n fold)']

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
            if not (type(t1) == TypeSystem.Sym) or type(t2) == TypeSystem.Void:
                return None
            else:
                rt.t = t2
        else:
            return None

        return t_env


@final
class AddAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '+='

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
class SubAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '-='

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
class MulAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '*='

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
class MatMulAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '%*%='

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
class DivAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '/='

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError


@final
class RemAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '%='

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
class QuotAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '//='

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
class PowAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '**='

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
class AndAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '&='

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
class OrAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '|='

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
class XorAsgn(AsgnOp):
    __PRECD: Final[Tuple[int, int]] = (1, 2)
    __SYM: Final[str] = '^='

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
