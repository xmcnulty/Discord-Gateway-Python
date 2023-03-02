from Event import *

class Heartbeat(Event):
    def __init__(self, last_sequence_number: int):
        super().__init__(OpCode.HEARTBEAT, {})
        self.__last_sequence_number = last_sequence_number
    
    # returns json formatted string of event payload
    def json(self) -> str:
        return json.dumps(self.__dict__())
    
    def __dict__(self) -> dict:
        return {
            op: self.__op_code.value,
            d: self.__last_sequence_number
        }