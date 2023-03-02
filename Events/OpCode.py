import enum

"""OpCodes for Discord Gateway"""
class OpCode(enum.Enum):
    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE_UPDATE = 3
    VOICE_STATE_UPDATE = 4
    RESUME = 6
    RECONNECT = 7
    REQUEST_GUILD_MEMBERS = 8
    INVALID_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11
    
# function that returns the opcode from its value
@staticmethod
def get_opcode(value) -> OpCode:
    for opcode in OpCode:
        if opcode.value == value:
            return opcode
    return None