from __future__ import annotations

from typing import final, List, Tuple, Optional, Set, Dict

from Core import AST, Token, TypeSystem, Type
from Operator import *
from Util import Printer
from copy import copy


@final
class FVar:
    __cnt: int = 0

    def __init__(self) -> None:
        self.__v: int = self.__cnt

        self.__update()

    def __eq__(self, other: FVar) -> bool:
        return self.__v == other.v

    def __lt__(self, other: FVar) -> bool:
        return self.__v < other.v

    def __le__(self, other: FVar) -> bool:
        return self.__v <= other.v

    @classmethod
    def __update(cls) -> None:
        cls.__cnt += 1

    @property
    def v(self) -> int:
        return self.__v

    @v.setter
    def v(self, v: int) -> None:
        self.__v = v


@final
class List2(TypeSystem.T):
    def __init__(self, chd_t: TypeSystem.T, fold: FVar) -> None:
        super().__init__(False)
        self.__chd_t: TypeSystem.T = chd_t
        self.__fold: FVar = fold

    def __str__(self) -> str:
        return f'List({self.__chd_t}, {self.__fold.v})'

    @property
    def chd_t(self) -> TypeSystem.T:
        return self.__chd_t

    @property
    def fold(self) -> FVar:
        return self.__fold

    @fold.setter
    def fold(self, fold: FVar) -> None:
        self.__fold = fold


@final
class TVar:
    __cnt: int = 0

    def __init__(self) -> None:
        self.__v: int = self.__cnt

        self.__update()

    def __eq__(self, other: TVar) -> bool:
        return self.__v == other.v

    def __lt__(self, other: TVar) -> bool:
        return self.__v < other.v

    def __le__(self, other: TVar) -> bool:
        return self.__v <= other.v

    @classmethod
    def __update(cls) -> None:
        cls.__cnt += 1

    @property
    def v(self) -> int:
        return self.__v

    @v.setter
    def v(self, v: int) -> None:
        self.__v = v


