from typing import List, final, Union

from Core import Token, AST, Type, DB, Error
from Util import Printer
from Util.Macro import is_white, is_alpha, is_underscore, is_quote, is_delim, is_dot, is_digit, is_op


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
    __inst = None

    def __init__(self) -> None:
        self.__line: str = ''
        self.__infix: List[Token.Tok] = []
        self.__postfix: List[Token.Tok] = []
        self.__tmp_stk: List[Token.Tok] = []

    def __del__(self) -> None:
        pass

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
        When all tokens are generated, it checks the terminal condition of expression.
        For detailed description for syntax checking, refer to the comments below and those of ``Parser.__add_tok``.

        This method is private and called internally as the second step of parsing chain.
        For detailed description for parsing chain, refer to the comments of ``Parser.parse``.

        :raise INVALID_EXPR: If the input string is invalid expression.
        :raise INVALID_TOK: If unknown token is encountered.
        :raise EMPTY_EXPR: If the input expression is void.
        """
        pos: int = 0  # Current position at the string to be tokenized.

        while pos < len(self.__line):
            if is_white(self.__line[pos]):
                # Skip all white spaces
                while is_white(self.__line[pos]):
                    pos += 1

                    if pos == len(self.__line):
                        break
            elif is_digit(self.__line[pos]):
                # Parse numeric value with integer part.
                # Parsing numeric value comprises of three steps.
                #   1. Parse integer part.
                #   2. Check for decimal point and parse decimal part.
                #   3. Check whether decimal point is overused.
                # The following logic is an implementation of these steps.
                upper: int = 0  # Integer part of numeric value.
                start: int = pos  # Starting position.

                # Parse integer part.
                while is_digit(self.__line[pos]):
                    upper *= 10
                    upper += ord(self.__line[pos]) - ord('0')
                    pos += 1

                    if pos == len(self.__line):
                        break

                if pos == len(self.__line) or not is_dot(self.__line[pos]):
                    self.__add_tok(Token.NumTok(upper, start))

                    continue

                pos += 1
                exp: int = 1  # Exponent.
                lower: int = 0  # Decimal part of numeric value.

                # Parse decimal part.
                while pos < len(self.__line) and is_digit(self.__line[pos]):
                    exp *= 10
                    lower *= 10
                    lower += ord(self.__line[pos]) - ord('0')
                    pos += 1

                # Check for decimal point overuse.
                if pos < len(self.__line) and is_dot(self.__line[pos]):
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 17, self.__line, pos)

                self.__add_tok(Token.NumTok(upper + lower / exp, start))

                continue
            elif is_dot(self.__line[pos]):
                # Parse numeric value w/o integer part.
                # The same logic for parsing numeric value with integer part is used.
                start: int = pos  # Starting position.
                exp: int = 1  # Exponent.
                lower: int = 0  # Decimal part of numeric value.
                pos += 1

                # Parse decimal part.
                while pos < len(self.__line) and is_digit(self.__line[pos]):
                    exp *= 10
                    lower *= 10
                    lower += ord(self.__line[pos]) - ord('0')
                    pos += 1

                # Check for decimal point misuse.
                if pos < len(self.__line) and is_dot(self.__line[pos]):
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 17, self.__line, pos)
                elif start == pos - 1:
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 19, self.__line, start)

                self.__add_tok(Token.NumTok(lower / exp, start))

                continue
            elif is_alpha(self.__line[pos]):
                # Parse function/command/constant/variable.
                # Variable name has following rules.
                #   1. It comprises of alphabets, digits, and underscore.
                #   2. It must start with alphabet.
                #   3. It cannot end with digit.
                # With this in mind, parsing is easy.
                # Since it cannot determine whether it means function/command/constant/variable, it searches for DB
                # after parsing.
                # For efficiency, parsed string will be hashed.
                start: int = pos  # Starting position.
                pos += 1

                while (pos < len(self.__line) and (
                        is_alpha(self.__line[pos]) or is_digit(self.__line[pos]) or is_underscore(self.__line[pos]))):
                    pos += 1

                if is_underscore(self.__line[pos - 1]):
                    pos -= 1

                # Check whether parsed symbol is function.
                find: Union[float, Type.CmdT, Type.FunT] = DB.DB.inst().get_handle(self.__line[start:pos])

                if isinstance(find, Type.FunT):
                    self.__add_tok(Token.FunTok(find, start))
                elif isinstance(find, Type.ConstT):
                    self.__add_tok(Token.NumTok(find.value, start))
                elif isinstance(find, Type.CmdT):
                    self.__add_tok(Token.CmdTok(find, start))
                else:
                    str_hash: int = hash(self.__line[start:pos])  # Hashed value of parsed string.

                    self.__add_tok(Token.VarTok(str_hash, start))

                    if not AST.AST.find_var(str_hash):
                        AST.AST.add_var(str_hash, self.__line[start:pos])

                continue
            elif is_op(self.__line[pos]):
                # Parse operator.
                if self.__line[pos] == '+':
                    # Note that at this point, it cannot determine whether + means ADD or PLUS.
                    # Just try as ADD token and let Parser.__add_tok to determine this.
                    self.__add_tok(Token.OpTok(Type.OpT.ADD, pos))
                elif self.__line[pos] == '-':
                    # Note that at this point, it cannot determine whether - means SUB or MINUS.
                    # Just try as SUB token and let Parser.__add_tok to determine this.
                    self.__add_tok(Token.OpTok(Type.OpT.SUB, pos))
                elif self.__line[pos] == '*':
                    if pos + 1 < len(self.__line) and self.__line[pos + 1] == '*':
                        self.__add_tok(Token.OpTok(Type.OpT.POW, pos))
                        pos += 1
                    else:
                        self.__add_tok(Token.OpTok(Type.OpT.MUL, pos))
                elif self.__line[pos] == '/':
                    self.__add_tok(Token.OpTok(Type.OpT.DIV, pos))
                elif self.__line[pos] == '%':
                    self.__add_tok(Token.OpTok(Type.OpT.REM, pos))
                elif self.__line[pos] == '^':
                    self.__add_tok(Token.OpTok(Type.OpT.POW, pos))
                elif self.__line[pos] == '!':
                    self.__add_tok(Token.OpTok(Type.OpT.FACT, pos))
                elif self.__line[pos] == '(':
                    self.__add_tok(Token.OpTok(Type.OpT.LPAR, pos))
                else:
                    self.__add_tok(Token.OpTok(Type.OpT.RPAR, pos))

                pos += 1

                continue
            elif is_delim(self.__line[pos]):
                # Parse delimiter.
                if self.__line[pos] == '[':
                    self.__add_tok(Token.DelimTok(Type.DelimT.START, pos))
                elif self.__line[pos] == ']':
                    self.__add_tok(Token.DelimTok(Type.DelimT.END, pos))
                else:
                    self.__add_tok(Token.DelimTok(Type.DelimT.CONT, pos))

                pos += 1

                continue
            elif is_quote(self.__line[pos]):
                # Parse string.
                # Note that string must be enclosed by double quote.
                start: int = pos  # Starting position.

                while True:
                    pos += 1

                    if pos == len(self.__line) or is_quote(self.__line[pos]):
                        break

                if pos == len(self.__line):
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 1, self.__line, start)

                self.__add_tok(Token.StrTok(self.__line[start + 1:pos], start))
                pos += 1

                continue
            elif is_underscore(self.__line[pos]):
                # Underscore is wrongly used.
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 18, self.__line, pos)
            else:
                # Unknown token is encountered.
                raise Error.ParserErr(Type.ParserErrT.INVALID_TOK, 2, self.__line, pos)

        # Check whether expression is void.
        if not self.__infix:
            raise Error.ParserErr(Type.ParserErrT.EMPTY_EXPR, 3)

        # Check for terminal condition of expression.
        # An expression cannot terminate with FUN/CMD/OP(except for RPAR, FACT)/DLEIM(except for END).
        top_tok: Token = self.__infix[-1]  # Top token of infix list.

        if top_tok.tok_t in [Type.TokT.FUN, Type.TokT.CMD]:
            raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 4, self.__line, top_tok.pos)
        elif top_tok.tok_t == Type.TokT.OP:
            if top_tok.v not in [Type.OpT.RPAR, Type.OpT.FACT]:
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 5, self.__line, top_tok.pos)
        elif top_tok.tok_t == Type.TokT.DELIM:
            if top_tok.v != Type.DelimT.END:
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 6, self.__line, top_tok.pos)
        elif top_tok.tok_t == Type.TokT.STR:
            raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 10, self.__line, top_tok.pos)

    def __add_tok(self, tok: Token.Tok) -> None:
        """
        Add token to internal buffer.

        Before it adds token, it checks the syntax.
        If it detects syntax error, it raises exception.
        Further, based on the previously added token, it determines whether + and - are unary sign operation or binary
        addition/subtraction.
        And based on the previously added token again, it detects the need of implicit multiplication and adds * between
        them to make it explicit.

        This method is private and called internally as a helper of ``Parser.__lexer``.
        For detailed description for lexing, refer to the comments of ``Parser.__lexer``.

        :param tok: Token to be added.
        :type tok: Token.Tok

        :raise INVALID_EXPR: If the input string is invalid expression.
        """
        curr_t: Type.TokT = tok.tok_t  # Token type of token to be added.
        curr_v = tok.v  # Token value of token to be added.

        if not self.__infix:
            # An expression can start with any of NUM/VAR/FUN/CMD 
            # Additionally, it can start with PLUS/MINUS/LPAR token (thus + and - here means PLUS and MINUS, resp.)
            # All other cases are illegal.
            if curr_t in [Type.TokT.NUM, Type.TokT.VAR, Type.TokT.FUN, Type.TokT.CMD]:
                self.__infix.append(tok)

                return
            if curr_t == Type.TokT.OP:
                if curr_v == Type.OpT.ADD:
                    self.__infix.append(Token.OpTok(Type.OpT.PLUS, tok.pos))

                    return
                elif curr_v == Type.OpT.SUB:
                    self.__infix.append(Token.OpTok(Type.OpT.MINUS, tok.pos))

                    return
                elif curr_v == Type.OpT.LPAR:
                    self.__infix.append(tok)

                    return
                else:
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 7, self.__line, tok.pos)
            else:
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 8, self.__line, tok.pos)

        prev_t: Type.TokT = self.__infix[-1].tok_t  # Token type of previously added
        prev_v = self.__infix[-1].v  # Value of previously added

        if curr_t in [Type.TokT.NUM, Type.TokT.VAR, Type.TokT.FUN, Type.TokT.CMD]:
            if prev_t in [Type.TokT.NUM, Type.TokT.VAR]:
                # NUM/VAR token followed by NUM/VAR/FUN/CMD token is perfectly legal.
                # But there must be implicit multiplication b/w them.
                self.__infix.append(Token.OpTok(Type.OpT.MUL))
                self.__infix.append(tok)

                return
            elif prev_t == Type.TokT.OP:
                # OP token followed by NUM/VAR/FUN/CMD token is perfectly legal.
                # But if the OP token is RPAR/FACT, then there must be implicit multiplication b/w them.
                if prev_v in [Type.OpT.RPAR, Type.OpT.FACT]:
                    self.__infix.append(Token.OpTok(Type.OpT.MUL))

                self.__infix.append(tok)

                return
            elif prev_t == Type.TokT.DELIM:
                # DELIM token followed by NUM/VAR/FUN/CMD token is perfectly legal.
                # But if the DELIM token is END, then there must be implicit multiplication b/w them.
                if prev_v == Type.DelimT.END:
                    self.__infix.append(Token.OpTok(Type.OpT.MUL))

                self.__infix.append(tok)

                return
            elif prev_t in [Type.TokT.FUN, Type.TokT.CMD]:
                # FUN/CMD token must be followed by START 
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 9, self.__line, tok.pos)
            else:
                # STR token must be followed by CONT/END 
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 10, self.__line, tok.pos)
        elif curr_t == Type.TokT.OP:
            if prev_t in [Type.TokT.NUM, Type.TokT.VAR]:
                # NUM/VAR token followed by OP token is perfectly legal.
                # But if the OP token is LPAR, then there must be implicit multiplication b/w them.
                if curr_v == Type.OpT.LPAR:
                    self.__infix.append(Token.OpTok(Type.OpT.MUL))

                self.__infix.append(tok)

                return
            elif prev_t == Type.TokT.OP:
                # OP token followed by OP token is not legal in general.
                # Few exceptions are,
                #   1. RPAR/FACT token followed by any OP token
                #     (but if the following OP token is LPAR, then there must be implicit multiplication b/w them)
                #   2. Any OP token which is not RPAR/FACT token followed by PLUS/MINUS/LPAR token
                #      (thus + and - here means PLUS and MINUS, resp.)
                # The following logic is an implementation of this rule.
                if prev_v in [Type.OpT.RPAR, Type.OpT.FACT]:
                    if curr_v == Type.OpT.LPAR:
                        self.__infix.append(Token.OpTok(Type.OpT.MUL))

                    self.__infix.append(tok)

                    return
                elif curr_v == Type.OpT.ADD:
                    self.__infix.append(Token.OpTok(Type.OpT.PLUS, tok.pos))

                    return
                elif curr_v == Type.OpT.SUB:
                    self.__infix.append(Token.OpTok(Type.OpT.MINUS, tok.pos))

                    return
                elif curr_v == Type.OpT.LPAR:
                    self.__infix.append(tok)

                    return
                else:
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 11, self.__line, tok.pos)
            elif prev_t == Type.TokT.DELIM:
                # DELIM token followed by OP token is not legal in general.
                # Few exceptions are,
                #   1. START/CONT token followed by PLUS/MINUS/LPAR token
                #      (thus + and - here means PLUS and MINUS, resp.)
                #   2. END token followed by any OP token
                #      (but if the following OP token is LPAR, there must be implicit multiplication b/w them)
                # The following logic is an implementation of this rule.
                if prev_v == Type.DelimT.END:
                    if curr_v == Type.OpT.LPAR:
                        self.__infix.append(Token.OpTok(Type.OpT.MUL))

                    self.__infix.append(tok)

                    return
                elif curr_v == Type.OpT.ADD:
                    self.__infix.append(Token.OpTok(Type.OpT.PLUS, tok.pos))

                    return
                elif curr_v == Type.OpT.SUB:
                    self.__infix.append(Token.OpTok(Type.OpT.MINUS, tok.pos))

                    return
                elif curr_v == Type.OpT.LPAR:
                    self.__infix.append(tok)

                    return
                else:
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 12, self.__line, tok.pos)
            elif prev_t == Type.TokT.STR:
                # STR token followed by OP token is illegal.
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 10, self.__line, tok.pos)
            else:
                # FUN/CMD token followed by OP token illegal.
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 9, self.__line, tok.pos)
        elif curr_t == Type.TokT.DELIM:
            if prev_t in [Type.TokT.NUM, Type.TokT.VAR, Type.TokT.STR]:
                # NUM/VAR/STR token can be followed by DELIM token which is not START.
                if curr_v == Type.DelimT.START:
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 13, self.__line, tok.pos)

                self.__infix.append(tok)

                return
            elif prev_t == Type.TokT.OP:
                # OP token followed by DELIM token is illegal with only one exception.
                # The exceptional case is RPAR/FACT token followed by DLEIM token which is not START.
                if prev_v in [Type.OpT.RPAR, Type.OpT.FACT] and curr_v != Type.DelimT.START:
                    self.__infix.append(tok)

                    return

                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 14, self.__line, tok.pos)
            elif prev_t == Type.TokT.DELIM:
                # DLEIM token followed by DELIM token is illegal in general.
                # Few exceptions are
                #   1. START token followed by END token
                #      (this case means that no parameter is passed, so we need VOID token for placeholder)
                #   2. END token followed by CONT/END token
                # The following logic is an implementation of this rule.
                if prev_v == Type.DelimT.START and curr_v == Type.DelimT.END:
                    self.__infix += [Token.VoidTok(), tok]

                    return
                elif prev_v == Type.DelimT.END and curr_v != Type.DelimT.START:
                    self.__infix.append(tok)

                    return
                else:
                    raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 15, self.__line, tok.pos)
            else:
                # FUN/CMD token can be only followed by START 
                if curr_v == Type.DelimT.START:
                    self.__infix.append(tok)

                    return

                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 9, self.__line, tok.pos)
        else:
            # For STR token, there must be preceding START/CONT 
            # This with other rules described above forces for STR token to be used as parameter of function or command
            # only.
            if prev_v in [Type.DelimT.START, Type.DelimT.CONT]:
                self.__infix.append(tok)

                return

            raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 16, self.__line, tok.pos)

    def __infix_to_postfix(self) -> None:
        """
        Convert infix-ordered tokens to postfix-order.

        For conversion, it uses two-stack approach described in the reference below.
        With deliberately assigned inner and outer precedence of operators, delimiters, functions, and commands,
        this conversion takes account for precedence and association rule b/w them.
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
            if tok.tok_t in [Type.TokT.NUM, Type.TokT.VAR, Type.TokT.STR, Type.TokT.VOID]:
                # NUM/VAR/STR/VOID tokens goes directly to the postfix list.
                self.__postfix.append(tok)

                continue
            elif tok.tok_t == Type.TokT.OP:
                # Basically, OP token goes to temporary stack.
                # One exception is FACT token, which goes directly to the postfix list.
                if tok.v == Type.OpT.FACT:
                    self.__postfix.append(tok)

                    continue

                if tok.v == Type.OpT.RPAR:
                    # If RPAR token is encountered, this means that parenthesis is closed.
                    # Thus it pops tokens from temporary stack and add them to postfix list until matching LPAR token
                    # appears.
                    # When LPAR token appears, the popping stops.
                    # However, if matching parenthesis does not appear or delimiter START/CONT comes first, then this
                    # implies that there is some parenthesis matching problem.
                    while self.__tmp_stk:
                        top_tok: Token.Tok = self.__tmp_stk[-1]  # Top token in temporary stack

                        if top_tok.v != Type.DelimT.START and top_tok.v != Type.OpT.LPAR:
                            self.__postfix.append(self.__tmp_stk.pop())

                            continue

                        break

                    if not self.__tmp_stk or self.__tmp_stk[-1].tok_t != Type.TokT.OP:
                        raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 20, self.__line, tok.pos)

                    self.__tmp_stk.pop()

                    continue

                # OP token goes to temporary stack as mentioned, but before push, it compares the precedence b/w the top
                # token in the temporary stack and the token to be pushed.
                # If the top token has higher (inner) precedence than (outer) precedence of token to be pushed,
                # pop the temporary stack and add them to postfix list until the relation inverts.
                # Since the precedence is deliberately designed, this simple procedure automatically reorder operations
                # following the precedence and association rule b/w operations.
                if not self.__tmp_stk:
                    self.__tmp_stk.append(tok)

                    continue

                if self.__tmp_stk[-1].precd[0] > tok.precd[1]:
                    while self.__tmp_stk[-1].precd[0] > tok.precd[1]:
                        self.__postfix.append(self.__tmp_stk.pop())

                        if not self.__tmp_stk:
                            break

                self.__tmp_stk.append(tok)

                continue
            elif tok.tok_t in [Type.TokT.FUN, Type.TokT.CMD]:
                # FUN/CMD token goes directly to temporary stack.
                self.__tmp_stk.append(tok)

                continue
            else:
                # Basically, DELIM token goes to temporary stack.
                # But if CONT/END token is encountered, we pop tokens in temporary stack and add them to postfix list as
                # we did for RPAR 
                # Further, the same logic for parenthesis matching problem detection is used.
                # One slight difference is that unlike RPAR, CONT token goes in to the temporary stack after popping.
                # And END token will pop all remaining CONT tokens.
                # This is to count the # of parameters passed for specific function or command.
                # However, it cannot determine whether the function or function has 0 or 1 parameter with the # of CONT
                # tokens (they both have no CONT tokens at all) it inspects the top token in the postfix list.
                # If the function or command has no parameter passed, then the top token must be VOID 
                if tok.v == Type.DelimT.START:
                    self.__tmp_stk.append(tok)

                    continue
                elif tok.v == Type.DelimT.END:
                    if self.__postfix[-1].tok_t == Type.TokT.VOID:
                        self.__postfix.pop()
                        self.__tmp_stk.pop()
                        self.__postfix.append(self.__tmp_stk.pop())

                        continue

                    argc: int = 1  # # of arguments

                    while self.__tmp_stk:
                        top_tok: Token.Tok = self.__tmp_stk[-1]  # Top token in temporary stack

                        if top_tok.tok_t == Type.TokT.OP and top_tok.v != Type.OpT.LPAR:
                            self.__postfix.append(self.__tmp_stk.pop())

                            continue
                        elif top_tok.v == Type.DelimT.CONT:
                            argc += 1
                            self.__tmp_stk.pop()

                            continue

                        break

                    if not self.__tmp_stk or self.__tmp_stk[-1].tok_t == Type.TokT.OP:
                        raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 20, self.__line, tok.pos)

                    # After popping, register the # of parameters passed to the FUN/CMD
                    self.__tmp_stk.pop()
                    self.__tmp_stk[-1].argc = argc
                    self.__postfix.append(self.__tmp_stk.pop())

                    continue
                else:
                    while self.__tmp_stk:
                        top_tok: Token.Tok = self.__tmp_stk[-1]  # Top token in temporary stack

                        if top_tok.tok_t == Type.TokT.OP and top_tok.v != Type.OpT.LPAR:
                            self.__postfix.append(self.__tmp_stk.pop())

                            continue

                        break

                    if not self.__tmp_stk or self.__tmp_stk[-1].tok_t == Type.TokT.OP:
                        raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 21, self.__line, tok.pos)

                    self.__tmp_stk.append(tok)

                    continue

        # After all tokens being processed, pop all remaining tokens in temporary stack and add them to postfix list.
        # Note that there must be no LPAR/START 
        # The existence of these tokens implies parenthesis matching problem.
        while self.__tmp_stk:
            top_tok: Token.Tok = self.__tmp_stk[-1]  # Top token in temporary stack

            if top_tok.v == Type.OpT.LPAR or top_tok.v == Type.DelimT.START:
                raise Error.ParserErr(Type.ParserErrT.INVALID_EXPR, 20, self.__line, top_tok.pos)

            self.__postfix.append(self.__tmp_stk.pop())

    def __AST_gen(self) -> AST.AST:
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
            if tok.tok_t in [Type.TokT.NUM, Type.TokT.VAR, Type.TokT.STR]:
                # NUM/VAR/STR token goes directly to temporary as single (intermediate) AST.
                # They will be merged latter to form one final AST with will be returned.
                self.__tmp_stk.append(tok)

                continue
            elif tok.tok_t == Type.TokT.OP:
                # OP token pops ASTs in temporary stack and merge them into one AST rooted to itself.
                # The # of ASTs to be popped depends on the type of operator.
                # Note that the order of ASTs must be reversed.
                # That is, the top AST in the temporary stack should be registered as the last children and so on.
                if tok.v in [Type.OpT.PLUS, Type.OpT.MINUS, Type.OpT.FACT]:
                    tok.add_chd(self.__tmp_stk.pop())
                    self.__tmp_stk.append(tok)

                    continue
                else:
                    top_tok: Token.Tok = self.__tmp_stk.pop()  # Top token in temporary stack
                    tok.add_chd(self.__tmp_stk.pop())
                    tok.add_chd(top_tok)
                    self.__tmp_stk.append(tok)

                    continue
            else:
                # FUN/CMD token is dealt similarly as OP token.
                if tok.argc == 0:
                    self.__tmp_stk.append(tok)

                    continue
                else:
                    for i in range(tok.argc, 0, -1):
                        tok.add_chd(self.__tmp_stk[-i])

                    self.__tmp_stk = self.__tmp_stk[:-tok.argc]
                    self.__tmp_stk.append(tok)

                    continue

        # After iteration, there must be one final AST.
        assert len(self.__tmp_stk) == 1

        return AST.AST(self.__tmp_stk.pop(), self.__line)

    @classmethod
    def inst(cls):
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
                Printer.Printer.inst().buf(f'[{i}] {self.__infix[i].tok_t}', buf, indent=4)
                Printer.Printer.inst().buf(f'@val: {self.__infix[i].v}', buf, indent=6)
                Printer.Printer.inst().buf(f'@pos: {self.__infix[i].pos}', buf, indent=6)
                Printer.Printer.inst().buf_newline(buf)

            # Convert infix expression to postfix expression.
            Printer.Printer.inst().buf(
                Printer.Printer.inst().f_prog('Running infix to postfix converter'), buf, False, 2)

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
                Printer.Printer.inst().buf(f'[{i}] {self.__postfix[i].tok_t}', buf, indent=4)
                Printer.Printer.inst().buf(f'@val: {self.__postfix[i].v}', buf, indent=6)
                Printer.Printer.inst().buf(f'@pos: {self.__postfix[i].pos}', buf, indent=6)
                Printer.Printer.inst().buf_newline(buf)

            # Generate AST.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog('Running AST generator'), buf, False, 2)
            expr: AST.AST = self.__AST_gen()  # Generated AST
            Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
            Printer.Printer.inst().buf(f'@infix  : {expr.infix()}', buf, indent=4)
            Printer.Printer.inst().buf(f'@postfix: {expr.postfix()}', buf, indent=4)
            Printer.Printer.inst().buf(f'@prefix : {expr.prefix()}', buf, indent=4)
            Printer.Printer.inst().buf_newline(buf)

            return expr
        else:
            self.__line = line
            self.__init()
            self.__lexer()
            self.__infix_to_postfix()

            return self.__AST_gen()
