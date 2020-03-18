from Warning import Warning


class NumWarn(Warning.ParserWarn):
    def __init__(self, warnno: int, pos: int):
        super().__init__(warnno)
        self.__pos: int = pos

    @property
    def pos(self) -> int:
        return self.__pos