@final
class FConst:
    __idx_map: List[Tuple[int, int]] = []
    __idx_src: List[Tuple[int, int]] = []
    __merge_it: List[int] = []

    def __init__(self, var: List[FVar], offset: List[Optional[int]]) -> None:
        self.__var: List[FVar] = var
        self.__offset: List[Optional[int]] = offset
        self.__eq: bool = offset[0] is None

    # Debugging
    # latter remove
    def __str__(self) -> str:
        buf: str = '{'

        for i in range(len(self.__var)):
            buf += f'{self.__var[i].v}:{self.__offset[i]}, '

        return buf[:-2] + '}'

    def __add__(self, other: FConst) -> FConst:
        assert self.__eq == other.eq == False

        merged_var: List[FVar] = []
        merged_offset: List[int] = []
        i: int = 0
        j: int = 0

        while i < len(self.__var) and j < len(other.var):
            while i < len(self.__var) and self.__var[i] < other.var[j]:
                merged_var.append(self.__var[i])
                merged_offset.append(self.__offset[i])
                i += 1

            if i == len(self.__var):
                continue

            while j < len(other.var) and self.__var[i] > other.var[j]:
                merged_var.append(other.var[j])
                merged_offset.append(other.offset[j])
                j += 1

        if i == len(self.__var):
            merged_var += other.var[j:]
            merged_offset += other.offset[j:]
        else:
            merged_var += self.__var[i:]
            merged_offset += self.__offset[i:]

        return FConst(merged_var, merged_offset)

    def __mul__(self, other: FConst) -> Tuple[bool, Optional[FConst]]:
        if self.__eq:
            if other.eq:
                return self.__mul_eq_eq_hlper(other)
            else:
                return self.__mul_eq_neq_hlpr(other)
        else:
            if other.eq:
                return other * self
            else:
                return self.__mul_neq_neq_hlpr(other)

    def __mul_eq_eq_hlper(self, other: FConst) -> Tuple[bool, Optional[FConst]]:
        i: int = 0
        j: int = 0
        cnt: int = 0
        new_var: List[FVar] = []
        new_offset: List[Optional[int]] = []

        self.__idx_map.clear()
        self.__idx_src.clear()
        self.__merge_it.clear()

        while i < len(self.__var) and j < len(other.var):
            while i < len(self.__var) and self.__var[i] < other.var[j]:
                new_var.append(self.__var[i])
                self.__idx_src.append((-1, i))
                i += 1

            if i == len(self.__var):
                continue

            if self.__var[i] == other.var[j]:
                self.__idx_map.append((i, j))
                self.__idx_src.append((0, cnt))
                cnt += 1
                i += 1
            else:
                self.__idx_src.append((1, j))

            new_var.append(other.var[j])
            j += 1

        if not self.__idx_map:
            return True, None

        if i == len(self.__var):
            self.__idx_src += [(1, k + j) for k in range(len(other.var[j:]))]
            new_var += other.var[j:]
        else:
            self.__idx_src += [(-1, k + i) for k in range(len(self.__var[i:]))]
            new_var += self.__var[i:]

        assert len(self.__idx_src) == len(new_var)

        # Equal ref
        if self.__idx_map[0][0] == 0:
            if self.__idx_map[0][1] == 0:
                for idx in self.__idx_map[1:]:
                    if self.__offset[idx[0]] != other.offset[idx[1]]:
                        return False, None

                for idx in self.__idx_src:
                    if idx[0] == -1:
                        new_offset.append(self.__offset[idx[1]])
                    elif idx[0] == 0:
                        new_offset.append(other.offset[self.__idx_map[idx[1]][1]])
                    else:
                        new_offset.append(other.offset[idx[1]])

                return True, FConst(new_var, new_offset)
            # Self ref and other offset
            else:
                addi: int = other.offset[self.__idx_map[0][1]]

                for idx in self.__idx_map[1:]:
                    if other.offset[idx[1]] - self.__offset[idx[0]] != addi:
                        return False, None

                for idx in self.__idx_src:
                    if idx[0] == -1:
                        new_offset.append(self.__offset[idx[1]] + addi)
                    elif idx[0] == 0:
                        new_offset.append(other.offset[self.__idx_map[idx[1]][1]])
                    else:
                        new_offset.append(other.offset[idx[1]])

                return True, FConst(new_var, new_offset)
        else:
            # other ref and self offset
            if self.__idx_map[0][1] == 0:
                addi: int = self.__offset[self.__idx_map[0][0]]

                for idx in self.__idx_map[1:]:
                    if self.__offset[idx[0]] - other.offset[idx[1]] != addi:
                        return False, None

                for idx in self.__idx_src:
                    if idx[0] == -1:
                        new_offset.append(self.__offset[idx[1]])
                    elif idx[0] == 0:
                        new_offset.append(self.__offset[self.__idx_map[idx[1]][0]])
                    else:
                        new_offset.append(other.offset[idx[1]] + addi)

                return True, FConst(new_var, new_offset)
            else:
                if self.__var[0] < other.var[0]:
                    addi: int = self.__offset[self.__idx_map[0][0]] - other.offset[self.__idx_map[0][1]]

                    for idx in self.__idx_map[1:]:
                        if self.__offset[idx[0]] - other.offset[idx[1]] != addi:
                            return False, None

                    for idx in self.__idx_src:
                        if idx[0] == -1:
                            new_offset.append(self.__offset[idx[1]])
                        elif idx[0] == 0:
                            new_offset.append(self.__offset[self.__idx_map[idx[1]][0]])
                        else:
                            if idx[1] == 0:
                                new_offset.append(addi)
                            else:
                                new_offset.append(other.offset[idx[1]] + addi)

                    return True, FConst(new_var, new_offset)
                else:
                    addi: int = other.offset[self.__idx_map[0][1]] - self.__offset[self.__idx_map[0][0]]

                    for idx in self.__idx_map[1:]:
                        if other.offset[idx[1]] - self.__offset[idx[0]] != addi:
                            return False, None

                    for idx in self.__idx_src:
                        if idx[0] == -1:
                            if idx[1] == 0:
                                new_offset.append(addi)
                            else:
                                new_offset.append(self.__offset[idx[1]] + addi)
                        elif idx[0] == 0:
                            new_offset.append(other.offset[self.__idx_map[idx[1]][1]])
                        else:
                            new_offset.append(other.offset[idx[1]])

                    return True, FConst(new_var, new_offset)

    def __mul_neq_neq_hlpr(self, other: FConst) -> Tuple[bool, Optional[FConst]]:
        i: int = 0
        j: int = 0
        new_var: List[FVar] = []
        new_offset: List[Optional[int]] = []
        disjoint: bool = True

        while i < len(self.__var) and j < len(other.var):
            while i < len(self.__var) and self.__var[i] < other.var[j]:
                new_var.append(self.__var[i])
                new_offset.append(self.__offset[i])
                i += 1

            if i == len(self.__var):
                continue

            if self.__var[i] == other.var[j]:
                if self.__offset[i] != other.offset[j]:
                    return False, None

                i += 1
                disjoint = False

            new_var.append(other.var[j])
            new_offset.append(other.offset[j])
            j += 1

        return (True, None) if disjoint else (True, FConst(new_var, new_offset))

    def __mul_eq_neq_hlpr(self, other: FConst) -> Tuple[bool, Optional[FConst]]:
        i: int = 0
        j: int = 0
        cnt: int = 0
        new_var: List[FVar] = []
        new_offset: List[Optional[int]] = []

        self.__idx_map.clear()
        self.__idx_src.clear()
        self.__merge_it.clear()

        while i < len(self.__var) and j < len(other.var):
            while i < len(self.__var) and self.__var[i] < other.var[j]:
                new_var.append(self.__var[i])
                self.__idx_src.append((-1, i))
                i += 1

            if i == len(self.__var):
                continue

            if self.__var[i] == other.var[j]:
                self.__idx_map.append((i, j))
                self.__idx_src.append((0, cnt))
                cnt += 1
                i += 1
            else:
                self.__idx_src.append((1, j))

            new_var.append(other.var[j])
            j += 1

        if not self.__idx_map:
            return True, None

        if i == len(self.__var):
            self.__idx_src += [(1, k + j) for k in range(len(other.var[j:]))]
            new_var += other.var[j:]
        else:
            self.__idx_src += [(-1, k + i) for k in range(len(self.__var[i:]))]
            new_var += self.__var[i:]

        assert len(self.__idx_src) == len(new_var)

        # Ref eq something
        if self.__idx_map[0][0] == 0:
            addi: int = other.offset[self.__idx_map[0][1]]

            for idx in self.__idx_map[1:]:
                if other.offset[idx[1]] - self.__offset[idx[0]] != addi:
                    return False, None

            for idx in self.__idx_src:
                if idx[0] == -1:
                    new_offset.append(self.__offset[idx[1]] + addi)
                elif idx[0] == 0:
                    new_offset.append(other.offset[self.__idx_map[idx[1]][1]])
                else:
                    new_offset.append(other.offset[idx[1]])

            return True, FConst(new_var, new_offset)
        else:
            addi: int = other.offset[self.__idx_map[0][1]] - self.__offset[self.__idx_map[0][0]]

            for idx in self.__idx_map[1:]:
                if other.offset[idx[1]] - self.__offset[idx[0]] != addi:
                    return False, None

            for idx in self.__idx_src:
                if idx[0] == -1:
                    if idx[1] == 0:
                        new_offset.append(addi)
                    else:
                        new_offset.append(self.__offset[idx[1]] + addi)
                elif idx[0] == 0:
                    new_offset.append(other.offset[self.__idx_map[idx[1]][1]])
                else:
                    new_offset.append(other.offset[idx[1]])

            return True, FConst(new_var, new_offset)

    @property
    def var(self) -> List[FVar]:
        return self.__var

    @property
    def offset(self) -> List[Optional[int]]:
        return self.__offset

    @property
    def eq(self) -> bool:
        return self.__eq

    @var.setter
    def var(self, var: List[FVar]) -> None:
        self.__var = var

    def drop(self) -> FConst:
        if not self.__eq:
            return self

        drop_msk: List[bool] = [False for _ in range(len(self.__var))]
        uniq_idx: List[int] = [0]

        i: int = 1

        while i < len(self.__var):
            if self.__offset[i] == 0:
                drop_msk[i] = True
                self.__var[i].v = self.__var[0].v

            i += 1

        i: int = 1

        while i < len(self.__var):
            if drop_msk[i]:
                i += 1

                continue

            uniq_idx.append(i)

            j: int = i + 1

            while j < len(self.__var):
                if self.__var[i] == self.__var[j]:
                    drop_msk[j] = True
                    self.__var[j].v = self.__var[i]

                j += 1

            i += 1

        return FConst([self.__var[idx] for idx in uniq_idx], [self.__offset[idx] for idx in uniq_idx])


