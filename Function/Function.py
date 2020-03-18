from sys import maxsize
from typing import Final, Tuple, List


class Fun:
    __PRECD: Final[Tuple[int, int]] = (0, maxsize)
    __SGN: List[str] = None

    def __new__(cls, *args, **kwargs) -> None:
        raise NotImplementedError

    @classmethod
    def precd_in(cls) -> int:
        return cls.__PRECD[0]

    @classmethod
    def precd_out(cls) -> int:
        return cls.__PRECD[1]

    @classmethod
    def sgn(cls) -> List[str]:
        return cls.__SGN
