from typing import final, List, Tuple
from functools import reduce


class Poly:
    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass


@final
class NilPoly(Poly):
    def __init__(self, var: int):
        super().__init__()
        self.__var: int = var


@final
class UniPoly(Poly):
    def __init__(self, var: int, coef: List[int]) -> None:
        super().__init__()
        self.__var: int = var
        self.__coef: List[int] = coef
        self.__deg: int = len(self.__coef) - 1

    def __del__(self) -> None:
        pass


@final
class UniSparPoly(Poly):
    def __init__(self, var: int, coef: List[Tuple[int, int]]) -> None:
        super().__init__()
        self.__var: int = var
        self.__coef: List[Tuple[int, int]] = coef
        self.__deg: int = coef[-1][1]

    def __del__(self) -> None:
        pass


@final
class MultiPoly(Poly):
    def __init__(self, var: List[int], coef: list, deg: int) -> None:
        super().__init__()
        self.__var: List[int] = var
        self.__coef: list = coef
        self.__deg: int = deg

    def __del__(self) -> None:
        pass


@final
class MultiSparPoly(Poly):
    def __init__(self, var: List[int], coef: List[int]) -> None:
        super().__init__()
        self.__var: int = var
        self.__coef: List[Tuple[int, List[int]]] = coef
        self.__deg: int = max(deg)

    def __del__(self) -> None:
        pass
