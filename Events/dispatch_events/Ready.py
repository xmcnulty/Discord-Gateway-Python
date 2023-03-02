from DispatchEvent import *

class Ready(DispatchEvent):
    def __init__(self, data: dict, sequence: int):
        super().__init__(data, "READY", sequence)

    @property
    def version(self) -> int:
        return self.__data["v"]
    
    @property
    def user(self) -> dict:
        return self.__data["user"]
    
    @property
    def guilds(self) -> list:
        return self.__data["guilds"]
    
    @property
    def session_id(self) -> str:
        return self.__data["session_id"]
    
    @property
    def resume_gateway_url(self) -> str:
        return self.__data["resume_gateway_url"]
    
    @property
    def shard(self) -> list:
        return self.__data["shard"]
    
    @property
    def application(self) -> dict:
        return self.__data["application"]