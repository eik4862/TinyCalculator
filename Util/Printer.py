import sys
from typing import final, TextIO, Final, List, Union

from Core import Type


# TODO: floating point printing mode
# TODO: Long int ... printing
@final
class Printer:
    """
    Buffer strings and print out them to target file.

    This class is implemented as singleton.
    For the concept of singleton pattern, consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Singleton_pattern

    :cvar __TITLE_LEN: Length of title.
    :cvar __PROG_LEN: Length of progress bar.
    :cvar __TITLE_FILL: Placeholder in title.
    :cvar __PROG_FILL: Placeholder in progress bar.
    :cvar __HLINE_FILL: Marker in horizontal line of table.
    :cvar __BLUE_TEMP: Blue bold style template.
    :cvar __RED_TEMP: Red bold style template.
    :cvar __inst: Singleton object.

    :ivar __stdout: Buffer for std output.
    :ivar __stderr: Buffer for std error.
    :ivar __stdwarn: Buffer for std warning.
    :ivar __internal: Buffer for internal output.
    :ivar __debug: Buffer for debugging.
    """
    __TITLE_LEN: Final[int] = 44
    __PROG_LEN: Final[int] = 37
    __TB_SEP: Final[int] = 2
    __TITLE_FILL: Final[str] = '-'
    __PROG_FILL: Final[str] = '.'
    __HLINE_FILL: Final[str] = '-'

    __BLUE_TEMP: Final[str] = '\033[1;36m$1\033[0m'
    __RED_TEMP: Final[str] = '\033[1;31m$1\033[0m'

    __inst = None

    def __init__(self) -> None:
        self.__stdout: str = ''
        self.__stderr: str = ''
        self.__stdwarn: str = ''
        self.__internal: str = ''
        self.__debug: str = ''

    def __del__(self) -> None:
        pass

    @classmethod
    def inst(cls):
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: Printer
        """
        if not cls.__inst:
            cls.__inst = Printer()

        return cls.__inst

    def buf(self, string: str, buf: Type.BufT = Type.BufT.STDOUT, newline: bool = True, indent: int = 0) -> None:
        """
        Buffer input string to target buffer.

        :param string: String to be buffered.
        :type string: str
        :param buf: Buffer where input content will be buffered. (Default: Type.PrinterBuf.STDOUT)
        :type buf: Type.BufT
        :param newline: Flag for newline character at the end of string to be buffered. (Default: True)
        :type newline: bool
        :param indent: The # of leading indentation (white space). (Default: 0)
        :type indent: int
        """
        if buf == Type.BufT.STDOUT:
            self.__stdout += ' ' * indent + string + '\n' if newline else ' ' * indent + string
        elif buf == Type.BufT.STDERR:
            self.__stderr += ' ' * indent + string + '\n' if newline else ' ' * indent + string
        elif buf == Type.BufT.INTERNAL:
            self.__internal += ' ' * indent + string + '\n' if newline else ' ' * indent + string
        elif buf == Type.BufT.DEBUG:
            self.__debug += ' ' * indent + string + '\n' if newline else ' ' * indent + string
        else:
            self.__stdwarn += ' ' * indent + string + '\n' if newline else ' ' * indent + string

    def buf_newline(self, buf: Type.BufT = Type.BufT.STDOUT) -> None:
        """
        Buffer newline character to target buffer.

        :param buf: Buffer where newline character will be buffered. (Default: Type.PrinterBuf.STDOUT)
        :type buf: Type.BufT
        """
        self.buf('', buf, True)

    def pop(self, buf: Type.BufT = Type.BufT.STDOUT) -> None:
        """
        Pop the last character from target buffer.

        :param buf: Buffer to be popped. (Default: Type.PrinterBuf.STDOUT)
        :type buf: Type.BufT
        """
        if buf == Type.BufT.STDOUT:
            self.__stdout = self.__stdout[:-1]
        elif buf == Type.BufT.STDERR:
            self.__stderr = self.__stderr[:-1]
        elif buf == Type.BufT.INTERNAL:
            self.__internal = self.__internal[:-1]
        elif buf == Type.BufT.STDWARN:
            self.__stdwarn = self.__stdwarn[:-1]
        else:
            self.__debug = self.__debug[:-1]

    def print(self, buf: Type.BufT = Type.BufT.STDOUT, to: TextIO = sys.stdout) -> None:
        """
        Print buffered string in target buffer to target file.
        After printing, the buffer will be cleared.

        :param buf: Buffer whose content is to be printed out. (Default: Type.PrinterBuf.STDOUT)
        :type buf: Type.BufT
        :param to: File where content will be written. (Default: sys.stdout)
        :type to: TextIO
        """
        if buf == Type.BufT.STDOUT:
            print(self.__stdout, end='', file=to)
            self.__stdout = ''
        elif buf == Type.BufT.STDERR:
            print(self.__stderr, end='', file=to)
            self.__stderr = ''
        elif buf == Type.BufT.INTERNAL:
            print(self.__internal, end='', file=to)
            self.__internal = ''
        elif buf == Type.BufT.STDWARN:
            print(self.__stdwarn, end='', file=to)
            self.__stdwarn = ''
        else:
            print(self.__debug, end='', file=to)
            self.__debug = ''

    def sprint(self, buf: Type.BufT = Type.BufT.STDOUT) -> str:
        """
        Print buffered string in target buffer as a string.
        After printing, the buffer will be cleared.

        :param buf: Buffer whose content is to be printed out. (Default: Type.PrinterBuf.STDOUT)
        :type buf: Type.BufT
        """
        if buf == Type.BufT.STDOUT:
            content: str = self.__stdout
            self.__stdout = ''

            return content
        elif buf == Type.BufT.STDERR:
            content: str = self.__stderr
            self.__stderr = ''

            return content
        elif buf == Type.BufT.INTERNAL:
            content: str = self.__internal
            self.__internal = ''

            return content
        elif buf == Type.BufT.STDWARN:
            content: str = self.__stdwarn
            self.__stdwarn = ''

            return content
        else:
            content: str = self.__debug
            self.__debug = ''

            return content

    def clr(self, buf: Type.BufT = Type.BufT.STDOUT) -> None:
        """
        Clear target buffer without printing out.

        :param buf: Buffer to be cleared.
        :type buf: Type.BufT
        """
        if buf == Type.BufT.STDOUT:
            self.__stdout = ''
        elif buf == Type.BufT.STDERR:
            self.__stderr = ''
        elif buf == Type.BufT.INTERNAL:
            self.__internal = ''
        elif buf == Type.BufT.STDWARN:
            self.__stdwarn = ''
        else:
            self.__debug = ''

    def f_title(self, string: str, length: int = None) -> str:
        """
        Format string as a title of specific length.

        Title is aligned to center using title placeholder character ``Printer.__TITLE_FILL``.
        The length of title is optional and will be default length ``Printer.__TITLE_LEN`` if not given.

        :param string: String to be formatted.
        :type string: str
        :param length: Length of title. (Default: None)
        :type length: int

        :return: Formatted string.
        :rtype: str
        """
        length = self.__TITLE_LEN if not length else length

        if len(string) >= length:
            return string.upper()

        head_cnt: int = round((length - len(string) - 2) / 2)
        tail_cnt: int = length - len(string) - head_cnt - 2

        return f'{self.__TITLE_FILL * head_cnt} {string.upper()} {self.__TITLE_FILL * tail_cnt}'

    def f_prog(self, string: str, length: int = None) -> str:
        """
        Format string as a line of progress line.

        Status line is aligned to left using progress line placeholder ``Printer.__PROG_FILL``.
        The length of progress line is optional and will be default length ``Printer.__PROG_LEN`` if not given.

        :param string: String to be formatted.
        :type string: str
        :param length: (Default: None)
        :type length: int

        :return: Formatted string.
        :rtype: str
        """
        length = self.__PROG_LEN if not length else length

        if len(string) >= length:
            return string

        trailing_cnt = length - len(string)

        return f'{string}{self.__PROG_FILL * trailing_cnt} '

    def f_col(self, string: str, col: Type.Col) -> str:
        """
        Colorize string.
        In addition, it gives the string bold style.

        :param string: String to be colorized.
        :type string: str
        :param col: Type of color for colorizing.
        :type col: Type.Col

        :return: Colorized string.
        :rtype: str
        """
        if col == Type.Col.RED:
            return self.__RED_TEMP.replace('$1', string)
        else:
            return self.__BLUE_TEMP.replace('$1', string)

    def f_ord(self, n: int) -> str:
        """
        Generate ordinal expression of natural number.

        :param n: Natural number whose ordinal expression is to be generated.
        :type n: int

        :return: Ordinal expression.
        :rtype: str
        """
        if 11 <= n <= 13:
            return f'{n}th'
        elif n % 10 == 1:
            return f'{n}st'
        elif n % 10 == 2:
            return f'{n}nd'
        elif n % 10 == 3:
            return f'{n}rd'
        else:
            return f'{n}th'

    def f_tb(self, string: List[str], col_width: Union[List[int], int], sep: int = None) -> str:
        if not sep:
            sep = self.__TB_SEP

        if isinstance(col_width, int):
            col_width = [col_width] * len(string)

        buf: str = ''

        for i in range(len(string)):
            if col_width[i] > len(string[i]):
                head_cnt: int = round((col_width[i] - len(string[i])) / 2)
                tail_cnt: int = col_width[i] - len(string[i]) - head_cnt
                buf += ' ' * (head_cnt + sep) + string[i].upper() + ' ' * tail_cnt
            else:
                buf += ' ' * sep + string[i].upper()

        return buf[sep:]

    def f_hline(self, col_width: Union[List[int], int], col_num: int = None, sep: int = None) -> str:
        if not sep:
            sep = self.__TB_SEP

        if isinstance(col_width, int):
            col_width = [col_width] * col_num

        buf: str = ''

        for width in col_width:
            buf += ' ' * sep + self.__HLINE_FILL * width

        return buf[sep:]
