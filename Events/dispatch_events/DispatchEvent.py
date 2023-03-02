from Event import *

class DispatchEvent(Event):
    def __init__(self, data: dict, name: str, sequence: int):
        super().__init__(OpCode.DISPATCH, data)
        self.name = name
        self.sequence_number = sequence

    @staticmethod
    def from_raw(data: dict):
        name = data["t"]

        if name == "MESSAGE_CREATE":
            return MessageCreate(data)