from sys import float_info

"""
Simple macros.
"""


def is_white(c: str) -> bool:
    """
    Check whether input character is whitespace or not.
    Here, whitespace includes space, tab, and newline characters.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is whitespace. False otherwise.
    :rtype: bool
    """
    return c in [' ', '\t', '\n']


def is_digit(c: str) -> bool:
    """
    Check whether input character is digit or not.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is digit. False otherwise.
    :rtype: bool
    """
    return '0' <= c <= '9'


def is_dot(c: str) -> bool:
    """
    Check whether input character is decimal point or not.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is decimal point. False otherwise.
    :rtype: bool
    """
    return c == '.'


def is_alpha(c: str) -> bool:
    """
    Check whether input character is alphabet or not.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is alphabet. False otherwise.
    :rtype: bool
    """
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'


def is_underscore(c: str) -> bool:
    """
    Check whether input character is underscore or not.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is underscore. False otherwise.
    :rtype: bool
    """
    return c == '_'


def is_op(c: str) -> bool:
    """
    Check whether input character is operator or not.
    Here, whitespace includes +, -, /, %, ^, *, !, (, and ).

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is operator. False otherwise.
    :rtype: bool
    """
    return c in ['+', '-', '/', '%', '^', '*', '!', '(', ')']


def is_delim(c: str) -> bool:
    """
    Check whether input character is delimiter or not.
    Here, whitespace includes [, ], and ,.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is delimiter. False otherwise.
    :rtype: bool
    """
    return c in ['[', ']', ',']


def is_quote(c: str) -> bool:
    """
    Check whether input character is (double) quote or not.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is quote. False otherwise.
    :rtype: bool
    """
    return c == '"'


def is_comment(c: str) -> bool:
    """
    Check whether input character is comment delimiter # or not.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is comment delimiter. False otherwise.
    :rtype: bool
    """
    return c == '#'


def is_newline(c: str) -> bool:
    """
    Check whether input character is newline character or not.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is newline character. False otherwise.
    :rtype: bool
    """
    return c == '\n'


def is_tag(c: str) -> bool:
    """
    Check whether input character is tag delimiter $ or not.
    Here, whitespace includes space, tab, and newline characters.

    :param c: Character to be checked.
    :type c: str

    :return: True if the input character is tag delimiter. False otherwise.
    :rtype: bool
    """
    return c == '$'


def is_bigint(n: int) -> bool:
    """
    Check whether input integer is so-called big integer which is too big to be casted to float.

    :param n: Integer to be checked.
    :type n: int

    :return: True if it is big integer which is too big. False otherwise.
    :rtype: bool
    """
    return isinstance(n, int) and n > float_info.max


def is_smallint(n: int) -> bool:
    """
    Check whether input integer is so-called big integer which is too small to be casted to float.

    :param n: Integer to be checked.
    :type n: int

    :return: True if it is big integer which is too small. False otherwise.
    :rtype: bool
    """
    return isinstance(n, int) and n < -float_info.max


def is_int(x: float) -> bool:
    return x % 1 == 0
