from OpCode import *
import json

# payload keys
op = "op"
d = "d"
s = "s"
t = "t"


"""Parent class for all events."""
class Event:
    def __init__(self, op_code: OpCode, data: dict):
        self.__op_code = op_code
        self.__data = data

    @property
    def op_code(self) -> OpCode:
        return self.__op_code
    
    # returns json formatted string of event payload
    @property
    def json(self) -> str:
        return json.dumps(self.__dict__())
    
    def __dict__(self) -> dict:
        return {
            op: self.__op_code.value,
            d: self.__data
        }
    
event = Event(OpCode.IDENTIFY, {})

print(event.json)