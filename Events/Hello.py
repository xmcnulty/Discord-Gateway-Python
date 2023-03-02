from Event import *

"""
Event for when the client receives a hello event from the gateway.
Sent on connection to gateway. Contains heartbeat interval in milliseconds.
"""
class Hello(Event):
    def __init__(self, data: dict):
        super().__init__(OpCode.HELLO, data)

    @property
    def heartbeat_interval(self) -> int:
        return self.__data["heartbeat_interval"]