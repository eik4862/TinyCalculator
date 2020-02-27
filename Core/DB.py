from decimal import Decimal
from typing import Dict, List, TextIO, final, Final, Union, Tuple

from Core import Type, Error
from Util import Printer
from Util.Macro import is_comment, is_newline, is_tag


@final
class DB:
    """
    Load database from source file and manage them.
    
    This class is implemented as singleton.
    For the concept of singleton pattern, consult the references below.

    **Reference**
        * https://en.wikipedia.org/wiki/Singleton_pattern

    :cvar __HANDLE_SRC: Handles to be registered.
    :cvar __FILE_SRC: DB source files to be loaded.
    :cvar __TEST_SRC: DB source files for test to be loaded.
    :cvar __inst: Singleton object.

    :ivar __handle_tb: Hash table for function/command/constant handles.
    :ivar __storage: Storage for DB.
    """
    __HANDLE_SRC: Final[List[Type.HandleSrc]] = [
        Type.HandleSrc(Type.FunT, 'function handles'),
        Type.HandleSrc(Type.CmdT, 'command handles'),
        Type.HandleSrc(Type.ConstT, 'constant handles')
    ]
    __FILE_SRC: Final[Dict[str, Type.FileSrc]] = {
        'err_msg': Type.FileSrc('../Data/ErrorMassage.data', 'error messages', False),
        'warn_msg': Type.FileSrc('../Data/WarningMessage.data', 'warning messages', False),
        'greet_msg': Type.FileSrc('../Data/GreetingMessage.data', 'greeting messages', True),
        'debug_in': Type.FileSrc('../Data/Debug.in', 'debug input', False),
        'debug_out': Type.FileSrc('../Data/Debug.out', 'debug output', True)
    }
    __TEST_IDX_OFFSET: Final[int] = len(__FILE_SRC)
    __TEST_SRC: Final[Dict[str, Type.FileSrc]] = {
        'custom_in': Type.FileSrc('../Test/In/Test.in', 'Custom test input', False),
        'sin_small_in': Type.FileSrc('../Test/In/Test_Sin_Small.in', 'Sin test input', False),
        'sin_medium_in': Type.FileSrc('../Test/In/Test_Sin_Medium.in', 'Sin test input', False),
        'sin_large_in': Type.FileSrc('../Test/In/Test_Sin_Large.in', 'Sin test input', False),
        'cos_small_in': Type.FileSrc('../Test/In/Test_Cos_Small.in', 'Cos test input', False),
        'cos_medium_in': Type.FileSrc('../Test/In/Test_Cos_Medium.in', 'Cos test input', False),
        'cos_large_in': Type.FileSrc('../Test/In/Test_Cos_Large.in', 'Cos test input', False),
        'tan_small_in': Type.FileSrc('../Test/In/Test_Tan_Small.in', 'Tan test input', False),
        'tan_medium_in': Type.FileSrc('../Test/In/Test_Tan_Medium.in', 'Tan test input', False),
        'tan_large_in': Type.FileSrc('../Test/In/Test_Tan_Large.in', 'Tan test input', False),
        'csc_small_in': Type.FileSrc('../Test/In/Test_Csc_Small.in', 'Csc test input', False),
        'csc_medium_in': Type.FileSrc('../Test/In/Test_Csc_Medium.in', 'Csc test input', False),
        'csc_large_in': Type.FileSrc('../Test/In/Test_Csc_Large.in', 'Csc test input', False),
        'sec_small_in': Type.FileSrc('../Test/In/Test_Sec_Small.in', 'Sec test input', False),
        'sec_medium_in': Type.FileSrc('../Test/In/Test_Sec_Medium.in', 'Sec test input', False),
        'sec_large_in': Type.FileSrc('../Test/In/Test_Sec_Large.in', 'Sec test input', False),
        'cot_small_in': Type.FileSrc('../Test/In/Test_Cot_Small.in', 'Cot test input', False),
        'cot_medium_in': Type.FileSrc('../Test/In/Test_Cot_Medium.in', 'Cot test input', False),
        'cot_large_in': Type.FileSrc('../Test/In/Test_Cot_Large.in', 'Cot test input', False),
        'asin_small_in': Type.FileSrc('../Test/In/Test_Asin_Small.in', 'Asin test input', False),
        'acos_small_in': Type.FileSrc('../Test/In/Test_Acos_Small.in', 'Acos test input', False),
        'atan_small_in': Type.FileSrc('../Test/In/Test_Atan_Small.in', 'Atan test input', False),
        'atan_medium_in': Type.FileSrc('../Test/In/Test_Atan_Medium.in', 'Atan test input', False),
        'atan_large_in': Type.FileSrc('../Test/In/Test_Atan_Large.in', 'Atan test input', False),
        'acsc_small_in': Type.FileSrc('../Test/In/Test_Acsc_Small.in', 'Acsc test input', False),
        'acsc_medium_in': Type.FileSrc('../Test/In/Test_Acsc_Medium.in', 'Acsc test input', False),
        'acsc_large_in': Type.FileSrc('../Test/In/Test_Acsc_Large.in', 'Acsc test input', False),
        'asec_small_in': Type.FileSrc('../Test/In/Test_Asec_Small.in', 'Asec test input', False),
        'asec_medium_in': Type.FileSrc('../Test/In/Test_Asec_Medium.in', 'Asec test input', False),
        'asec_large_in': Type.FileSrc('../Test/In/Test_Asec_Large.in', 'Asec test input', False),
        'acot_small_in': Type.FileSrc('../Test/In/Test_Acot_Small.in', 'Acot test input', False),
        'acot_medium_in': Type.FileSrc('../Test/In/Test_Acot_Medium.in', 'Acot test input', False),
        'acot_large_in': Type.FileSrc('../Test/In/Test_Acot_Large.in', 'Acot test input', False),
        'erf_small_in': Type.FileSrc('../Test/In/Test_Erf_Small.in', 'Erf test input', False),
        'erf_medium_in': Type.FileSrc('../Test/In/Test_Erf_Medium.in', 'Erf test input', False),
        'erf_large_in': Type.FileSrc('../Test/In/Test_Erf_Large.in', 'Erf test input', False),
        'erfc_small_in': Type.FileSrc('../Test/In/Test_Erfc_Small.in', 'Erfc test input', False),
        'erfc_medium_in': Type.FileSrc('../Test/In/Test_Erfc_Medium.in', 'Erfc test input', False),
        'erfc_large_in': Type.FileSrc('../Test/In/Test_Erfc_Large.in', 'Erfc test input', False),
        'gamma_small_in': Type.FileSrc('../Test/In/Test_Gamma_Small.in', 'Gamma test input', False),
        'gamma_medium_in': Type.FileSrc('../Test/In/Test_Gamma_Medium.in', 'Gamma test input', False),
        'gamma_large_in': Type.FileSrc('../Test/In/Test_Gamma_Large.in', 'Gamma test input', False),
        'lgamma_small_in': Type.FileSrc('../Test/In/Test_Lgamma_Small.in', 'Lgamma test input', False),
        'lgamma_medium_in': Type.FileSrc('../Test/In/Test_Lgamma_Medium.in', 'Lgamma test input', False),
        'lgamma_large_in': Type.FileSrc('../Test/In/Test_Lgamma_Large.in', 'Lgamma test input', False),
        'beta_small_in': Type.FileSrc('../Test/In/Test_Beta_Small.in', 'Beta test input', False),
        'beta_medium_in': Type.FileSrc('../Test/In/Test_Beta_Medium.in', 'Beta test input', False),
        'beta_large_in': Type.FileSrc('../Test/In/Test_Beta_Large.in', 'Beta test input', False),
        'custom_ref': Type.FileSrc('../Test/Ref/Test.ref', 'Custom ref output', False),
        'sin_small_ref': Type.FileSrc('../Test/Ref/Test_Sin_Small.ref', 'Sin ref output', False),
        'sin_medium_ref': Type.FileSrc('../Test/Ref/Test_Sin_Medium.ref', 'Sin ref output', False),
        'sin_large_ref': Type.FileSrc('../Test/Ref/Test_Sin_Large.ref', 'Sin ref output', False),
        'cos_small_ref': Type.FileSrc('../Test/Ref/Test_Cos_Small.ref', 'Cos ref output', False),
        'cos_medium_ref': Type.FileSrc('../Test/Ref/Test_Cos_Medium.ref', 'Cos ref output', False),
        'cos_large_ref': Type.FileSrc('../Test/Ref/Test_Cos_Large.ref', 'Cos ref output', False),
        'tan_small_ref': Type.FileSrc('../Test/Ref/Test_Tan_Small.ref', 'Tan ref output', False),
        'tan_medium_ref': Type.FileSrc('../Test/Ref/Test_Tan_Medium.ref', 'Tan ref output', False),
        'tan_large_ref': Type.FileSrc('../Test/Ref/Test_Tan_Large.ref', 'Tan ref output', False),
        'csc_small_ref': Type.FileSrc('../Test/Ref/Test_Csc_Small.ref', 'Csc ref output', False),
        'csc_medium_ref': Type.FileSrc('../Test/Ref/Test_Csc_Medium.ref', 'Csc ref output', False),
        'csc_large_ref': Type.FileSrc('../Test/Ref/Test_Csc_Large.ref', 'Csc ref output', False),
        'sec_small_ref': Type.FileSrc('../Test/Ref/Test_Sec_Small.ref', 'Sec ref output', False),
        'sec_medium_ref': Type.FileSrc('../Test/Ref/Test_Sec_Medium.ref', 'Sec ref output', False),
        'sec_large_ref': Type.FileSrc('../Test/Ref/Test_Sec_Large.ref', 'Sec ref output', False),
        'cot_small_ref': Type.FileSrc('../Test/Ref/Test_Cot_Small.ref', 'Cot ref output', False),
        'cot_medium_ref': Type.FileSrc('../Test/Ref/Test_Cot_Medium.ref', 'Cot ref output', False),
        'cot_large_ref': Type.FileSrc('../Test/Ref/Test_Cot_Large.ref', 'Cot ref output', False),
        'asin_small_ref': Type.FileSrc('../Test/Ref/Test_Asin_Small.ref', 'Asin ref output', False),
        'acos_small_ref': Type.FileSrc('../Test/Ref/Test_Acos_Small.ref', 'Acos ref output', False),
        'atan_small_ref': Type.FileSrc('../Test/Ref/Test_Atan_Small.ref', 'Atan ref output', False),
        'atan_medium_ref': Type.FileSrc('../Test/Ref/Test_Atan_Medium.ref', 'Atan ref output', False),
        'atan_large_ref': Type.FileSrc('../Test/Ref/Test_Atan_Large.ref', 'Atan ref output', False),
        'acsc_small_ref': Type.FileSrc('../Test/Ref/Test_Acsc_Small.ref', 'Acsc ref output', False),
        'acsc_medium_ref': Type.FileSrc('../Test/Ref/Test_Acsc_Medium.ref', 'Acsc ref output', False),
        'acsc_large_ref': Type.FileSrc('../Test/Ref/Test_Acsc_Large.ref', 'Acsc ref output', False),
        'asec_small_ref': Type.FileSrc('../Test/Ref/Test_Asec_Small.ref', 'Asec ref output', False),
        'asec_medium_ref': Type.FileSrc('../Test/Ref/Test_Asec_Medium.ref', 'Asec ref output', False),
        'asec_large_ref': Type.FileSrc('../Test/Ref/Test_Asec_Large.ref', 'Asec ref output', False),
        'acot_small_ref': Type.FileSrc('../Test/Ref/Test_Acot_Small.ref', 'Acot ref output', False),
        'acot_medium_ref': Type.FileSrc('../Test/Ref/Test_Acot_Medium.ref', 'Acot ref output', False),
        'acot_large_ref': Type.FileSrc('../Test/Ref/Test_Acot_Large.ref', 'Acot ref output', False),
        'erf_small_ref': Type.FileSrc('../Test/Ref/Test_Erf_Small.ref', 'Erf ref output', False),
        'erf_medium_ref': Type.FileSrc('../Test/Ref/Test_Erf_Medium.ref', 'Erf ref output', False),
        'erf_large_ref': Type.FileSrc('../Test/Ref/Test_Erf_Large.ref', 'Erf ref output', False),
        'erfc_small_ref': Type.FileSrc('../Test/Ref/Test_Erfc_Small.ref', 'Erfc ref output', False),
        'erfc_medium_ref': Type.FileSrc('../Test/Ref/Test_Erfc_Medium.ref', 'Erfc ref output', False),
        'erfc_large_ref': Type.FileSrc('../Test/Ref/Test_Erfc_Large.ref', 'Erfc ref output', False),
        'gamma_small_ref': Type.FileSrc('../Test/Ref/Test_Gamma_Small.ref', 'Gamma ref output', False),
        'gamma_medium_ref': Type.FileSrc('../Test/Ref/Test_Gamma_Medium.ref', 'Gamma ref output', False),
        'gamma_large_ref': Type.FileSrc('../Test/Ref/Test_Gamma_Large.ref', 'Gamma ref output', False),
        'lgamma_small_ref': Type.FileSrc('../Test/Ref/Test_Lgamma_Small.ref', 'Lgamma ref output', False),
        'lgamma_medium_ref': Type.FileSrc('../Test/Ref/Test_Lgamma_Medium.ref', 'Lgamma ref output', False),
        'lgamma_large_ref': Type.FileSrc('../Test/Ref/Test_Lgamma_Large.ref', 'Lgamma ref output', False),
        'beta_small_ref': Type.FileSrc('../Test/Ref/Test_Beta_Small.ref', 'Beta ref output', False),
        'beta_medium_ref': Type.FileSrc('../Test/Ref/Test_Beta_Medium.ref', 'Beta ref output', False),
        'beta_large_ref': Type.FileSrc('../Test/Ref/Test_Beta_Large.ref', 'Beta ref output', False)
    }

    __inst = None

    def __init__(self) -> None:
        self.__handle_tb: Dict[str, Union[float, Type.CmdT, Type.FunT]] = {}
        self.__storage: List[Union[Dict[str, str], List[str]]] = []
        self.__storage_test: List[List[Decimal]] = []

    def __del__(self) -> None:
        pass

    def __load_hlpr(self, path: str, tag: bool = False) -> None:
        """
        Load DB from source file.

        There are two modes of parsing.
            1. Plain mode.
               This mode is used for no tagged DB source file.
               One line which is not empty in the source file is considered as one item.
               The parsed item is stored sequentially.
            2. Tag mode.
               This mode is used for tagged DB source file.
               Each item consists of one tag and one content.
               Here, content can span multiple lines whereas tag cannot.
               Tag starts with special delimiter character $ and there should be no leading whitespaces.
               Also, # in tag will not be considered as a start of comment.
        In both mode, any character after # will be considered as commend and will not be parsed.
        Note that the grammar for DB source is strict.
        In case of violation (two adjacent tags, for example), it will show unexpected behavior.

        This method is private and called internally as a helper of ``DB.load``.
        For detailed description for DB loading chain, refer to the comments of ``DB.load``.

        :param path: Path of source file.
        :type path: str
        :param tag: Flag for tagged DB source. (Default: False)
        :type tag: bool
        """
        # Open source file.
        try:
            src: TextIO = open(path)  # Source file.
        except OSError as os_err:
            raise Error.DBErr(Type.DBErrT.OPEN_ERR, path, os_err.strerror)

        if tag:
            # Tagged mode.
            # Parsing tagged DB source file comprises of two steps.
            #   1. Parse tag.
            #      If it finds tag delimiter $, then the whole line except for trailing newline character is tag.
            #   2. Parse item.
            #      If there is no tag delimiter, the whole line excluding any character after comment delimiter # is a
            #      part of item.
            #      In tagged mode, even the trailing newline character is a part of item.
            # Note that if it detects tag, it must store previously parsed item with previously parsed tag.
            # Also, do not forget to store the last parsed item with last parsed tag.
            # The following logic is an implementation of these steps.
            storage: Dict[str, str] = {}  # Storage of tagged DB.
            tag: str = ''  # Parsed tag.
            it: str = ''  # Parsed item.

            self.__storage.append(storage)

            while True:
                line: str = src.readline()  # Current parsing line in the source file.

                if not line:
                    break

                pos: int = 0  # Current parsing position.

                while pos < len(line):
                    # Parse tag.
                    if is_tag(line[pos]):
                        # Store previously parsed item with previously parsed tag.
                        if it:
                            storage[tag] = it
                            it = ''

                        tag = line[pos + 1:-1]

                        break
                    # Parse item with comment.
                    elif is_comment(line[pos]):
                        it += line[:pos]

                        break

                    pos += 1

                # Parse item w/o comment.
                if pos == len(line):
                    it += line

            # Store last item with last tag.
            storage[tag] = it
        else:
            # Plain mode.
            # Parsing not tagged DB source file is simple.
            # For each line, which is not empty, the whole line excluding any character after comment delimiter # is one
            # item.
            # In no tag mode, trailing newline character will be dropped.
            # The following logic is an implementation of these steps.
            storage: List[str] = []  # Storage of not tagged DB.

            self.__storage.append(storage)

            while True:
                line: str = src.readline()  # Current parsing line in the source file.

                if not line:
                    break

                pos: int = 0  # Current parsing position.

                # Parse item with comment.
                while pos < len(line):
                    if is_comment(line[pos]):
                        if line[:pos]:
                            storage.append(line[:pos])

                        break

                    pos += 1

                # Parse item w/o comment.
                if pos == len(line) and not is_newline(line[0]):
                    if is_newline(line[-1]):
                        storage.append(line[:-1])
                    else:
                        storage.append(line)

        # Close source file.
        try:
            src.close()
        except OSError as os_err:
            raise Error.DBErr(Type.DBErrT.CLOSE_ERR, path, os_err.strerror)

    def __load_test_hlpr(self, path: str) -> None:
        """
        Load test DB from source file.

        DB source file for test has very strict (more than usual tagged or not tagged source files) grammar, which is
        inevitable for fast parsing.
        Each line must represent (arbitrary precision) numeric value.
        There must be to tag, empty lines, comments and even characters besides ``e`` for exponential.
        The parsed item is stored sequentially as Decimal class which preserves the test input's precision.
        In case of violation (existence of comment, for example), it will show unexpected behavior.

        This method is private and called internally as a helper of ``DB.load_test``.
        For detailed description for test DB loading, refer to the comments of ``DB.load_test``.

        :param path: Path of source file.
        :type path: str
        """
        # Open source file.
        try:
            src: TextIO = open(path)  # Source file.
        except OSError as os_err:
            raise Error.DBErr(Type.DBErrT.OPEN_ERR, path, os_err.strerror)

        # Parsing test source file is trivial.
        # Each line is one numeric value.
        # The following logic is an implementation of these steps.
        storage: List[Decimal] = []  # Storage of test DB.

        self.__storage_test.append(storage)

        while True:
            line: str = src.readline()  # Current parsing line in the source file.

            if not line:
                break

            storage.append(Decimal(line))

        # Close source file.
        try:
            src.close()
        except OSError as os_err:
            raise Error.DBErr(Type.DBErrT.CLOSE_ERR, path, os_err.strerror)

    @classmethod
    def inst(cls):
        """
        Getter for singleton object.

        If it is the first time calling this, it initializes the singleton objects.
        This automatically supports so called lazy initialization.

        :return: Singleton object.
        :rtype: DB
        """
        if not cls.__inst:
            cls.__inst = DB()

        return cls.__inst

    def load(self, debug: bool = False) -> None:
        """
        Load DB sources.

        DB loading consists of two steps.
            1. Register handles.
               At this step, it registers function/command/constant handles.
               For fast search, key is hashed value of string.
            2. Load source files.
               At this step, it open source files, parse it and store it properly.

        This method supports brief summary outputs which can be used for debugging.

        :param debug: Flag for debug mode. (Default: False)
        :type debug: bool
        """

        if debug:
            from sys import getsizeof
            from os import getcwd
            import time

            buf: Type.BufT = Type.BufT.DEBUG  # Debug buffer.

            # Print out loading target.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('database info'), buf)
            Printer.Printer.inst().buf(f'@pwd : {getcwd()}', buf, indent=2)
            Printer.Printer.inst().buf('@path:', buf, indent=2)

            for _, src in self.__FILE_SRC.items():
                tag: str = 'tag' if src.tag else 'plain'  # Type of source file.

                Printer.Printer.inst().buf(f'[{src.idx}] {src.path:28} ({tag})', buf, indent=4)

            Printer.Printer.inst().buf_newline(buf)
            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('start database loading'), buf)

            # Register function/command/constant handles.
            start: float = time.process_time()  # Start time stamp for elapsed time measure.
            cnt: int = 0  # DB load counter.

            for src in self.__HANDLE_SRC:
                bf_cnt: int = len(self.__handle_tb)  # # of items in table before registration.
                bf_sz: int = getsizeof(self.__handle_tb)  # Size of table before registration.
                Printer.Printer.inst().buf(Printer.Printer.inst().f_prog(f'[{cnt}] Registering {src.brief}'), buf,
                                           False, 2)

                for handle in src.enum:
                    self.__handle_tb[handle.name.capitalize()] = handle

                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
                Printer.Printer.inst().buf(
                    f'@size: {len(self.__handle_tb) - bf_cnt} ({getsizeof(self.__handle_tb) - bf_sz} bytes)', buf,
                    indent=4)
                Printer.Printer.inst().buf_newline(buf)
                cnt += 1

            tot_cnt: int = len(self.__handle_tb)  # Total # of DB items.
            tot_sz: int = getsizeof(self.__handle_tb)  # Total size of DB.

            # Load DB source files.
            for _, src in self.__FILE_SRC.items():
                Printer.Printer.inst().buf(Printer.Printer.inst().f_prog(f'[{cnt}] Loading {src.brief}'), buf, False, 2)

                try:
                    self.__load_hlpr(src.path, src.tag)
                except Error.DBErr as DB_err:
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)
                    Printer.Printer.inst().buf_newline(buf)

                    raise DB_err
                else:
                    Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)

                Printer.Printer.inst().buf(f'@size: {len(self.__storage[-1])} ({getsizeof(self.__storage[-1])} bytes)',
                                           buf, indent=4)
                Printer.Printer.inst().buf_newline(buf)
                cnt += 1
                tot_cnt += len(self.__storage[-1])
                tot_sz += getsizeof(self.__storage[-1])

            elapsed: float = time.process_time() - start  # Elapsed time.

            Printer.Printer.inst().buf(Printer.Printer.inst().f_title('database loading finished'), buf)
            Printer.Printer.inst().buf(f'@total size: {tot_cnt} ({tot_sz} bytes)', buf, indent=2)
            Printer.Printer.inst().buf(f'@elapsed   : {elapsed * 1000:.2f}ms', buf, indent=2)
            Printer.Printer.inst().buf_newline(buf)
        else:
            for src in self.__HANDLE_SRC:
                for handle in src.enum:
                    self.__handle_tb[handle.name.capitalize()] = handle

            for _, src in self.__FILE_SRC.items():
                self.__load_hlpr(src.path, src.tag)

    def load_test(self) -> None:
        """
        Load test DB sources.

        It just open and load two source files, one is test input and the other is test reference output generated by
        MATLAB.
        These two source files are plain DB sources with strict format.
        That is, there must be no comments and each line is comprised of one numeric value.

        Unlike ``DB.load``, it clears storage for test DB before loading.
        Thus there is always at most one loaded test DB.
        This is because the size of test input and reference output can be quite large, exceeding 1MB.

        This method always shows brief summary outputs which can be used for debugging.
        """

        from sys import getsizeof
        from os import getcwd
        import time

        buf: Type.BufT = Type.BufT.DEBUG  # Debug buffer.

        # Print out loading target.
        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('database info'), buf)
        Printer.Printer.inst().buf(f'@pwd : {getcwd()}', buf, indent=2)
        Printer.Printer.inst().buf('@path:', buf, indent=2)

        for _, src in self.__TEST_SRC.items():
            Printer.Printer.inst().buf(f'[{src.idx - self.__TEST_IDX_OFFSET:02d}] {src.path}', buf, indent=4)

        Printer.Printer.inst().buf_newline(buf)

        # Load DB source files.
        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('start database loading'), buf)

        start: float = time.process_time()  # Start time stamp for elapsed time measure.

        # Register function/command/constant handles.
        cnt: int = 0  # DB load counter.

        for src in self.__HANDLE_SRC:
            bf_cnt: int = len(self.__handle_tb)  # # of items in table before registration.
            bf_sz: int = getsizeof(self.__handle_tb)  # Size of table before registration.
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog(f'[{cnt}] Registering {src.brief}'), buf,
                                       False, 2)

            for handle in src.enum:
                self.__handle_tb[handle.name.capitalize()] = handle

            Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)
            Printer.Printer.inst().buf(
                f'@size: {len(self.__handle_tb) - bf_cnt} ({getsizeof(self.__handle_tb) - bf_sz} bytes)', buf,
                indent=4)
            Printer.Printer.inst().buf_newline(buf)
            cnt += 1

        tot_cnt: int = len(self.__handle_tb)  # Total # of DB items.
        tot_sz: int = getsizeof(self.__handle_tb)  # Total size of DB.

        # Load inputs and references.
        for k, src in self.__TEST_SRC.items():
            src_t: str = 'custom' if 'custom' in k else k[(k.find('_') + 1):k.find('_', k.find('_') + 1)]
            Printer.Printer.inst().buf(Printer.Printer.inst().f_prog(f'[{cnt}] Loading {src.brief}'), buf, False, 2)

            try:
                self.__load_test_hlpr(src.path)
            except Error.DBErr as DB_err:
                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('fail', Type.Col.RED), buf)
                Printer.Printer.inst().buf_newline(buf)

                raise DB_err
            else:
                Printer.Printer.inst().buf(Printer.Printer.inst().f_col('done', Type.Col.BLUE), buf)

            Printer.Printer.inst().buf(
                f'@size: {len(self.__storage_test[-1])} ({getsizeof(self.__storage_test[-1])} bytes)', buf, indent=4)
            Printer.Printer.inst().buf(f'@type: {src_t}', buf, indent=4)
            Printer.Printer.inst().buf_newline(buf)
            tot_cnt += len(self.__storage_test[-1])
            tot_sz += getsizeof(self.__storage_test[-1])
            cnt += 1

        elapsed: float = time.process_time() - start  # Elapsed time.
        tot_cnt += len(self.__storage_test[1])
        tot_sz += getsizeof(self.__storage_test[1])

        Printer.Printer.inst().buf(Printer.Printer.inst().f_title('database loading finished'), buf)
        Printer.Printer.inst().buf(f'@total size: {tot_cnt} ({tot_sz} bytes)', buf, indent=2)
        Printer.Printer.inst().buf(f'@elapsed   : {elapsed * 1000:.2f}ms', buf, indent=2)
        Printer.Printer.inst().buf_newline(buf)

    def get_handle(self, k: str) -> Union[float, Type.CmdT, Type.FunT]:
        """
        Getter for function/command/constant handle.

        :param k: Name of handle to get.
        :type k: int

        :return: Found handle with corresponding key. None in case of not found.
        :rtype: Union[float, Type.CmdT, Type.FunT]
        """
        return self.__handle_tb.get(k)

    def get_greet_msg(self, k: str) -> str:
        """
        Getter for greeting messages.

        :param k: Tag of greeting message to get.
        :type k: str

        :return: Meta information with corresponding tag.
        :rtype: str
        """
        return self.__storage[self.__FILE_SRC.get('greet_msg').idx].get(k)

    def get_err_msg(self, idx: int) -> str:
        """
        Getter for error message.

        :param idx: Index of error message to get.
        :type idx: int

        :return: Error message with corresponding index.
        :rtype: str
        """
        return self.__storage[self.__FILE_SRC.get('err_msg').idx][idx]

    def get_warn_msg(self, idx: int) -> str:
        """
        Getter for warning message.

        :param idx: Index of warning message to get.
        :type idx: int

        :return: Warning message with corresponding index.
        :rtype: str
        """
        return self.__storage[self.__FILE_SRC.get('warn_msg').idx][idx]

    def get_debug_in(self, idx: int) -> str:
        """
        Getter for debug input.

        :param idx: Index of debug input to get.
        :type idx: int

        :return: Debug input with corresponding index.
        :rtype: str
        """
        return self.__storage[self.__FILE_SRC.get('debug_in').idx][idx]

    def get_debug_out(self, k: str) -> str:
        """
        Getter for debug output.

        :param k: Tag of debug output to get.
        :type k: str

        :return: Debug output with corresponding tag
        :rtype: str
        """
        return self.__storage[self.__FILE_SRC.get('debug_out').idx].get(k)

    def get_sz(self, storage: str) -> int:
        """
        Get the # of DB items.

        :return: The # of DB items.
        :rtype: int
        """
        return len(self.__storage[self.__FILE_SRC.get(storage).idx])

    def get_test_in(self, fun: Type.FunT = None, sz: Type.TestSzT = None) -> List[Decimal]:
        """
        Getter for test input.

        :return: Test input.
        :rtype: List[Decimal]
        """
        storage = f'{fun.name.lower()}_{sz.name.lower()}_in' if fun else 'custom_in'

        return self.__storage_test[self.__TEST_SRC.get(storage).idx - self.__TEST_IDX_OFFSET]

    def get_test_ref(self, fun: Type.FunT = None, sz: Type.TestSzT = None) -> List[Decimal]:
        """
        Getter for test reference output.

        :return: Test reference output.
        :rtype: List[Decimal]
        """
        storage = f'{fun.name.lower()}_{sz.name.lower()}_ref' if fun else 'custom_ref'

        return self.__storage_test[self.__TEST_SRC.get(storage).idx - self.__TEST_IDX_OFFSET]

    def get_test_target(self) -> List[Tuple[Type.FunT, Type.TestSzT]]:
        keys: List[List[str]] = [k.split('_') for k in [k[:-3] for k in list(self.__TEST_SRC.keys())]]
        keys = keys[1:int(len(keys) / 2)]
        target: List[Tuple[Type.FunT, Type.TestSzT]] = []

        for k in keys:
            if k[1] == 'small':
                target.append((self.get_handle(k[0].capitalize()), Type.TestSzT.SMALL))
            elif k[1] == 'medium':
                target.append((self.get_handle(k[0].capitalize()), Type.TestSzT.MEDIUM))
            else:
                target.append((self.get_handle(k[0].capitalize()), Type.TestSzT.LARGE))

        return target