@final
class TConst:
    __idx_map: List[Tuple[int, int]] = []
    __idx_src: List[Tuple[int, int]] = []
    __merge_it: List[Tuple[int, int, List[TypeSystem.T], List[FConst]]] = []
    __merge_idx: List[int] = []

    def __init__(self, var: List[TVar], cand: List[List[TypeSystem.T]], f_const: List[List[FConst]]) -> None:
        self.__var: List[TVar] = var
        self.__cand: List[List[TypeSystem.T]] = cand
        self.__f_const: List[List[FConst]] = f_const
        self.__f_var_l: List[List[FVar]] = []

        for it in f_const:
            if not it:
                self.__f_var_l.append([])

                continue

            var_l: List[FVar] = copy(it[0].var)

            for const in it[1:]:
                var_l = self.__merge(var_l, const.var)

            self.__f_var_l.append(var_l)

    def __getitem__(self, item: TVar) -> Optional[Set[TypeSystem.T]]:
        pos: int = 0

        while pos < len(self.__var):
            if item == self.__var[pos]:

                return {it[pos] for it in self.__cand}
            elif item < self.__var[pos]:
                return None

            pos += 1

        return None

    def __mul__(self, other: TConst) -> Tuple[bool, Optional[TConst]]:
        print('unifying two constraint table')
        print('LHS')
        print('  @var  : ' + ', '.join([str(var.v) for var in self.__var]))
        print('  @const:')

        for i in range(len(self.__cand)):
            print(f'    [{i}] ' + ', '.join([str(t) for t in self.__cand[i]]) + ' ' +
                  ' '.join([str(it) for it in self.__f_const[i]]) + ' / ' +
                  ', '.join([str(var.v) for var in self.__f_var_l[i]]))

        print('')
        print('RHS')
        print('  @var  : ' + ', '.join([str(var.v) for var in other.var]))
        print('  @const:')

        for i in range(len(other.cand)):
            print(f'    [{i}] ' + ', '.join([str(t) for t in other.cand[i]]) + ' ' +
                  ' '.join([str(it) for it in other.f_const[i]]) + ' / ' +
                  ', '.join([str(var.v) for var in other.__f_var_l[i]]))

        print('')

        i: int = 0
        j: int = 0
        cnt: int = 0
        new_var: List[TVar] = []
        new_cand: List[List[TypeSystem.T]] = []
        new_f_const: List[List[FConst]] = []

        self.__idx_map.clear()
        self.__idx_src.clear()
        self.__merge_it.clear()

        while i < len(self.__var) and j < len(other.var):
            while i < len(self.__var) and self.__var[i] < other.var[j]:
                new_var.append(self.__var[i])
                self.__idx_src.append((-1, i))
                i += 1

            if i == len(self.__var):
                continue

            if self.__var[i] == other.var[j]:
                self.__idx_map.append((i, j))
                self.__idx_src.append((0, cnt))
                cnt += 1
                i += 1
            else:
                self.__idx_src.append((1, j))

            new_var.append(other.var[j])
            j += 1

        if not self.__idx_map:
            print('nothing to unify')

            return True, None

        if i == len(self.__var):
            self.__idx_src += [(1, k + j) for k in range(len(other.var[j:]))]
            new_var += other.var[j:]
        else:
            self.__idx_src += [(-1, k + i) for k in range(len(self.__var[i:]))]
            new_var += self.__var[i:]

        assert len(self.__idx_src) == len(new_var)

        for i in range(len(self.__cand)):
            for j in range(len(other.cand)):
                merge_flag: bool = True
                resolved: List[TypeSystem.T] = []
                f_const: List[FConst] = []

                for idx in self.__idx_map:
                    sub_t, const = self.__t_resolve(self.__cand[i][idx[0]], other.cand[j][idx[1]])

                    merge_flag &= bool(sub_t)
                    resolved.append(sub_t)

                    if const:
                        f_const.append(const)

                    if not merge_flag:
                        break

                if merge_flag:
                    self.__merge_it.append((i, j, resolved, f_const))

        if not self.__merge_it:
            print('unification failed')

            return False, None

        for it in self.__merge_it:
            new_it: List[TypeSystem.T] = []

            for idx in self.__idx_src:
                if idx[0] == -1:
                    new_it.append(self.__cand[it[0]][idx[1]])
                elif idx[0] == 0:
                    new_it.append(it[2][idx[1]])
                else:
                    new_it.append(other.cand[it[1]][idx[1]])

            new_const_it: List[FConst] = self.__f_unify(self.__f_const[it[0]], other.f_const[it[1]])

            if new_const_it is None:
                continue

            new_const_it = self.__f_unify(new_const_it, it[3])

            if new_const_it is None:
                continue

            new_it, new_const_it = self.__alpha_conv(new_it, new_const_it,
                                                     self.__merge(self.__f_var_l[it[0]], other.f_var_l[it[1]]))
            new_const_it = [const.drop() for const in new_const_it]
            new_cand.append(new_it)
            new_f_const.append(new_const_it)

        if not new_cand:
            print('unification failed')
            return False, None

        print('unification result')
        print('  @var  : ' + ', '.join([str(var.v) for var in new_var]))
        print('  @const:')

        for i in range(len(new_cand)):
            print(f'    [{i}] ' + ', '.join([str(t) for t in new_cand[i]]) + ' ' +
                  ' '.join([str(it) for it in new_f_const[i]]))

        print('')
        return True, TConst(new_var, new_cand, new_f_const)

    def __t_resolve(self, t1: TypeSystem.T, t2: TypeSystem.T) -> Tuple[Optional[TypeSystem.T], Optional[FConst]]:
        if t1.base:
            return (None, None) if not t2.base else (t1, None) if type(t1) == type(t2) else (None, None)

        if t2.base or type(t1.chd_t) != type(t2.chd_t):
            return None, None

        if t1.fold == t2.fold:
            return List2(t1.chd_t, t1.fold), None
        elif t1.fold < t2.fold:
            return List2(t1.chd_t, t1.fold), FConst([t1.fold, t2.fold], [None, 0])
        else:
            return List2(t1.chd_t, t1.fold), FConst([t2.fold, t1.fold], [None, 0])

    def __f_unify(self, f_const_l1: List[FConst], f_const_l2: List[FConst]) -> Optional[List[FConst]]:
        unified: List[FConst] = []
        merged: List[FConst] = []

        self.__merge_idx.clear()
        f_const_l2 = copy(f_const_l2)

        for i in range(len(f_const_l1)):
            del_idx: List[int] = []
            res: FConst = f_const_l1[i]
            j: int = 0

            while j < len(f_const_l2):
                succ, tmp = res * f_const_l2[j]

                if not succ:
                    return None

                if tmp:
                    del_idx.append(j)
                    res = tmp

                j += 1

            if del_idx:
                j = len(del_idx) - 1

                while j >= 0:
                    del f_const_l2[del_idx[j]]

                    j -= 1

                f_const_l2.append(res)
            else:
                unified.append(copy(res))

        unified += f_const_l2

        for i in range(len(unified)):
            if unified[i].eq:
                merged.append(unified[i])
            else:
                self.__merge_idx.append(i)

        if len(self.__merge_idx) == 0:
            return merged

        res: FConst = unified[self.__merge_idx[0]]

        for i in self.__merge_idx[1:]:
            res += unified[i]

        return merged + [res]

    def __alpha_conv(self, cand: List[TypeSystem.T], f_const: List[FConst],
                     f_var: List[FVar]) -> Tuple[List[TypeSystem.T], List[FConst]]:
        new_f_var: List[FVar] = [FVar() for _ in range(len(f_var))]
        var_map: Dict[int, FVar] = {f_var[i].v: new_f_var[i] for i in range(len(f_var))}

        for t in cand:
            if not t.base:
                t.fold = var_map[t.fold.v]

        for const in f_const:
            const.var = [var_map[var.v] for var in const.var]

        return cand, f_const

    def __merge(self, l1: list, l2: list) -> list:
        i: int = 0
        j: int = 0
        res: list = []

        while i < len(l1) and j < len(l2):
            while i < len(l1) and l1[i] < l2[j]:
                res.append(l1[i])
                i += 1

            if i == len(l1):
                continue

            if l1[i] == l2[j]:
                i += 1

            res.append(l2[j])
            j += 1

        if i == len(l1):
            res += l2[j:]
        else:
            res += l1[i:]

        return res

    @property
    def var(self) -> List[TVar]:
        return self.__var

    @property
    def cand(self) -> List[List[TypeSystem.T]]:
        return self.__cand

    @property
    def f_const(self) -> List[List[FConst]]:
        return self.__f_const

    @property
    def f_var_l(self) -> List[List[FVar]]:
        return self.__f_var_l

    def empty(self) -> bool:
        return not self.__var

    def split(self) -> List[TConst]:
        if len(self.__var) == 1:
            return [self]

        i: int = len(self.__var) - 1
        del_idx: List[int] = []
        frag: List[TConst] = []

        while i >= 0:
            split_flag: bool = True
            j: int = 1
            ref_t: TypeSystem.T = self.__cand[0][i]

            while j < len(self.__cand) and split_flag:
                split_flag &= (ref_t == self.__cand[j][i])
                j += 1

            if split_flag:
                del_idx.append(i)
                frag.append(TConst([self.__var[i]], [[self.__cand[0][i]]]))

            i -= 1

        if not frag:
            return [self]

        for idx in del_idx:
            del self.__var[idx]

            for it in self.__cand:
                del it[idx]

        return frag + [self] if self.__var else frag

    def drop(self, var: TVar) -> Optional[TVar]:
        i: int = 0

        while i < len(self.__var) and self.__var[i] < var:
            i += 1

        if i < len(self.__var) and var == self.__var[i]:
            print(f'drop {var.v} from constraint table')
            print('TARGET')
            print('  @var  : ' + ', '.join([str(var.v) for var in self.__var]))

            for it in self.__cand:
                print('  @const: ' + ', '.join([str(t) for t in it]))

            print('')

            del self.__var[i]

            for it in self.__cand:
                del it[i]

            print('drop result')
            print('  @var  : ' + ', '.join([str(var.v) for var in self.__var]))

            for it in self.__cand:
                print('  @const: ' + ', '.join([str(t) for t in it]))

            print('')

            return var
        else:
            return None


