class Chart:
    def __init__(self, code, day, opening, highest, lowest, closing, volume):
        self.__code = code
        self.__day = day
        self.__opening = opening
        self.__closing = closing
        self.__highest = highest
        self.__lowest = lowest
        self.__volume = volume

    @property
    def code(self):
        return self.__code

    @property
    def day(self):
        return self.__day

    @property
    def opening(self):
        return self.__opening

    @property
    def closing(self):
        return self.__closing

    @property
    def highest(self):
        return self.__highest

    @property
    def lowest(self):
        return self.__lowest

    @property
    def volume(self):
        return self.__volume

    def __repr__(self):
        return str({
            'code': self.code,
            'day': self.day,
            'opening': self.opening,
            'closing': self.closing,
            'highest': self.highest,
            'lowest': self.lowest,
            'volume': self.volume
        })