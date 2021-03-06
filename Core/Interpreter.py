from __future__ import annotations

from typing import Dict, List

from Core import AST, Type, Token, TypeSystem
from Error import *
from Util import Printer
from Operator import *


class Interp:
    """
    Type check AST and interpret it.

    This class is implemented as singleton.
    For the concept of singleton pattern, consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Singleton_pattern

    :cvar __inst: Singleton object.

    :ivar __expr: AST to be interpreted.
    :ivar __line: Original user input string.
    """
    __inst: Interp = None
    __t_env: Dict[int, TypeSystem.T] = {2: 3}

    def __init__(self) -> None:
        self.__expr: AST.AST = None
        self.__line: str = ''

    def __chk_t(self) -> None:
        """
        Check type of AST.

        It just calls its helper ``Interp.__chk_t_hlpr``.
        For detailed description of simplification, refer to the comments in ``Interp.__chk_t_hlpr``.

        This method is private and called internally as the first step of interpreting chain.
        For detailed description for interpreting chain, refer to the comments of ``Interp.interp``.
        """
        self.__chk_t_hlpr(self.__expr.rt, self.__t_env)

    def __chk_t_hlpr(self, rt: Token.Tok, t_env: Dict[int, TypeSystem.T]) -> Dict[int, TypeSystem.T]:
        """
        Check type of partial AST.

        Usually, type checking is quite tricky logic.
        For example, Hindley-Milner let type system needs unification algorithms for type checking.
        But since grammar of math expression is simple, type checking logic is relatively simple.

        It just calls corresponding type checking methods by looking up the value of root token.
        After checking type, it assign inferred type of root token as its field value.
        For concept of Hindley-Milner let type system and unification algorithm, consult the references below.

        This method is private and called internally as a helper of ``Interp.__chk_t``.

        **Reference**
            * https://en.wikipedia.org/wiki/Hindley–Milner_type_system
            * https://en.wikipedia.org/wiki/Unification_(computer_science)

        :param rt: Root of partial AST to be typed checked.
        :type rt: Token.Tok
        """
        tok_t: type = type(rt)

        if tok_t == Token.Num:
            rt.t = TypeSystem.Cmplx.inst() if type(rt.v) == complex else TypeSystem.Real.inst()

            return t_env
        elif tok_t == Token.Str:
            rt.t = TypeSystem.Str.inst()

            return t_env
        elif tok_t == Token.Bool:
            rt.t = TypeSystem.Bool.inst()

            return t_env
        elif tok_t == Token.Void:
            rt.t = TypeSystem.Void.inst()

            return t_env
        elif tok_t == Token.Var:
            # find: TypeSystem.T = t_env.get(rt.v)

            rt.t = TypeSystem.Sym.inst()

            return t_env
        elif tok_t == Token.List:
            chd_t: List[TypeSystem.T] = []

            for tok in rt.chd:
                t_env = self.__chk_t_hlpr(tok, t_env)
                chd_t.append(tok.t)

            res_t: TypeSystem.T = TypeSystem.ArrFact.inst().get_arr_t(chd_t)

            if not res_t:
                raise Exception('type error')

            rt.t = res_t

            return t_env
        elif tok_t == Token.Op:
            for tok in rt.chd:
                t_env = self.__chk_t_hlpr(tok, t_env)

            t_env = rt.v.chk_t(rt, t_env)

            if not t_env:
                raise InterpreterError.TErr(23, *self.__expr.str_pos(rt), rt, rt.v.sgn(), rt.v.__name__.upper())

            return t_env
        else:
            for tok in rt.chd:
                t_env = self.__chk_t_hlpr(tok, t_env)

            rt.t = TypeSystem.Sym()

            return t_env

    def __debug_hlpr(self, rt: Token.Tok, cnt: int) -> int:
        buf: Type.BufT = Type.BufT.DEBUG  # Debug buffer.
        tok_t: type = type(rt)

        if tok_t == Token.Op:
            for tok in rt.chd:
                cnt = self.__debug_hlpr(tok, cnt)

            if rt.v in [Unary.Plus, Unary.Minus, Bool.Neg]:
                t_str: str = f'{rt.v.sym()}{rt.chd[0].t} -> {rt.t}'
            elif rt.v == Unary.Trans:
                t_str: str = f'{rt.chd[0].t}{rt.v.sym()} -> {rt.t}'
            elif rt.v == Delimiter.Seq:
                if rt.argc == 2:
                    t_str: str = f'{rt.chd[0].t}:{rt.chd[1].t} -> {rt.t}'
                else:
                    t_str: str = f'{rt.chd[0].t}:{rt.chd[1].t}:{rt.chd[1].t} -> {rt.t}'
            elif rt.v == Delimiter.Idx:
                t_str: str = f'{rt.chd[0].t}[' + ', '.join([str(tok.t) for tok in rt.chd[1:]]) + f'] -> {rt.t}'
            else:
                t_str: str = f'{rt.chd[0].t} {rt.v.sym()} {rt.chd[1].t} -> {rt.t}'
        elif tok_t == Token.Fun:
            for tok in rt.chd:
                cnt = self.__debug_hlpr(tok, cnt)

            t_str: str = f'{rt.v_str()}[' + ', '.join([str(tok.t) for tok in rt.chd]) + f'] -> {rt.t}'
        elif tok_t == Token.List:
            for tok in rt.chd:
                cnt = self.__debug_hlpr(tok, cnt)

            t_str: str = '{' + ', '.join([str(tok.t) for tok in rt.chd]) + '}' + f' -> {rt.t}'
        else:
            t_str: str = str(rt.t)

        Printer.Printer.inst().buf(f'[{cnt}]', buf, indent=4)
        Printer.Printer.inst().buf(f'@partial AST: {AST.AST(rt)}', buf, indent=6)
        Printer.Printer.inst().buf(f'@inferred   : {t_str}', buf, indent=6)
        Printer.Printer.inst().buf_newline(buf)

        return cnt + 1

    # def __simplify(self) -> None:
    #     """
    #     Simplify AST.
    #
    #     It just calls its helper ``Interp.__simplify_hlpr``.
    #     For detailed description of simplification, refer to the comments in ``Interp.__simplify_hlpr``.
    #
    #     This method is private and called internally as the second step of interpreting chain.
    #     For detailed description for interpreting chain, refer to the comments of ``Interp.interp``.
    #     """
    #     self.__expr.rt = self.__simplify_hlpr(self.__expr.rt, None)
    #
    # def __simplify_hlpr(self, rt: Token.Tok, prn: Token.Tok) -> Token.Tok:
    #     """
    #     Simplify partial AST.
    #
    #     It does following simplifications.
    #         1. Constant folding.
    #         2. Sign propagation.
    #         3. Dead expression stripping.
    #         4. Hoisting.
    #         5. Packing.
    #         6. Unpacking.
    #         7. Function coalescing.
    #     Most of these simplification tricks are originally part of compiler optimization, virtual memory management, and
    #     programing language scheme.
    #     It just calls corresponding simplifying methods by looking up the value of root token.
    #     For detailed description and examples of each trick, consult following references and comments of
    #     ``Op.simplify`` and ``Tri.simplify``.
    #
    #     This method is private and called internally as a helper of ``Interp.__simplify``.
    #
    #     **Reference**
    #         * https://en.wikipedia.org/wiki/Constant_folding
    #         * https://en.wikipedia.org/wiki/Dead_code_elimination
    #         * https://developer.mozilla.org/ko/docs/Glossary/Hoisting
    #         * https://en.wikipedia.org/wiki/Coalescing_(computer_science)
    #
    #     :param rt: Root of partial AST to be simplified.
    #     :type rt: Token.Tok
    #     :param prn: Parent of root of partial AST to be simplified.
    #     :type prn: Token.Tok
    #
    #     :return: Root of simplified partial AST.
    #     :rtype: Token.Tok
    #     """
    #     if rt.tok_t in [Type.TokT.NUM, Type.TokT.VAR, Type.TokT.STR, Type.TokT.VOID]:
    #         return rt
    #     elif rt.tok_t == Type.TokT.OP:
    #         rt.chd = [self.__simplify_hlpr(tok, rt) for tok in rt.chd]
    #         simple, warn = Operator.Op.pck(rt, prn)
    #
    #         for it in warn:
    #             WarningManager.WarnManager.inst().push(it)
    #
    #         return simple
    #     elif rt.tok_t == Type.TokT.FUN:
    #         rt.chd = [self.__simplify_hlpr(tok, rt) for tok in rt.chd]
    #
    #         if rt.v in [Type.FunT.Sin, Type.FunT.Cos, Type.FunT.Tan, Type.FunT.Csc, Type.FunT.Sec, Type.FunT.Cot,
    #                     Type.FunT.ArcSin, Type.FunT.ArcCos, Type.FunT.ArcTan, Type.FunT.ArcCsc, Type.FunT.ArcSec,
    #                     Type.FunT.ArcCot]:
    #             simple, warn = Trigonometric.TriFun.simplify(rt)
    #         elif rt.v in [Type.FunT.Sinh, Type.FunT.Cosh, Type.FunT.Tanh, Type.FunT.Csch, Type.FunT.Sech,
    #                       Type.FunT.Coth, Type.FunT.ArcSinh, Type.FunT.ArcCosh, Type.FunT.ArcTanh, Type.FunT.ArcCsch,
    #                       Type.FunT.ArcSech, Type.FunT.ArcCoth]:
    #             simple, warn = Hyperbolic.HypbolicFunc.simplify(rt)
    #         elif rt.v in [Type.FunT.Exp, Type.FunT.Log, Type.FunT.Pow, Type.FunT.Sqrt, Type.FunT.Log2, Type.FunT.Log10]:
    #             simple, warn = Exponential.ExpFun.simplify(rt)
    #         else:
    #             simple, warn = SpecialFunction.SpecialFun.simplify(rt)
    #
    #         for it in warn:
    #             WarningManager.WarnManager.inst().push(it)
    #
    #         return simple
    #     else:
    #         rt.chd = [self.__simplify_hlpr(tok, rt) for tok in rt.chd]
    #
    #         return rt
    #
    # def __eval(self) -> bool:
    #     """
    #     Evaluate AST and return whether further evaluation is needed.
    #
    #     It just calls its helper ``Interp.__eval_hlpr``.
    #     For detailed description of evaluation, refer to the comments in ``Interp.__eval_hlpr``.
    #
    #     This method is private and called internally as the fourth of interpreting chain.
    #     For detailed description for interpreting chain, refer to the comments of ``Interp.interp``.
    #
    #     :return: True if there is need of further evaluation. False otherwise.
    #     :rtype: bool
    #     """
    #     evaled, done = self.__eval_hlpr(self.__expr.rt)
    #     self.__expr.rt = evaled
    #
    #     return done
    #
    # def __eval_hlpr(self, rt: Token.Tok) -> Tuple[Token.Tok, bool]:
    #     """
    #     Evaluate partial AST and return whether further evaluation is needed.
    #
    #     It just calls corresponding evaluation methods by looking up the value of root token.
    #     Note that it only evaluates command at the lowest level of AST, not all.
    #
    #     This method is private and called internally as a helper of ``Interp.__eval``.
    #
    #     :param rt: Root of partial AST to be evaluated.
    #     :type rt: Token.Tok
    #
    #     :return: Root of evaluated partial AST and flag for further evaluation.
    #              The flag is true if there is need of further evaluation, and false otherwise.
    #     :rtype: Tuple[Token.Tok, bool]
    #     """
    #     if rt.tok_t in [Type.TokT.NUM, Type.TokT.VAR, Type.TokT.STR, Type.TokT.VOID]:
    #         return rt, False
    #     elif rt.tok_t in [Type.TokT.OP, Type.TokT.FUN]:
    #         done: bool = False
    #
    #         for i in range(len(rt.chd)):
    #             evaled, tmp = self.__eval_hlpr(rt.chd[i])
    #             done |= tmp
    #             rt.swap_chd(evaled, i)
    #
    #         return rt, done
    #     else:
    #         done: bool = False
    #
    #         for i in range(len(rt.chd)):
    #             evaled, tmp = self.__eval_hlpr(rt.chd[i])
    #             done |= tmp
    #             rt.swap_chd(evaled, i)
    #
    #         if done:
    #             return rt, done
    #
    #         if rt.v in [Type.CmdT.HELP, Type.CmdT.QUIT, Type.CmdT.SET_SYS_VAR, Type.CmdT.GET_SYS_VAR, Type.CmdT.SLEEP]:
    #             evaled, warn = Utility.Util.eval(rt)
    #
    #             for it in warn:
    #                 WarningManager.WarnManager.inst().push(it)
    #
    #             return evaled, True

    @classmethod
    def inst(cls) -> Interp:
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Interp
        """
        if not cls.__inst:
            cls.__inst = Interp()

        return cls.__inst

    def interp(self, expr: AST.AST, debug: bool = False) -> AST.AST:
        """
        Type check AST and interpret it.

        Interpreting is recursive procedure comprised of 5 steps.
            1. Type check AST.
               Run type checker on AST, filtering type errors before evaluating it.
            2. Simplify AST.
               After simplification, AST becomes much simpler, lightening burden of evaluation.
            3. Check whether further evaluation is needed.
               If further evaluation is not needed, interpreting chain stops here, returning fully interpreted AST.
               Note that returning AST may not be single NUM token.
            4. Evaluate AST partially.
               With simplified AST, it evaluates CMD tokens in AST partially.
               Here, partially means that it only evaluates CMD tokens at the lowest level of AST, not all of them.
               This is because after partial evaluation, further simplification may be possible.
            5. Move to step 2 and repeat.

        By step 5, there is a danger of infinite loop.
        Further, evaluation may tak very long time.
        Thus there is a timeout limit of this recursive loop, which is defined as system variable
        ``Computation_Timeout``.
        This timeout limit can be customized using ``Set_sys_var`` command.

        This method supports brief summary outputs which can be used for debugging or generation of debug set.

        :param expr: AST to be interpreted.
        :type expr: AST.AST
        :param debug: Flag for debug mode. (Default: False)
        :type debug: bool

        :return: Interpreted AST.
        :rtype: AST.AST
        """
        self.__expr = expr
        self.__line = expr.line

        if debug:
            buf: Type.BufT = Type.BufT.DEBUG  # Debug buffer.

            # Print out interpreting target.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('interpreting target'), buf)
            Printer.Printer.inst().buf(f'@AST: {expr}', buf, indent=2)
            Printer.Printer.inst().buf_newline(buf)
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('interpreting chain'), buf)
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running type checker'), buf, False, 2)

            # Run type checker.
            try:
                self.__chk_t()
            except Error.InterpErr as interpreter_err:
                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)
                Printer.Printer.inst().buf_newline(buf)

                raise interpreter_err
            else:
                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)

            self.__debug_hlpr(expr.rt, 0)

            Printer.Printer.inst().buf_newline(buf)
            #
            # iter: int = 1  # Interpretation loop counter.
            #
            # try:
            #     with SystemManager.timeout(SystemManager.SysManager.inst().get_sys_var('Computation_Timeout').v):
            #         while True:
            #             # Run simplifier.
            #             Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running simplifier'), buf, False, 2)
            #
            #             try:
            #                 self.__simplify()
            #             except Error.InterpErr as interpreter_err:
            #                 Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)
            #                 Printer.Printer.inst().buf_newline(buf)
            #
            #                 raise interpreter_err
            #             else:
            #                 Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
            #
            #             Printer.Printer.inst().buf(f'@simplified: {self.__expr.infix()}', buf, indent=4)
            #             Printer.Printer.inst().buf_newline(buf)
            #
            #             # Evaluate.
            #             Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Evaluating AST'), buf, False, 2)
            #
            #             try:
            #                 cont: bool = self.__eval()
            #             except Error.UtilErr as util_err:
            #                 if util_err.t == Type.UtilErrT.QUIT:
            #                     Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
            #                 else:
            #                     Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)
            #
            #                 Printer.Printer.inst().buf_newline(buf)
            #                 raise util_err
            #             except Error.Err as err:
            #                 Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)
            #                 Printer.Printer.inst().buf_newline(buf)
            #
            #                 raise err
            #             else:
            #                 Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
            #
            #             Printer.Printer.inst().buf(f'@evaluated: {self.__expr.infix()}', buf, indent=4)
            #
            #             if not cont:
            #                 # If there is no need of further evaluation, return.
            #
            #                 Printer.Printer.inst().buf('@continue : False', buf, indent=4)
            #                 Printer.Printer.inst().buf(f'@iter     : {iter}', buf, indent=4)
            #                 Printer.Printer.inst().buf_newline(buf)
            #
            #                 return self.__expr
            #
            #             Printer.Printer.inst().buf('@continue : True', buf, indent=4)
            #             Printer.Printer.inst().buf_newline(buf)
            #
            #             iter += 1
            #
            # except Error.SysErr as sys_err:
            #     # In case of timeout, clear global data structures manipulated so far to avoid async errors.
            #     Printer.Printer.inst().clr(Type.BufT.DEBUG)
            #     Printer.Printer.inst().clr(Type.BufT.INTERNAL)
            #     WarningManager.WarnManager.inst().clr()
            #     sys_err.iter = iter
            #     sys_err.err_no = 24
            #
            #     raise sys_err
        else:
            self.__chk_t()

            # try:
            #     with SystemManager.timeout(SystemManager.SysManager.inst().get_sys_var('Computation_Timeout').v):
            #         iter: int = 1  # Interpretation loop counter.
            #
            #         while True:
            #             self.__simplify()
            #
            #             if not self.__eval():
            #                 return self.__expr
            #
            #             iter += 1
            # except Error.SysErr as sys_err:
            #     sys_err.iter = iter
            #     sys_err.err_no = 24
            #
            #     raise sys_err
