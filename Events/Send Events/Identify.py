from Event import *

class Identify(Event):

    # Identify connection properties (os, browser, device)
    class ConnectionProperties:
        def __init__(
                self, 
                os: str = "windows", 
                browser: str = "chrome", 
                device: str = "my computer"
                ):
            self.os = os
            self.browser = browser
            self.device = device

        def __dict__(self) -> dict:
            return {
                "os": self.os,
                "browser": self.browser,
                "device": self.device
            }
        
    def __init__(
            self, 
            token: str, 
            intents: int, 
            properties: ConnectionProperties = ConnectionProperties(),
            compress: bool = None,
            large_threshold: int = None,
            shard: list = None,
            presence: dict = None):
        data = {
            "token": token,
            "intents": intents,
            "properties": properties.__dict__()
        }

        if compress is not None:
            data["compress"] = compress
        
        if large_threshold is not None:
            data["large_threshold"] = large_threshold
        
        if shard is not None:
            data["shard"] = shard

        if presence is not None:
            data["presence"] = presence
        
        super().__init__(OpCode.IDENTIFY, data)

    @property
    def token(self) -> str:
        return self.__data["token"]
    
    @token.setter
    def token(self, token: str):
        self.__data["token"] = token

    @property
    def intents(self) -> int:
        return self.__data["intents"]
    
    @intents.setter
    def intents(self, intents: int):
        self.__data["intents"] = intents
    
    @property
    def properties(self) -> ConnectionProperties:
        return self.__data["properties"]
    
    @properties.setter
    def properties(self, properties: ConnectionProperties):
        self.__data["properties"] = properties.__dict__()

    @property
    def compress(self) -> bool:
        try:
            return self.__data["compress"]
        except KeyError:
            return None
        
    @compress.setter
    def compress(self, compress: bool):
        self.__data["compress"] = compress

    @property
    def large_threshold(self) -> int:
        try:
            return self.__data["large_threshold"]
        except KeyError:
            return None
        
    @large_threshold.setter
    def large_threshold(self, large_threshold: int):
        self.__data["large_threshold"] = large_threshold

    @property
    def shard(self) -> list:
        try:
            return self.__data["shard"]
        except KeyError:
            return None
        
    @shard.setter
    def shard(self, shard: list):
        self.__data["shard"] = shard

    @property
    def presence(self) -> dict:
        try:
            return self.__data["presence"]
        except KeyError:
            return None
    
    @presence.setter
    def presence(self, presence: dict):
        self.__data["presence"] = presence