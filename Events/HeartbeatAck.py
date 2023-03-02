from Event import *

class HeartbeatAck(Event):
    def __init__(self):
        super().__init__(OpCode.HEARTBEAT_ACK, None)

    def __dict__(self) -> dict:
        return {
            "op": self.__op_code.value
        }
    
    def json(self) -> str:
        return json.dumps(self.__dict__())