@final
class TChker:
    __inst: TChker = None

    def __init__(self) -> None:
        self.__expr: AST.AST = None
        self.__t_env: Dict[int, TVar] = {}
        self.__t_const: List[TConst] = []

    def __new_f_var(self, cnt: int) -> List[FVar]:
        return [FVar() for _ in range(cnt)]

    def __new_t_var(self) -> TVar:
        t_var: TVar = TVar()
        f_var: List[FVar] = self.__new_f_var(5)

        self.__t_const.append(TConst([t_var],
                                     [[TypeSystem.Real.inst()], [TypeSystem.Cmplx.inst()], [TypeSystem.Str.inst()],
                                      [TypeSystem.Bool.inst()], [TypeSystem.Void.inst()],
                                      [List2(TypeSystem.Real.inst(), f_var[0])],
                                      [List2(TypeSystem.Cmplx.inst(), f_var[1])],
                                      [List2(TypeSystem.Str.inst(), f_var[2])],
                                      [List2(TypeSystem.Bool.inst(), f_var[3])],
                                      [List2(TypeSystem.Void.inst(), f_var[4])]],
                                     [[], [], [], [], [], [FConst([f_var[0]], [None])], [FConst([f_var[1]], [None])],
                                      [FConst([f_var[2]], [None])], [FConst([f_var[3]], [None])],
                                      [FConst([f_var[4]], [None])]]))

        return t_var

    def __t_unify(self, new_const: TConst) -> None:
        new_const_l: List[TConst] = [new_const]
        unified: List[TConst] = []
        print('UNIFY')

        for i in range(len(self.__t_const)):
            del_idx: List[int] = []
            res: TConst = self.__t_const[i]
            j: int = 0

            while j < len(new_const_l):
                succ, tmp = res * new_const_l[j]

                if not succ:
                    raise TypeError

                if tmp:
                    del_idx.append(j)
                    res = tmp

                j += 1

            if del_idx:
                j = len(del_idx) - 1

                while j >= 0:
                    del new_const_l[del_idx[j]]

                    j -= 1

                # new_const_l += res.split()
                new_const_l += [res]
            else:
                unified.append(res)

        self.__t_const = unified + new_const_l

    # def __f_unify(self, new_const: FConst) -> None:

    def __subst(self, var1: TVar, var2: TVar) -> None:
        assert var1 < var2

        self.__t_unify(TConst([var1, var2], [[TypeSystem.Real.inst(), TypeSystem.Real.inst()],
                                             [TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst()],
                                             [TypeSystem.Str.inst(), TypeSystem.Str.inst()],
                                             [TypeSystem.Bool.inst(), TypeSystem.Bool.inst()]]))

        for i in range(len(self.__t_const)):
            res: TVar = self.__t_const[i].drop(var2)

            if res:
                if self.__t_const[i].empty():
                    del self.__t_const[i]

                print(f'sub: {var2.v} -> {var1.v}')
                var2.v = var1.v

                return

    def __init(self) -> None:
        self.__cnt = 0
        self.__t_const = []

    def __chk_t_hlpr(self, rt: Token.Tok):
        tok_t: type = type(rt)

        if tok_t == Token.Num:
            if type(rt.v) == complex:
                self.__t_unify(TConst([rt.t_var], [[TypeSystem.Cmplx.inst()]], [[]]))
            else:
                self.__t_unify(TConst([rt.t_var], [[TypeSystem.Real.inst()]], [[]]))
        elif tok_t == Token.Str:
            self.__t_unify(TConst([rt.t_var], [[TypeSystem.Str.inst()]], [[]]))
        elif tok_t == Token.Bool:
            self.__t_unify(TConst([rt.t_var], [[TypeSystem.Bool.inst()]], [[]]))
        elif tok_t == Token.Var:
            pass
            # find: TVar = self.__t_env.get(rt.v)
            #
            # if find:
            #     self.__subst(find, rt.t_var)
            # else:
            #     self.__t_env[rt.v] = rt.t_var
        elif tok_t == Token.Op and rt.v == Binary.Add:
            rt.chd[0].t_var = self.__new_t_var()
            self.__chk_t_hlpr(rt.chd[0])
            rt.chd[1].t_var = self.__new_t_var()
            self.__chk_t_hlpr(rt.chd[1])

            f_var: List[FVar] = self.__new_f_var(12)

            self.__t_unify(TConst([rt.t_var, rt.chd[0].t_var, rt.chd[1].t_var],
                                  [[TypeSystem.Real.inst(), TypeSystem.Real.inst(), TypeSystem.Real.inst()],
                                   [TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst(), TypeSystem.Real.inst()],
                                   [TypeSystem.Cmplx.inst(), TypeSystem.Real.inst(), TypeSystem.Cmplx.inst()],
                                   [TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst()],
                                   [TypeSystem.Real.inst(), List2(TypeSystem.Real.inst(), f_var[0]),
                                    List2(TypeSystem.Real.inst(), f_var[0])],
                                   [TypeSystem.Real.inst(), List2(TypeSystem.Cmplx.inst(), f_var[1]),
                                    List2(TypeSystem.Cmplx.inst(), f_var[1])],
                                   [TypeSystem.Cmplx.inst(), List2(TypeSystem.Real.inst(), f_var[2]),
                                    List2(TypeSystem.Cmplx.inst(), f_var[2])],
                                   [TypeSystem.Cmplx.inst(), List2(TypeSystem.Cmplx.inst(), f_var[3]),
                                    List2(TypeSystem.Cmplx.inst(), f_var[3])],
                                   [List2(TypeSystem.Real.inst(), f_var[4]), TypeSystem.Real.inst(),
                                    List2(TypeSystem.Real.inst(), f_var[4])],
                                   [List2(TypeSystem.Cmplx.inst(), f_var[5]), TypeSystem.Real.inst(),
                                    List2(TypeSystem.Cmplx.inst(), f_var[5])],
                                   [List2(TypeSystem.Real.inst(), f_var[6]), TypeSystem.Cmplx.inst(),
                                    List2(TypeSystem.Cmplx.inst(), f_var[6])],
                                   [List2(TypeSystem.Cmplx.inst(), f_var[7]), TypeSystem.Cmplx.inst(),
                                    List2(TypeSystem.Cmplx.inst(), f_var[7])],
                                   [List2(TypeSystem.Real.inst(), f_var[8]), List2(TypeSystem.Real.inst(), f_var[8]),
                                    List2(TypeSystem.Real.inst(), f_var[8])],
                                   [List2(TypeSystem.Cmplx.inst(), f_var[9]), List2(TypeSystem.Real.inst(), f_var[9]),
                                    List2(TypeSystem.Cmplx.inst(), f_var[9])],
                                   [List2(TypeSystem.Real.inst(), f_var[10]), List2(TypeSystem.Cmplx.inst(), f_var[10]),
                                    List2(TypeSystem.Cmplx.inst(), f_var[10])],
                                   [List2(TypeSystem.Cmplx.inst(), f_var[11]),
                                    List2(TypeSystem.Cmplx.inst(), f_var[11]),
                                    List2(TypeSystem.Cmplx.inst(), f_var[11])]],
                                  [[], [], [], [], [FConst([f_var[0]], [None])],
                                   [FConst([f_var[1]], [None])], [FConst([f_var[2]], [None])],
                                   [FConst([f_var[3]], [None])], [FConst([f_var[4]], [None])],
                                   [FConst([f_var[5]], [None])], [FConst([f_var[6]], [None])],
                                   [FConst([f_var[7]], [None])], [FConst([f_var[8]], [None])],
                                   [FConst([f_var[9]], [None])], [FConst([f_var[10]], [None])],
                                   [FConst([f_var[11]], [None])]]))
        elif tok_t == Token.List:
            for tok in rt.chd:
                tok.t_var = self.__new_t_var()
                self.__chk_t_hlpr(tok)

            if rt.argc == 0:
                f_var: FVar = FVar()

                self.__t_unify(TConst([rt.t_var], [[List2(TypeSystem.Void.inst(), f_var)]], [[FConst([f_var], [1])]]))
            elif rt.argc == 1:
                f_var: List[FVar] = self.__new_f_var(4)

                self.__t_unify(TConst([rt.t_var, rt.chd[0].t_var],
                                      [[List2(TypeSystem.Real.inst(), f_var[0]), TypeSystem.Real.inst()],
                                       [List2(TypeSystem.Cmplx.inst(), f_var[1]), TypeSystem.Cmplx.inst()],
                                       [List2(TypeSystem.Str.inst(), f_var[2]), TypeSystem.Str.inst()],
                                       [List2(TypeSystem.Bool.inst(), f_var[3]), TypeSystem.Bool.inst()]],
                                      [[FConst([f_var[0]], [1])], [FConst([f_var[1]], [1])], [FConst([f_var[2]], [1])],
                                       [FConst([f_var[3]], [1])]]))
            else:
                dummy: TVar = self.__new_t_var()

                self.__t_unify(TConst([rt.chd[0].t_var, rt.chd[1].t_var, dummy],
                                      [[TypeSystem.Real.inst(), TypeSystem.Real.inst(), TypeSystem.Real.inst()],
                                       [TypeSystem.Real.inst(), TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst()],
                                       [TypeSystem.Cmplx.inst(), TypeSystem.Real.inst(), TypeSystem.Cmplx.inst()],
                                       [TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst()],
                                       [TypeSystem.Str.inst(), TypeSystem.Str.inst(), TypeSystem.Str.inst()],
                                       [TypeSystem.Bool.inst(), TypeSystem.Bool.inst(), TypeSystem.Bool.inst()]],
                                      [[], [], [], [], [], []]))

                for i in range(len(rt.chd) - 2):
                    prev_dummy: TVar = dummy

                    dummy = self.__new_t_var()
                    self.__t_unify(TConst([rt.chd[0].t_var, rt.chd[i + 2].t_var, prev_dummy, dummy],
                                          [[TypeSystem.Real.inst(), TypeSystem.Real.inst(), TypeSystem.Real.inst(),
                                            TypeSystem.Real.inst()],
                                           [TypeSystem.Real.inst(), TypeSystem.Cmplx.inst(), TypeSystem.Real.inst(),
                                            TypeSystem.Cmplx.inst()],
                                           [TypeSystem.Cmplx.inst(), TypeSystem.Real.inst(), TypeSystem.Real.inst(),
                                            TypeSystem.Cmplx.inst()],
                                           [TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst(), TypeSystem.Real.inst(),
                                            TypeSystem.Cmplx.inst()],
                                           [TypeSystem.Real.inst(), TypeSystem.Real.inst(), TypeSystem.Cmplx.inst(),
                                            TypeSystem.Cmplx.inst()],
                                           [TypeSystem.Real.inst(), TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst(),
                                            TypeSystem.Cmplx.inst()],
                                           [TypeSystem.Cmplx.inst(), TypeSystem.Real.inst(), TypeSystem.Cmplx.inst(),
                                            TypeSystem.Cmplx.inst()],
                                           [TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst(), TypeSystem.Cmplx.inst(),
                                            TypeSystem.Cmplx.inst()],
                                           [TypeSystem.Str.inst(), TypeSystem.Str.inst(), TypeSystem.Str.inst(),
                                            TypeSystem.Str.inst()],
                                           [TypeSystem.Bool.inst(), TypeSystem.Bool.inst(), TypeSystem.Bool.inst(),
                                            TypeSystem.Bool.inst()]], [[], [], [], [], [], [], [], [], [], []]))

                f_var: List[FVar] = self.__new_f_var(4)

                self.__t_unify(TConst([rt.t_var, dummy],
                                      [[List2(TypeSystem.Real.inst(), f_var[0]), TypeSystem.Real.inst()],
                                       [List2(TypeSystem.Cmplx.inst(), f_var[1]), TypeSystem.Cmplx.inst()],
                                       [List2(TypeSystem.Str.inst(), f_var[2]), TypeSystem.Str.inst()],
                                       [List2(TypeSystem.Bool.inst(), f_var[3]), TypeSystem.Bool.inst()]],
                                      [[FConst([f_var[0]], [None])], [FConst([f_var[1]], [None])],
                                       [FConst([f_var[2]], [None])], [FConst([f_var[3]], [None])]]))
        else:
            raise NotImplementedError

    def __find_t(self, var: TVar) -> Set[TypeSystem.T]:
        for const in self.__t_const:
            find: Set[TypeSystem.T] = const[var]

            if find:
                return find

    @classmethod
    def inst(cls) -> TChker:
        if not cls.__inst:
            cls.__inst = TChker()

        return cls.__inst

    def chk_t(self, expr: AST.AST):
        self.__expr = expr

        buf: Type.BufT = Type.BufT.DEBUG  # Debug buffer.

        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('type checking target'), buf)
        Printer.Printer.inst().buf(f'@AST: {expr}', buf, indent=2)
        Printer.Printer.inst().buf_newline(buf)
        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('type checking chain'), buf)

        Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Initializing type checker'), buf, False, 2)
        self.__init()
        Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
        Printer.Printer.inst().buf(f'@__const_l: {len(self.__t_const)} (cleared)', buf, indent=4)
        Printer.Printer.inst().buf_newline(buf)

        Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running type checker'), buf, False, 2)
        self.__expr.rt.t_var = self.__new_t_var()
        self.__chk_t_hlpr(self.__expr.rt)
        Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
        Printer.Printer.inst().buf(f'@AST     : {expr}', buf, indent=4)
        tmp: str = ' or '.join([str(t) for t in self.__find_t(expr.rt.t_var)])
        Printer.Printer.inst().buf(f'@inferred: {tmp}', buf, indent=4)
        Printer.Printer.inst().buf_newline(buf)
