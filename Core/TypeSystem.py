from __future__ import annotations

from typing import final, List, Optional


class T:
    def __init__(self, base: bool) -> None:
        self.__base: bool = base

    @classmethod
    def supt(cls, t1: T, t2: T) -> T:
        return t2 if t1 <= t2 else t1 if t2 <= t1 else None

    @classmethod
    def subt(cls, t1: T, t2: T) -> T:
        return t1 if t1 <= t2 else t2 if t2 <= t1 else None

    @property
    def base(self) -> bool:
        return self.__base


@final
class Real(T):
    __inst: Real = None

    def __init__(self) -> None:
        super().__init__(True)

    def __le__(self, other: T) -> bool:
        return type(other) in [Real, Cmplx, Sym]

    def __str__(self) -> str:
        return 'Real'

    @classmethod
    def inst(cls) -> Real:
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Real
        """
        if not cls.__inst:
            cls.__inst = Real()

        return cls.__inst


@final
class Cmplx(T):
    __inst: Cmplx = None

    def __init__(self) -> None:
        super().__init__(True)

    def __le__(self, other: T) -> bool:
        return type(other) in [Cmplx, Sym]

    def __str__(self) -> str:
        return 'Complex'

    @classmethod
    def inst(cls) -> Cmplx:
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Real
        """
        if not cls.__inst:
            cls.__inst = Cmplx()

        return cls.__inst


@final
class Str(T):
    __inst: Str = None

    def __init__(self) -> None:
        super().__init__(True)

    def __le__(self, other: T) -> bool:
        return type(other) in [Str, Sym]

    def __str__(self) -> str:
        return 'String'

    @classmethod
    def inst(cls) -> Str:
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Real
        """
        if not cls.__inst:
            cls.__inst = Str()

        return cls.__inst


@final
class Bool(T):
    __inst: Bool = None

    def __init__(self) -> None:
        super().__init__(True)

    def __le__(self, other: T) -> bool:
        return type(other) in [Bool, Sym]

    def __str__(self) -> str:
        return 'Bool'

    @classmethod
    def inst(cls) -> Bool:
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Real
        """
        if not cls.__inst:
            cls.__inst = Bool()

        return cls.__inst


@final
class Sym(T):
    __inst: Sym = None

    def __init__(self) -> None:
        super().__init__(True)

    def __le__(self, other: T) -> bool:
        return type(other) == Sym

    def __str__(self) -> str:
        return 'Symbol'

    @classmethod
    def inst(cls) -> Sym:
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Real
        """
        if not cls.__inst:
            cls.__inst = Sym()

        return cls.__inst


@final
class Void(T):
    __inst: Void = None

    def __init__(self) -> None:
        super().__init__(True)

    def __le__(self, other: T) -> bool:
        return type(other) in [Void, Sym]

    def __str__(self) -> str:
        return 'Void'

    @classmethod
    def inst(cls) -> Void:
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Real
        """
        if not cls.__inst:
            cls.__inst = Void()

        return cls.__inst


@final
class Tens(T):
    def __init__(self, chd_t: T, dim: List[int]) -> None:
        super().__init__(False)
        self.__chd_t: T = chd_t
        self.__dim: List[int] = dim
        self.__fold: int = len(dim)

    def __le__(self, other: T) -> bool:
        other_t: type = type(other)

        if other_t == Sym:
            return True
        elif other_t == Tens:
            return self.__chd_t <= other.chd_t and len(self.__dim) == len(other.dim)
        elif other_t == Arr:
            return self.__chd_t <= other.chd_t and len(self.__dim) == other.fold
        else:
            return False

    def __eq__(self, other: T) -> bool:
        return type(other) == Tens and self.__chd_t == other.chd_t and self.__fold == other.fold

    def __ne__(self, other: T) -> bool:
        return type(other) != Tens or self.__chd_t != other.chd_t or self.__fold != other.fold

    def __str__(self) -> str:
        return f'List of {self.__chd_t} ({self.__fold} fold)'

    @property
    def chd_t(self) -> T:
        return self.__chd_t

    @property
    def dim(self) -> List[int]:
        return self.__dim

    @property
    def fold(self) -> int:
        return self.__fold


@final
class Arr(T):
    def __init__(self, chd_t: T, fold: int, dim: List[T] = None) -> None:
        super().__init__(False)
        self.__chd_t: T = chd_t
        self.__fold: int = fold
        self.__dim: List[T] = dim

    def __le__(self, other: T) -> bool:
        return (type(other) == Sym) or \
               (type(other) == Arr and self.__chd_t <= other.chd_t and self.__fold == other.fold)

    def __eq__(self, other: T) -> bool:
        return type(other) == Arr and self.__chd_t == other.chd_t and self.__fold == other.fold

    def __ne__(self, other: T) -> bool:
        return type(other) != Arr or self.__chd_t != other.chd_t or self.__fold != other.fold

    def __str__(self) -> str:
        return f'List of {self.__chd_t} ({self.__fold} fold)'

    @property
    def chd_t(self) -> T:
        return self.__chd_t

    @property
    def dim(self) -> List[T]:
        return self.__dim

    @property
    def fold(self) -> int:
        return self.__fold


@final
class ArrFact:
    __inst: ArrFact = None

    @classmethod
    def inst(cls) -> ArrFact:
        if not cls.__inst:
            cls.__inst = ArrFact()

        return cls.__inst

    def get_arr_t(self, chd_t: List[T]) -> Optional[T]:
        if not chd_t:
            return Tens(Void.inst(), [0])

        res_t: T = chd_t[0]

        for i in range(len(chd_t) - 1):
            res_t = T.supt(res_t, chd_t[i + 1])

            if not res_t:
                return None

        if res_t.base:
            if type(res_t) == Void:
                return Tens(Void.inst(), [0])
            elif type(res_t) == Sym:
                return res_t
            else:
                return Tens(res_t, [len(chd_t)])

        if type(res_t) == Arr:
            return Arr(res_t.chd_t, res_t.fold, chd_t)
        else:
            if len(chd_t) == 1:
                return Tens(chd_t[0].chd_t, [1, *res_t.dim])

            homo = all([d is not None for d in res_t.dim])
            i: int = 2

            while homo and i < len(chd_t):
                homo &= (chd_t[0].dim == chd_t[i].dim)
                i += 1

            return Tens(res_t.chd_t, [len(chd_t), *res_t.dim]) if homo else Arr(res_t.chd_t, len(res_t.dim) + 1, chd_t)

    def coerce_arr_t(self, src: T, chd_t: T) -> T:
        if type(chd_t) == Sym:
            return chd_t
        else:
            return Tens(chd_t, src.dim) if type(src) == Tens else Arr(chd_t, src.fold, src.dim)

    def idx_arr_t(self, src: T) -> T:
        if type(src) == Tens:
            return src.chd_t if src.fold == 1 else Tens(src.chd_t, src.dim[1:])
        else:
            return Arr(src.chd_t, src.fold - 1)


