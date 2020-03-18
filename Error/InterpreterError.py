from __future__ import annotations

from typing import final, List

from Core import Token
from Error import Error
from Operator import *


@final
class TErr(Error.InterpErr):
    def __init__(self, errno: int, line: str, pos: int, err_tok: Token.Tok, cand_sgn: List[str], handle: str) -> None:
        super().__init__(errno, line, pos)
        self.__cand_sgn: List[str] = cand_sgn
        self.__handle: str = handle

        if type(err_tok) == Token.Op:
            if err_tok.v in [Unary.Plus, Unary.Minus, Bool.Neg]:
                self.__err_sgn: str = f'{err_tok.v.sym()}{err_tok.chd[0].t}'
            elif err_tok.v == Unary.Trans:
                self.__err_sgn: str = f'{err_tok.chd[0].t}{err_tok.v.sym()}'
            elif err_tok.v == Delimiter.Seq:
                self.__err_sgn: str = f'{err_tok.chd[0].t}:{err_tok.chd[1].t}'
            elif err_tok.v == Delimiter.Idx:
                self.__err_sgn: str = f'{err_tok.chd[0].t}[' + ', '.join([str(tok.t) for tok in err_tok.chd[1:]]) + f']'
            else:
                self.__err_sgn: str = f'{err_tok.chd[0].t} {err_tok.v.sym()} {err_tok.chd[1].t}'

    @property
    def err_sgn(self) -> str:
        return self.__err_sgn

    @property
    def cand_sgn(self) -> List[str]:
        return self.__cand_sgn

    @property
    def handle(self) -> str:
        return self.__handle
