from Event import *

class InvalidSession(Event):
    def __init__(self, data: dict):
        super().__init__(OpCode.INVALID_SESSION, data)

    @property
    def is_resumable(self) -> bool:
        return self.__data["d"]