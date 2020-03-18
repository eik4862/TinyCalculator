from __future__ import annotations

import math
from typing import List, final, Union, Dict

from Core import Token, AST, Type, WarningManager
from Error import *
from Warning import *
from Operator import *
from Function import *
from Util import Printer
from Util.Macro import *


@final
class Parser:
    """
    Parse user input string to generate AST(Abstract Syntax Tree).

    This class is implemented as singleton.
    For the concept of AST and singleton pattern, consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Abstract_syntax_tree
        * https://en.wikipedia.org/wiki/Singleton_pattern

    :cvar __inst: Singleton object.

    :ivar __line: Original user input string.
    :ivar __infix: Storage for tokens in infix order.
    :ivar __postfix: Storage for tokens in postfix order.
    :ivar __tmp_stk: Temporary stack for infix to postfix conversion and AST generation.
    """
    __inst: Parser = None
    __kword_tb: Dict[str, Union[float, bool, Function.Fun]] = {}

    def __init__(self) -> None:
        self.__line: str = ''
        self.__infix: List[Token.Tok] = []
        self.__postfix: List[Token.Tok] = []
        self.__tmp_stk: List[Token.Tok] = []

        for fun_category in Function.Fun.__subclasses__():
            for fun in fun_category.__subclasses__():
                self.__kword_tb[fun.__name__] = fun

        for const in Type.Const:
            self.__kword_tb[const.name] = const.value

        self.__kword_tb['True'] = True
        self.__kword_tb['False'] = False

    def __init(self) -> None:
        """
        Initialize parser.

        Clear internal buffers to store tokens.
        This method is private and called internally as the first step of parsing chain.
        For detailed description for parsing chain, refer to the comments of ``Parser.parse``.
        """
        self.__infix.clear()
        self.__postfix.clear()

    def __lexer(self) -> None:
        """
        Lexer(lexical analyzer) for parsing.

        Read character from target string one by one and tokenize it properly.
        Further, it checks the syntax of input using ``Parser.__add_tok``.
        For detailed description for syntax checking, refer to the comments of ``Parser.__add_tok``.

        This method is private and called internally as the second step of parsing chain.
        For detailed description for parsing chain, refer to the comments of ``Parser.parse``.

        :raise BIG_INT: If parsed integer is bigger than the maximum float size.
        :raise OVERFLOW: If parsed float caused overflow.

        :raise INVALID_EXPR: If the input string is invalid expression.
        :raise INVALID_TOK: If unknown token is encountered.
        :raise EMPTY_EXPR: If the input expression is void.
        """
        pos: int = 0  # Current position at the string to be tokenized.

        while pos < len(self.__line):
            if is_white(self.__line[pos]):
                # Skip all white spaces
                while pos < len(self.__line) and is_white(self.__line[pos]):
                    pos += 1
            elif is_digit(self.__line[pos]):
                # Parsing numeric value with integer part comprises of four steps.
                #   1. Parse integer part.
                #   2. Check for decimal point and parse fractional part.
                #   3. Check for additional exponentation and parse exponent.
                #   4. Check for imaginary unit and parse it.
                # There are following restriction for numeric value literals.
                #   1. Decimal point cannot appear more than once.
                #   2. Additional exponentation must be followed by integer.
                #   3. There can be only one sign after additional exponentation.
                #   4. Imaginary unit, if exists, must be the terminal of the numeric value.
                # This logic generates warning in following cases.
                #   1. If the parsed integer part is too big so that it cannot be casted to float, it generates BIT_INT
                #      warning.
                #   2. If overflow occurs, it generates OVERFLOW warning.
                # The following logic is an implementation of these steps, restriction rules, and warning generation
                # rules.
                start: int = pos  # Starting position.

                # Parse integer part.
                while pos < len(self.__line) and is_digit(self.__line[pos]):
                    pos += 1

                if pos == len(self.__line) or not (
                        is_dot(self.__line[pos]) or is_exp(self.__line[pos]) or is_imag(self.__line[pos])):
                    # If there is nothing more, we are done.
                    parsed: int = int(self.__line[start:pos])  # Parsed numeric.

                    if is_bigint(parsed):
                        WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(58, start))

                    self.__add_tok(Token.Num(parsed, start))

                    continue
                elif is_dot(self.__line[pos]):
                    # If there is decimal point, parse fractional part.
                    pos += 1

                    # Parse fractional part.
                    while pos < len(self.__line) and is_digit(self.__line[pos]):
                        pos += 1

                    if pos == len(self.__line) or not (
                            is_dot(self.__line[pos]) or is_exp(self.__line[pos]) or is_imag(self.__line[pos])):
                        # If there is no additional exponentation, stop.
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(parsed, start))

                        continue
                    elif is_dot(self.__line[pos]):
                        # Decimal point cannot appear more than once.
                        pos -= 1
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(parsed, start))
                    elif is_exp(self.__line[pos]):
                        # If there is additional exponentation, parse exponent.
                        pos += 1

                        # Additional exponent must be followed by integer.
                        if pos == len(self.__line):
                            pos -= 1
                            parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                            if math.isinf(parsed):
                                WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                            self.__add_tok(Token.Num(parsed, start))

                            continue
                        elif is_sgn(self.__line[pos]):
                            if pos + 1 == len(self.__line[pos]) or not is_digit(self.__line[pos + 1]):
                                pos -= 1
                                parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                                if math.isinf(parsed):
                                    WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                                self.__add_tok(Token.Num(parsed, start))

                                continue

                            pos += 1
                        elif not is_digit(self.__line[pos]):
                            pos -= 1
                            parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                            if math.isinf(parsed):
                                WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                            self.__add_tok(Token.Num(parsed, start))

                            continue

                        # Parse additional exponent.
                        while pos < len(self.__line) and is_digit(self.__line[pos]):
                            pos += 1

                        if pos == len(self.__line) or not is_imag(self.__line[pos]):
                            # If there is nothing more, we are done.
                            parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                            if math.isinf(parsed):
                                WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                            self.__add_tok(Token.Num(parsed, start))

                            continue
                        else:
                            # If there is imaginary unit, parse it.
                            parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                            if math.isinf(parsed):
                                WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                            self.__add_tok(Token.Num(complex(0, parsed), start))
                            pos += 1

                            continue
                    else:
                        # If there is imaginary unit, parse it.
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(complex(0, parsed), start))
                        pos += 1

                        continue
                elif is_exp(self.__line[pos]):
                    # If there is additional exponentation, parse exponent.
                    pos += 1

                    # Additional exponent must be followed by integer.
                    if pos == len(self.__line):
                        pos -= 1
                        parsed: int = int(self.__line[start:pos])  # Parsed numeric.

                        if is_bigint(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(58, start))

                        self.__add_tok(Token.Num(parsed, start))

                        continue
                    elif is_sgn(self.__line[pos]):
                        if pos + 1 == len(self.__line[pos]) or not is_digit(self.__line[pos + 1]):
                            pos -= 1
                            parsed: int = int(self.__line[start:pos])  # Parsed numeric.

                            if is_bigint(parsed):
                                WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(58, start))

                            self.__add_tok(Token.Num(parsed, start))

                            continue

                        pos += 1
                    elif not is_digit(self.__line[pos]):
                        pos -= 1
                        parsed: int = int(self.__line[start:pos])  # Parsed numeric.

                        if is_bigint(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(58, start))

                        self.__add_tok(Token.Num(parsed, start))

                        continue

                    # Parse additional exponent.
                    while pos < len(self.__line) and is_digit(self.__line[pos]):
                        pos += 1

                    if pos == len(self.__line) or not is_imag(self.__line[pos]):
                        # If there is nothing more, we are done.
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(parsed, start))

                        continue
                    else:
                        # If there is imaginary unit, parse it.
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(complex(0, parsed), start))
                        pos += 1

                        continue
                else:
                    # If there is imaginary unit, parse it.
                    parsed: int = int(self.__line[start:pos])  # Parsed numeric.

                    if is_bigint(parsed):
                        WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))
                        parsed = math.inf

                    self.__add_tok(Token.Num(complex(0, parsed), start))
                    pos += 1

                    continue
            elif is_dot(self.__line[pos]):
                # Parsing numeric value w/o integer part comprises of three steps.
                #   1. Parse fractional part.
                #   2. Check for additional exponentation and parse exponent.
                #   3. Check for imaginary unit and parse it.
                # There are following restriction for numeric value literals.
                #   1. Decimal point cannot appear more than once.
                #   2. Additional exponentation must be followed by integer.
                #   3. There can be only one sign after additional exponentation.
                #   4. Imaginary unit, if exists, must be the terminal of the numeric value.
                # This logic generates warning in following cases.
                #   1. If overflow occurs, it generates OVERFLOW warning.
                # The following logic is an implementation of these steps, restriction rules, and warning generation
                # rules.
                start: int = pos  # Starting position.
                pos += 1

                if pos == len(self.__line) or not is_digit(self.__line[pos]):
                    raise ParserError.InvalidTok(2, self.__line, start)

                # Parse fractional part.
                while pos < len(self.__line) and is_digit(self.__line[pos]):
                    pos += 1

                if pos == len(self.__line) or not (
                        is_dot(self.__line[pos]) or is_exp(self.__line[pos]) or is_imag(self.__line[pos])):
                    # If there is no additional exponentation, stop.
                    self.__add_tok(Token.Num(float(self.__line[start:pos]), start))

                    continue
                elif is_dot(self.__line[pos]):
                    # Decimal point cannot appear more than once.
                    parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                    if math.isinf(parsed):
                        WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                    self.__add_tok(Token.Num(parsed, start))
                elif is_exp(self.__line[pos]):
                    # If there is additional exponentation, parse exponent.
                    pos += 1

                    # Additional exponent must be followed by integer.
                    if pos == len(self.__line):
                        pos -= 1
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(parsed, start))

                        continue
                    elif is_sgn(self.__line[pos]):
                        if pos + 1 == len(self.__line[pos]) or not is_digit(self.__line[pos + 1]):
                            pos -= 1
                            parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                            if math.isinf(parsed):
                                WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                            self.__add_tok(Token.Num(parsed, start))

                            continue

                        pos += 1
                    elif not is_digit(self.__line[pos]):
                        pos -= 1
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(parsed, start))

                        continue

                    # Parse additional exponent.
                    while pos < len(self.__line) and is_digit(self.__line[pos]):
                        pos += 1

                    if pos == len(self.__line) or not is_imag(self.__line[pos]):
                        # If there is nothing more, we are done.
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(parsed, start))

                        continue
                    else:
                        # If there is imaginary unit, parse it.
                        parsed: float = float(self.__line[start:pos])  # Parsed numeric.

                        if math.isinf(parsed):
                            WarningManager.WarnManager.inst().push(ParserWarning.NumWarn(59, start))

                        self.__add_tok(Token.Num(complex(0, parsed), start))
                        pos += 1

                        continue
                else:
                    self.__add_tok(Token.Num(complex(0, float(self.__line[start:pos])), start))
                    pos += 1

                    continue
            elif is_alpha(self.__line[pos]):
                # Parse function/command/constant/variable.
                # Variable name has following rules.
                #   1. It consists of alphabets, digits, and underscore.
                #   2. It must start with alphabet.
                #   3. It cannot terminate with underscore.
                # Since it cannot determine whether it means boolean/function/command/constant/variable, it searches
                # for DB after parsing.
                # For efficiency, parsed string for variable will be hashed.
                start: int = pos  # Starting position.
                pos += 1

                while (pos < len(self.__line) and (
                        is_alpha(self.__line[pos]) or is_digit(self.__line[pos]) or is_underscore(self.__line[pos]))):
                    pos += 1

                if is_underscore(self.__line[pos - 1]):
                    pos -= 1

                # Check whether parsed symbol is function.
                find: Union[float, bool, Function.Fun] = self.__kword_tb.get(self.__line[start:pos])

                if type(find) == bool:
                    self.__add_tok(Token.Bool(find, start))
                elif type(find) == float:
                    self.__add_tok(Token.Num(find, start))
                elif type(find) == type:
                    self.__add_tok(Token.Fun(find, start))
                else:
                    str_hash: int = hash(self.__line[start:pos])  # Hash value of parsed string.

                    self.__add_tok(Token.Var(str_hash, start))

                    if not AST.AST.var_name(str_hash):
                        AST.AST.add_var(str_hash, self.__line[start:pos])

                continue
            elif is_quote(self.__line[pos]):
                # Parse string.
                # Note that string must be enclosed by double quote.
                # Also, following escaping sequences should be handled.
                #   1. \n for newline.
                #   2. \t for tab.
                #   3. \\ for backslash.
                #   4. \" for double quote.
                start: int = pos  # Starting position.
                pos += 1
                parsed: str = ''

                while pos < len(self.__line) and not is_quote(self.__line[pos]):
                    if self.__line[pos] == '\\':
                        # Handle escaping sequence by lookahead one character.
                        if pos + 1 == len(self.__line):
                            raise ParserError.InvalidExpr(32, self.__line, pos)

                        if self.__line[pos + 1] == 'n':
                            parsed += '\n'
                        elif self.__line[pos + 1] == 't':
                            parsed += '\t'
                        elif self.__line[pos + 1] == '\\':
                            parsed += '\\'
                        elif self.__line[pos + 1] == '"':
                            parsed += '"'
                        else:
                            raise ParserError.InvalidExpr(32, self.__line, pos)

                        pos += 1
                    else:
                        parsed += self.__line[pos]

                    pos += 1

                # Double quote must be closed.
                if pos == len(self.__line):
                    raise ParserError.InvalidExpr(1, self.__line, start)

                self.__add_tok(Token.Str(parsed, start))
                pos += 1

                continue
            else:
                # Parse operator.
                # Some notes to make.
                #   1. It cannot determine whether + means Add or Plus.
                #      Just try as Add token and let ``Parser.__add_tok`` to determine this.
                #   2. It cannot determine whether - means Sub or Minus.
                #      Just try as Sub token and let ``Parser.__add_tok`` to determine this.
                #   3. It cannot determine whether [ and ] are used as function call or indexing operation.
                #      It will be determined by ``Parser.__infix_to_postfix`` later.
                #   4. It cannot determine whether : is binary or ternary operator.
                #      Just try as binary operator and let ``Parser.__infix_to_postfix`` to determine this.
                if self.__line[pos] == '+':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Assign.AddAsgn, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Binary.Add, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '-':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Assign.SubAsgn, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Binary.Sub, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '*':
                    if pos + 2 < len(self.__line) and self.__line[pos + 1:pos + 3] == '*=':
                        self.__add_tok(Token.Op(Assign.PowAsgn, pos))
                        pos += 3
                    elif pos + 1 < len(self.__line):
                        if self.__line[pos + 1] == '*':
                            self.__add_tok(Token.Op(Binary.Pow, pos))
                            pos += 2
                        elif self.__line[pos + 1] == '=':
                            self.__add_tok(Token.Op(Assign.MulAsgn, pos))
                            pos += 2
                        else:
                            self.__add_tok(Token.Op(Binary.Mul, pos))
                            pos += 1
                    else:
                        self.__add_tok(Token.Op(Binary.Mul, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '/':
                    if pos + 2 < len(self.__line) and self.__line[pos + 1: pos + 3] == '/=':
                        self.__add_tok(Token.Op(Assign.QuotAsgn, pos))
                        pos += 3
                    if pos + 1 < len(self.__line):
                        if self.__line[pos + 1] == '=':
                            self.__add_tok(Token.Op(Assign.DivAsgn, pos))
                            pos += 2
                        elif self.__line[pos + 1] == '/':
                            self.__add_tok(Token.Op(Binary.Quot, pos))
                            pos += 2
                        else:
                            self.__add_tok(Token.Op(Binary.Div, pos))
                            pos += 1
                    else:
                        self.__add_tok(Token.Op(Binary.Div, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '%':
                    if pos + 3 < len(self.__line) and self.__line[pos + 1:pos + 4] == '*%=':
                        self.__add_tok(Token.Op(Assign.MatMulAsgn, pos))
                        pos += 4
                    elif pos + 2 < len(self.__line) and self.__line[pos + 1:pos + 3] == '*%':
                        self.__add_tok(Token.Op(Binary.MatMul, pos))
                        pos += 3
                    elif pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Assign.RemAsgn, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Binary.Rem, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '\'':
                    self.__add_tok(Token.Op(Unary.Trans, pos))
                    pos += 1

                    continue
                elif self.__line[pos] == '!':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Compare.Diff, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Bool.Neg, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '&':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Assign.AndAsgn, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Bool.And, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '|':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Assign.OrAsgn, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Bool.Or, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '^':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Assign.XorAsgn, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Bool.Xor, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '<':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Compare.Geq, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Compare.Abv, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '>':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Compare.Leq, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Compare.Blw, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '=':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '=':
                        self.__add_tok(Token.Op(Compare.Eq, pos))
                        pos += 2
                    else:
                        self.__add_tok(Token.Op(Assign.Asgn, pos))
                        pos += 1

                    continue
                elif self.__line[pos] == '(':
                    self.__add_tok(Token.Op(Delimiter.Lpar, pos))
                    pos += 1

                    continue
                elif self.__line[pos] == ')':
                    self.__add_tok(Token.Op(Delimiter.Rpar, pos))
                    pos += 1

                    continue
                elif self.__line[pos] == '[':
                    self.__add_tok(Token.Op(Delimiter.SqrLpar, pos))
                    pos += 1

                    continue
                elif self.__line[pos] == ']':
                    self.__add_tok(Token.Op(Delimiter.SqrRpar, pos))
                    pos += 1

                    continue
                elif self.__line[pos] == '{':
                    self.__add_tok(Token.Op(Delimiter.CrlLpar, pos))
                    pos += 1

                    continue
                elif self.__line[pos] == '}':
                    self.__add_tok(Token.Op(Delimiter.CrlRpar, pos))
                    pos += 1

                    continue
                elif self.__line[pos] == ':':
                    self.__add_tok(Token.Op(Delimiter.Seq, pos))
                    pos += 1

                    continue
                elif self.__line[pos] == ',':
                    self.__add_tok(Token.Op(Delimiter.Com, pos))
                    pos += 1

                    continue

                # Unknown token is encountered.
                raise ParserError.InvalidTok(2, self.__line, pos)

        # Check whether expression is void.
        if not self.__infix:
            raise ParserError.EmptyExpr(3)

        # By adding terminal token, check terminal condition of expression.
        self.__add_tok(Token.Ter())

    def __add_tok(self, tok: Token.Tok) -> None:
        """
        Add token to internal buffer.

        Before it adds token, it checks the syntax.
        If it detects syntax error, it raises exception.
        Further, based on the previously added token, it determines whether +/- are Plus/Minus or Add/Sub, resp.
        And based on the previously added token again, it detects the need of implicit multiplication and adds * between
        them to make it explicit.

        This method is private and called internally as a helper of ``Parser.__lexer``.
        For detailed description for lexing, refer to the comments of ``Parser.__lexer``.

        :param tok: Token to be added.
        :type tok: Token.Tok

        :raise INVALID_EXPR: If the input string is invalid expression.
        """
        curr_t: type = type(tok)  # Token type of token to be added.
        curr_v = tok.v  # Token value of token to be added.

        # Starting condition for expression is as follows.
        #   1. It can start with any of Num/Var/Fun/Str/Bool token.
        #   2. It can start with Add/Sub/Neg/Lpar/CrlLpar token.
        #      But Add/Sub here means Plus/Minus, resp.
        # All other cases are illegal.
        # The following logic is an implementation of these rules.
        if not self.__infix:
            if curr_t == Token.Op:
                if curr_v == Binary.Add:
                    tok.v = Unary.Plus
                    self.__infix.append(tok)

                    return
                elif curr_v == Binary.Sub:
                    tok.v = Unary.Minus
                    self.__infix.append(tok)

                    return
                elif curr_v in [Bool.Neg, Delimiter.Lpar, Delimiter.CrlLpar]:
                    self.__infix.append(tok)

                    return
                else:
                    raise ParserError.InvalidExpr(7, self.__line, tok.pos)
            else:
                self.__infix.append(tok)

                return

        prev_t: type = type(self.__infix[-1])  # Token type of previously added
        prev_v = self.__infix[-1].v  # Value of previously added

        # Terminal condition for expression is as follows.
        #   1. It can terminate with any of Num/Var/Str/Bool token.
        #   2. If can terminate with Trans/Rpar/SqrRpar/CrlRpar token.
        # All other cases are illegal.
        # The following logic is an implementation of these rules.
        # Note that TER token is not added to the infix array.
        if curr_t == Token.Ter:
            if prev_t == Token.Fun:
                raise ParserError.InvalidExpr(4, self.__line, self.__infix[-1].pos)
            elif prev_t == Token.Op:
                if prev_v not in [Unary.Trans, Delimiter.Rpar, Delimiter.SqrRpar, Delimiter.CrlRpar]:
                    raise ParserError.InvalidExpr(5, self.__line, self.__infix[-1].pos)

            return

        if curr_t == Token.Op:
            # Adjacent rule for OP token is as follows.
            #   1. It can adjacent with any of Num/Var/Str/Bool.
            #      But if current OP token is Neg/Lpar/CrlLpar, it needs implicit multiplication b/w them.
            #   2. If previous one is Fun token and current one is SqrLpar, they can adjacent.
            #   3. If previous one is OP token,
            #       3.1. If current one is Add/Sub, it can adjacent with any OP token.
            #            But if previous one is not Trans/Rpar/SqrRpar/CrlRpar, +/- here means Plus/Minus, resp.
            #       3.2. If current one is Neg/Lpar/CrlLpar, it can adjacent with any OP token.
            #            But if previous one is Trans/Rpar/SqrRpar/CrlRpar, it needs implicit multiplication b/w them.
            #       3.3. If current one is SqrRpar/Com and previous one is Trans/Rpar/SqrLpar/SqrRpar/CrlRpar/Com, they
            #            can adjacent.
            #            But if previous one is SqrLpar/Com, it needs Void token b/w them.
            #       3.4. If current one is CrlRpar and previous one is Trans/Rpar/SqrRpar/CrlLpar/CrlRpar, they can
            #            adjacnet.
            #            But if previous one is CrlLpar, it needs Void token b/w them.
            #       3.5. If current one is not Add/Sub/Neg/Lpar/SqrLpar/SqrRpar/CrlLpar/CrlRpar/Com and previous one is
            #            Trans/Rpar/SqrRpar/CrlRpar, they can adjacent.
            # All other cases are illegal.
            # The following logic is an implementation of these rules.
            if prev_t == Token.Op:
                if curr_v == Binary.Add:
                    if prev_v not in [Unary.Trans, Delimiter.Rpar, Delimiter.SqrRpar, Delimiter.CrlRpar]:
                        tok.v = Unary.Plus

                    self.__infix.append(tok)

                    return
                elif curr_v == Binary.Sub:
                    if prev_v not in [Unary.Trans, Delimiter.Rpar, Delimiter.SqrRpar, Delimiter.CrlRpar]:
                        tok.v = Unary.Minus

                    self.__infix.append(tok)

                    return
                elif curr_v in [Bool.Neg, Delimiter.Lpar, Delimiter.CrlLpar]:
                    if prev_v in [Unary.Trans, Delimiter.Rpar, Delimiter.SqrRpar, Delimiter.CrlRpar]:
                        self.__infix.append(Token.Op(Binary.Mul))

                    self.__infix.append(tok)

                    return
                elif curr_v in [Delimiter.SqrRpar, Delimiter.Com]:
                    if prev_v in [Delimiter.SqrLpar, Delimiter.Com]:
                        self.__infix.append(Token.Void())
                        self.__infix.append(tok)

                        return
                    elif prev_v in [Unary.Trans, Delimiter.Rpar, Delimiter.SqrRpar, Delimiter.CrlRpar]:
                        self.__infix.append(tok)

                        return
                    else:
                        raise ParserError.InvalidExpr(11, self.__line, tok.pos, (prev_v, curr_v))
                elif curr_v == Delimiter.CrlRpar:
                    if prev_v == Delimiter.CrlLpar:
                        self.__infix.append(Token.Void())
                        self.__infix.append(tok)

                        return
                    elif prev_v in [Unary.Trans, Delimiter.Rpar, Delimiter.SqrRpar, Delimiter.CrlRpar]:
                        self.__infix.append(tok)

                        return
                    else:
                        raise ParserError.InvalidExpr(11, self.__line, tok.pos, (prev_v, curr_v))
                else:
                    if prev_v in [Unary.Trans, Delimiter.Rpar, Delimiter.SqrRpar, Delimiter.CrlRpar]:
                        self.__infix.append(tok)

                        return

                    raise ParserError.InvalidExpr(11, self.__line, tok.pos, (prev_v, curr_v))
            elif prev_t == Token.Fun:
                if curr_v == Delimiter.SqrLpar:
                    self.__infix.append(tok)

                    return

                raise ParserError.InvalidExpr(9, self.__line, tok.pos)
            else:
                if curr_v in [Bool.Neg, Delimiter.Lpar, Delimiter.CrlLpar]:
                    self.__infix.append(Token.Op(Binary.Mul))

                self.__infix.append(tok)

                return
        else:
            # Adjacent rule for Num/Var/Fun/Str/Bool token is as follows.
            #   1. It can adjacent with any of Num/Var/Str/Bool token but it needs implicit multiplication b/w
            #      them.
            #   2. It can adjacent with any of OP token, but if previous OP token is Trans/Rpar/SqrRpar/CrlRpar, it
            #      needs implicit multiplication b/w them.
            # All other cases are illegal.
            # The following logic is an implementation of these rules.
            if prev_t == Token.Op:
                if prev_v in [Unary.Trans, Delimiter.Rpar, Delimiter.SqrRpar, Delimiter.CrlRpar]:
                    self.__infix.append(Token.Op(Binary.Mul))

                self.__infix.append(tok)

                return
            elif prev_t == Token.Fun:
                raise ParserError.InvalidExpr(9, self.__line, tok.pos)
            else:
                self.__infix.append(Token.Op(Binary.Mul))
                self.__infix.append(tok)

                return

    def __infix_to_postfix(self) -> None:
        """
        Convert infix-ordered tokens to postfix-order.

        For conversion, it uses two-stack approach described in the reference below.
        With deliberately assigned inner and outer precedence of operators and functions, this conversion takes account
        for precedence and association rule b/w them.
        Thus after conversion, there is no parentheses and delimiters.

        This method is private and called internally as the third step of parsing chain.
        For detailed description for parsing chain, refer to the comments of ``Parser.parse``.

        **Reference**
            * https://www.geeksforgeeks.org/infix-to-postfix-using-different-precedence-values-for-in-stack-and-out-stack

        :raise INVALID_EXPR: If the input string is invalid expression.
        """
        assert self.__infix

        self.__tmp_stk.clear()

        for tok in self.__infix:
            tok_t: type = type(tok)

            if tok_t == Token.Op:
                # If Rpar token is encountered, this means that parenthesis is closed.
                # Thus it pops tokens from temporary stack and add them to postfix list until matching Lpar token
                # appears.
                # However, if matching parenthesis does not appear or SqrLpar/CrlLpar/Com token comes first, then
                # this implies that there is some parenthesis matching problem.
                if tok.v == Delimiter.Rpar:
                    while self.__tmp_stk:
                        if self.__tmp_stk[-1].v in [Delimiter.Lpar, Delimiter.SqrLpar, Delimiter.CrlLpar,
                                                    Delimiter.Com]:
                            break

                        self.__postfix.append(self.__tmp_stk.pop())

                    if not (self.__tmp_stk and self.__tmp_stk[-1].v == Delimiter.Lpar):
                        raise ParserError.InvalidExpr(20, self.__line, tok.pos)

                    self.__tmp_stk.pop()

                    continue
                elif tok.v == Delimiter.SqrRpar:
                    # If SqrRpar token is encountered, it pops tokens in temporary stack and add them to postfix list as
                    # it did for Rpar token.
                    # Again, if matching parenthesis does not appear or Lpar/CrlLpar comes first, then this implies that
                    # there is some parenthesis matching problem.
                    # However, there are two slight differences this time.
                    # First, by counting the # of Com tokens encountered during popping, it determines the # of
                    # parameters for function or indexing operation.
                    # But since 0 parameter and 1 parameter cannot be differentiated by the # of Com tokens, it checks
                    # whether the top of postfix list is Void token or not before popping.
                    # The existence of Void token with no encounter of Com token implies 0 parameter.
                    # Second, it determines whether SqrLpar and SqrRpar tokens are used to function call or indexing
                    # operation by inspecting the top token in temporary stack after popping.
                    # It is function call iff there exists Fun token.
                    void_flag: bool = (type(self.__postfix[-1]) == Token.Void)  # Void function flag.
                    void_pos: int = len(self.__postfix) - 1  # Idx of void token.
                    argc: int = 1  # # of arguments.

                    while self.__tmp_stk:
                        if self.__tmp_stk[-1].v in [Delimiter.Lpar, Delimiter.SqrLpar, Delimiter.CrlLpar]:
                            break
                        elif self.__tmp_stk[-1].v == Delimiter.Com:
                            argc += 1
                            self.__tmp_stk.pop()
                        else:
                            self.__postfix.append(self.__tmp_stk.pop())

                    if not (self.__tmp_stk and self.__tmp_stk[-1].v == Delimiter.SqrLpar):
                        raise ParserError.InvalidExpr(20, self.__line, tok.pos)

                    match: Token.Tok = self.__tmp_stk.pop()  # Matched parenthesis.

                    argc = 0 if void_flag and argc == 1 else argc

                    if self.__tmp_stk and type(self.__tmp_stk[-1]) == Token.Fun:
                        self.__tmp_stk[-1].argc = argc
                        self.__postfix.append(self.__tmp_stk.pop())
                    else:
                        self.__postfix.append(Token.Op(Delimiter.Idx, match.pos))
                        self.__postfix[-1].argc = argc + 1

                    if argc == 0:
                        del self.__postfix[void_pos]

                    continue
                elif tok.v == Delimiter.CrlRpar:
                    # If CrlRpar token is encountered, it pops tokens in temporary stack and add them to postfix list as
                    # it did for SqrRpar token.
                    # Again, if matching parenthesis does not appear or Lpar/SqrLpar token comes first, then this
                    # implies that there is some parenthesis matching problem.
                    # One slight difference this time is that, List token will be added to postfix list after popping.
                    void_flag: bool = (type(self.__postfix[-1]) == Token.Void)  # Empty list flag.
                    void_pos: int = len(self.__postfix) - 1  # Idx of void token.
                    sz: int = 1  # Size of list.

                    while self.__tmp_stk:
                        if self.__tmp_stk[-1].v in [Delimiter.Lpar, Delimiter.SqrLpar, Delimiter.CrlLpar]:
                            break
                        elif self.__tmp_stk[-1].v == Delimiter.Com:
                            sz += 1
                            self.__tmp_stk.pop()
                        else:
                            self.__postfix.append(self.__tmp_stk.pop())

                    if not (self.__tmp_stk and self.__tmp_stk[-1].v == Delimiter.CrlLpar):
                        raise ParserError.InvalidExpr(20, self.__line, tok.pos)

                    sz = 0 if void_flag and sz == 1 else sz
                    self.__postfix.append(Token.List(self.__tmp_stk[-1].pos, sz))
                    self.__tmp_stk.pop()

                    if sz == 0:
                        del self.__postfix[void_pos]

                    continue
                elif tok.v == Delimiter.Com:
                    # If Com token is encountered, it pops tokens in temporary stack and add them to postfix list until
                    # SqrLpar/CrlLpar/Com token appears.
                    # If SqrLpar/CrlLpar/Com token does not appear or Lpar token comes first, then this implies that
                    # there is problem in the usage of Com token.
                    # One slight difference this time is that, we leave Com token in the temporary stack.
                    # They will be popped by SqrRpar/CrlRpar token later.
                    while self.__tmp_stk:
                        if self.__tmp_stk[-1].v in [Delimiter.Lpar, Delimiter.SqrLpar, Delimiter.CrlLpar,
                                                    Delimiter.Com]:
                            break

                        self.__postfix.append(self.__tmp_stk.pop())

                    if not self.__tmp_stk or self.__tmp_stk[-1].v == Delimiter.Lpar:
                        raise ParserError.InvalidExpr(21, self.__line, tok.pos)

                    self.__tmp_stk.append(tok)

                    continue
                elif tok.v == Unary.Trans:
                    self.__postfix.append(tok)

                    continue
                else:
                    # OP token which it not Rpar/SqrRpar/CrlRpar/Com goes to temporary stack.
                    # Before push, it compares the precedence b/w the top token in the temporary stack and the token to
                    # be pushed. (If temporary stack is empty, it just pushes.)
                    # If the top token has higher inner precedence than outer precedence of token to be pushed, pop the
                    # temporary stack and add them to postfix list until the relation inverts.
                    # Since the precedence is deliberately designed, this simple procedure automatically reorder
                    # operations according to the precedence and association rule b/w operations.
                    if not self.__tmp_stk:
                        self.__tmp_stk.append(tok)

                        continue

                    if self.__tmp_stk[-1].precd_in > tok.precd_out:
                        while self.__tmp_stk and self.__tmp_stk[-1].precd_in > tok.precd_out:
                            self.__postfix.append(self.__tmp_stk.pop())

                    self.__tmp_stk.append(tok)

                    continue
            elif tok_t == Token.Fun:
                # Fun token goes directly to temporary stack.
                self.__tmp_stk.append(tok)

                continue
            else:
                # Num/Var/Str/Bool/Void tokens goes directly to the postfix list.
                self.__postfix.append(tok)

                continue

        # After all tokens being processed, pop all remaining tokens in temporary stack and add them to postfix list.
        # Note that there must be no Lpar/SqrLpar/CrlLpar token.
        # The existence of these tokens implies parenthesis matching problem.
        while self.__tmp_stk:
            if self.__tmp_stk[-1].v in [Delimiter.Lpar, Delimiter.SqrLpar, Delimiter.CrlLpar]:
                raise ParserError.InvalidExpr(20, self.__line, self.__tmp_stk[-1].pos)

            self.__postfix.append(self.__tmp_stk.pop())

    def __ast_gen(self) -> AST.AST:
        """
        Generate AST from postfix expression.

        For generation, it uses stack approach described in the references below.

        This method is private and called internally as the third step of parsing chain.
        For detailed description for parsing chain, refer to the comments of ``Parser.parse``.

        **Reference**
            * https://en.wikipedia.org/wiki/Binary_expression_tree
            * https://www.geeksforgeeks.org/expression-tree

        :return: Generated AST.
        :rtype: AST.AST
        """
        assert self.__postfix

        self.__tmp_stk.clear()

        for tok in self.__postfix:
            tok_t: type = type(tok)

            if tok_t == Token.Op:
                # OP token pops ASTs in temporary stack and merge them into one AST rooted to itself.
                # The # of ASTs to be popped depends on the type of operator.
                # Note that the order of ASTs must be reversed.
                # That is, the top AST in the temporary stack should be registered as the last children and so on.
                for i in range(tok.argc, 0, -1):
                    tok.add_chd(self.__tmp_stk[-i])

                self.__tmp_stk = self.__tmp_stk[:-tok.argc]
                self.__tmp_stk.append(tok)

                continue
            elif tok_t in [Token.Fun, Token.List]:
                # Fun/List token is dealt similarly as OP token.
                if tok.argc == 0:
                    self.__tmp_stk.append(tok)

                    continue
                else:
                    for i in range(tok.argc, 0, -1):
                        tok.add_chd(self.__tmp_stk[-i])

                    self.__tmp_stk = self.__tmp_stk[:-tok.argc]
                    self.__tmp_stk.append(tok)

                    continue
            else:
                # Num/Var/Str/Bool/Void token goes directly to temporary as single (intermediate) AST.
                # They will be merged latter to form one final AST with will be returned.
                self.__tmp_stk.append(tok)

                continue

        # After iteration, there must be one final AST.
        assert len(self.__tmp_stk) == 1

        return AST.AST(self.__tmp_stk.pop(), self.__line)

    @classmethod
    def inst(cls) -> Parser:
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Parser
        """
        if not cls.__inst:
            cls.__inst = Parser()

        return cls.__inst

    def parse(self, line: str, debug: bool = False) -> AST.AST:
        """
        Parse user input line and generate AST.

        Parsing consists of four steps.
            1. Initialize parser.
               At this step, it clears internal buffers.
            2. Run lexer.
               Lexer tokenizes input string and do lexical analysis to detect syntax errors.
            3. Convert infix to postfix expression.
               For generation of AST, it converts infix expression to postfix expression.
               Further, it checks whether parenthesis is balanced.
               If the input passes lexer and this converter with no error, one can ensure that there is no syntax error.
            4. Generate AST.
               Generate AST using postfix converted expression.

        This method supports brief summary outputs which can be used for debugging or generation of debug set.

        :param line: Original user input string to be parsed.
        :type line: str
        :param debug: Flag for debug mode. (Default: False)
        :type debug: bool

        :return: Generated AST.
        :rtype: AST.AST
        """
        if debug:
            from sys import getsizeof

            buf: Type.BufT = Type.BufT.DEBUG  # Debug buffer.

            self.__line = line

            # Print out parsing target.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('parsing target'), buf)
            Printer.Printer.inst().buf(f'@raw : {line}', buf, indent=2)
            Printer.Printer.inst().buf(f'@size: {len(line)} chars ({getsizeof(line)} bytes)', buf, indent=2)
            Printer.Printer.inst().buf_newline(buf)
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('parsing chain'), buf)

            # Initialize parser.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Initializing parser'), buf, False, 2)
            self.__init()
            Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
            Printer.Printer.inst().buf(f'@__infix  : {len(self.__infix)} (cleared)', buf, indent=4)
            Printer.Printer.inst().buf(f'@__postfix: {len(self.__postfix)} (cleared)', buf, indent=4)
            Printer.Printer.inst().buf_newline(buf)

            # Run lexer.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running lexer'), buf, False, 2)

            try:
                self.__lexer()
            except Error.ParserErr as parser_err:
                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)
                Printer.Printer.inst().buf_newline(buf)

                raise parser_err
            else:
                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)

            # Print out generated infix-ordered tokens.
            for i in range(len(self.__infix)):
                Printer.Printer.inst().buf(f'[{i}] {type(self.__infix[i]).__name__.upper()}', buf, indent=4)
                Printer.Printer.inst().buf(f'@val: {self.__infix[i].v_str()}', buf, indent=6)
                Printer.Printer.inst().buf(f'@pos: {self.__infix[i].pos}', buf, indent=6)
                Printer.Printer.inst().buf_newline(buf)

            # Convert infix expression to postfix expression.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running infix to postfix converter'), buf, False,
                                       2)

            try:
                self.__infix_to_postfix()
            except Error.ParserErr as parser_err:
                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)
                Printer.Printer.inst().buf_newline(buf)

                raise parser_err
            else:
                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)

            # Print out converted postfix-ordered tokens.
            for i in range(len(self.__postfix)):
                Printer.Printer.inst().buf(f'[{i}] {type(self.__postfix[i]).__name__.upper()}', buf, indent=4)
                Printer.Printer.inst().buf(f'@val: {self.__postfix[i].v_str()}', buf, indent=6)
                Printer.Printer.inst().buf(f'@pos: {self.__postfix[i].pos}', buf, indent=6)
                Printer.Printer.inst().buf_newline(buf)

            # Generate AST.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running AST generator'), buf, False, 2)
            expr: AST.AST = self.__ast_gen()  # Generated AST
            Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
            Printer.Printer.inst().buf(f'@AST: {expr}', buf, indent=4)
            Printer.Printer.inst().buf_newline(buf)

            return expr
        else:
            self.__line = line
            self.__init()
            self.__lexer()
            self.__infix_to_postfix()

            return self.__ast_gen()
