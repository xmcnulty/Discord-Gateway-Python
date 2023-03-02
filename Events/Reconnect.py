from Event import *

class Reconnect(Event):
    def __init__(self):
        super().__init__(OpCode.RECONNECT, None)