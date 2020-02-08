import datetime
import math
import time
from typing import List, Dict, Optional, Tuple

from Core import Type, Token, SystemManager, Error, Warning
from Util import Printer
from Util.Macro import is_bigint, is_smallint


class Util:
    """
    Utility command toolbox.

    :cvar __sign: Signatures of utility commands.
    """
    __sign: Dict[Type.CmdT, List[Type.Sign]] = {
        Type.CmdT.QUIT: [Type.Sign([], Type.T.TER, Type.CmdT.QUIT)],
        Type.CmdT.HELP: [Type.Sign([], Type.T.TER, Type.CmdT.HELP),
                         Type.Sign([Type.T.STR], Type.T.TER, Type.CmdT.HELP)],
        Type.CmdT.GET_SYS_VAR: [Type.Sign([Type.T.STR], Type.T.STR, Type.CmdT.GET_SYS_VAR)],
        Type.CmdT.SET_SYS_VAR: [Type.Sign([Type.T.STR, Type.T.NUM], Type.T.TER, Type.CmdT.SET_SYS_VAR),
                                Type.Sign([Type.T.STR, Type.T.STR], Type.T.TER, Type.CmdT.SET_SYS_VAR)],
        Type.CmdT.SLEEP: [Type.Sign([Type.T.NUM], Type.T.TER, Type.CmdT.SLEEP)]
    }

    def __init__(self) -> None:
        raise NotImplementedError

    def __del__(self) -> None:
        raise NotImplementedError

    @classmethod
    def chk_t(cls, rt: Token.CmdTok) -> Optional[List[Type.Sign]]:
        """
        Type checker for system commands.
        It checks type of input command token and assigns return type as type information of the token.

        :param rt: Token to be type checked.
        :type rt: Token.FunTok

        :return: None if type check is successful. Candidate signatures if not.
        :rtype: Optional[List[Type.Signature]]
        """
        cand: List[Type.Sign] = cls.__sign.get(rt.v)  # Candidate signatures
        infer: Type.Sign = Type.Sign([tok.t for tok in rt.chd], cand[0].ret_t, rt.v)  # Inferred signature

        # Inferred signature must be one of candidates and return type is TER type.
        if infer in cand:
            rt.t = infer.ret_t

            return None
        else:
            return cand

    @classmethod
    def eval(cls, rt: Token.CmdTok) -> Tuple[Token.Tok, List[Warning.UtilWarn]]:
        warn: List[Warning.UtilWarn] = []
        buf: Type.BufT = Type.BufT.INTERNAL

        if rt.v == Type.CmdT.QUIT:
            # Raise quit exception.
            # This will be handled by main procedure, terminating the whole process.
            raise Error.UtilErr(Type.UtilErrT.QUIT)
        elif rt.v == Type.CmdT.HELP:
            return Token.VoidTok(), warn
        elif rt.v == Type.CmdT.GET_SYS_VAR:
            sys_var: Type.SysVar = SystemManager.SysManager.inst().get_sys_var(rt.chd[0].v)

            # Check whether input is valid.
            # The system variable to get must exist.
            if not sys_var:
                raise Error.UtilErr(Type.UtilErrT.NOT_FOUND, 26, id=rt.chd[0].v)

            # Get.
            return Token.StrTok(str(sys_var.v)), warn
        elif rt.v == Type.CmdT.SET_SYS_VAR:
            prev_v: Type.SysVar = SystemManager.SysManager.inst().get_sys_var(rt.chd[0].v)

            # Check for errors.
            # Set_sys_var command for system variable x generates error for followings cases.
            #   1. x is not existing system variable. (NOT_FOUND)
            #   2. x is read only. (RD_ONLY)
            #   3. Type of system variable and that of x dose not match. (T_MISMATCH)
            # The following logic is an implementation of these rules.
            if not prev_v:
                raise Error.UtilErr(Type.UtilErrT.NOT_FOUND, 26, id=rt.chd[0].v)
            elif prev_v.rd_only:
                raise Error.UtilErr(Type.UtilErrT.RD_ONLY, 28, id=rt.chd[0].v)
            elif prev_v.t != rt.chd[1].t:
                raise Error.UtilErr(Type.UtilErrT.T_MISMATCH, 30, id=rt.chd[0].v, corret_t=prev_v.t,
                                    wrong_t=rt.chd[1].t)

            if rt.chd[0].v in ["Computation_Timeout", "Input_Timeout"]:
                # Check for errors and warnings.
                # Set_sys_var command for timeout limits with second parameter x generates error or warning for
                # followings cases.
                #   1. x is +-inf. (INF_DETECT)
                #   2. x is nan. (NAN_DETECT)
                #   3. x is finite negative. (DOMAIN_OUT)
                #   4. x is 0. (TURN_OFF)
                #   5. x is not in [0, 2147483647]. (DOMAIN_OUT)
                #   6. x is finite positive noninteger. (DOMAIN_OUT)
                # The following logic is an implementation of these rules.
                if is_bigint(rt.chd[1].v):
                    warn.append(Warning.UtilWarn(Type.UtilWarnT.DOMAIN_OUT, 17))
                    rt.chd[1].v = 2147483647
                elif is_smallint(rt.chd[1].v):
                    raise Error.UtilErr(Type.UtilErrT.DOMAIN_OUT, 27)
                elif math.isinf(rt.chd[1].v):
                    if rt.chd[1].v > 0:
                        warn.append(Warning.UtilWarn(Type.UtilWarnT.INF_DETECT, 20))
                        rt.chd[1].v = 0
                    else:
                        raise Error.UtilErr(Type.UtilErrT.INF_DETECT, 27)
                elif math.isnan(rt.chd[1].v):
                    raise Error.UtilErr(Type.UtilErrT.NAN_DETECT, 27)
                elif rt.chd[1].v < 0:
                    raise Error.UtilErr(Type.UtilErrT.DOMAIN_OUT, 27)
                elif rt.chd[1].v == 0:
                    warn.append(Warning.UtilWarn(Type.UtilWarnT.TURN_OFF, 14))
                elif rt.chd[1].v % 1 != 0:
                    warn.append(Warning.UtilWarn(Type.UtilWarnT.DOMAIN_OUT, 13))
                    rt.chd[1].v = max(round(rt.chd[1].v), 1)

                # Set.
                SystemManager.SysManager.inst().set_sys_var(rt.chd[0].v, rt.chd[1].v)

                # Report.
                Printer.Printer.inst().buf(Printer.Printer.inst().f_title('system report'), buf)
                Printer.Printer.inst().buf(f'Updated system variable \"{rt.chd[0].v}\".', buf, indent=2)
                Printer.Printer.inst().buf(f'@target: {rt.chd[0].v}', buf, indent=4)

                if prev_v.v == 0:
                    Printer.Printer.inst().buf('@from  : 0 (Turn off)', buf, indent=4)
                else:
                    Printer.Printer.inst().buf(f'@from  : {prev_v.v}', buf, indent=4)

                if rt.chd[1].v == 0:
                    Printer.Printer.inst().buf(f'@to    : 0 (Turn off)', buf, indent=4)
                else:
                    Printer.Printer.inst().buf(f'@to    : {rt.chd[1].v}', buf, indent=4)

                Printer.Printer.inst().buf_newline(buf)

            return Token.VoidTok(), warn
        else:
            # Check for errors.
            # Set_sys_var command for system variable x generates error for followings cases.
            #   1. x is +-inf. (INF_DETECT)
            #   2. x is nan. (NAN_DETECT)
            #   3. x is not in [0, 100000000.99999]. (DOMAIN_OUT)
            # The following logic is an implementation of these rules.
            if is_bigint(rt.chd[0].v) or is_smallint(rt.chd[0].v):
                raise Error.UtilErr(Type.UtilErrT.DOMAIN_OUT, 29)
            if math.isinf(rt.chd[0].v):
                raise Error.UtilErr(Type.UtilErrT.INF_DETECT, 29)
            elif math.isnan(rt.chd[0].v):
                raise Error.UtilErr(Type.UtilErrT.NAN_DETECT, 29)
            elif not (0 <= rt.chd[0].v <= 100000000.99999):
                raise Error.UtilErr(Type.UtilErrT.DOMAIN_OUT, 29)

            # Sleep.
            start: time = datetime.datetime.now()
            time.sleep(rt.chd[0].v)
            end: time = datetime.datetime.now()

            # Report.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('system report'), buf)
            Printer.Printer.inst().buf(f'Tiny calculator slept for {rt.chd[0].v} seconds.', buf, indent=2)
            Printer.Printer.inst().buf(f'@start: {start}', buf, indent=4)
            Printer.Printer.inst().buf(f'@end  : {end}', buf, indent=4)
            Printer.Printer.inst().buf_newline(buf)

            return Token.VoidTok(), warn
