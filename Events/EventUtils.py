import OpCode
from dispatch_events import *
from send_events import Heartbeat
import Hello, HeartbeatAck, InvalidSession, Reconnect
from .HeartbeatAck import HeartbeatAck
from Event import d, op
import InvalidSession


async def send_event(event, websocket):
    await websocket.send(event.json)

def get_event(event):
    op_code = event[op]
    data = event[d]

    if op_code == OpCode.HELLO:
        return Hello(data)
    elif op_code == OpCode.HEARTBEAT:
        return Heartbeat(data)
    elif op_code == OpCode.HEARTBEAT_ACK:
        return HeartbeatAck()
    elif op_code == OpCode.INVALID_SESSION:
        return InvalidSession(data)
    elif op_code == OpCode.RECONNECT:
        return Reconnect()
    elif op_code == OpCode.DISPATCH:
        return Dispatch(data)
    else:
        raise Exception(f"Invalid OpCode {op_code}")