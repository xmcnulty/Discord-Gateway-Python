from DispatchEvent import *
from user.User import User
from roles.Role import Role
from attachments.Attachment import Attachment

"""
Represents a message create event.
"""
class MessageCreate(DispatchEvent):
    def __init__(self, data: dict,  sequence: int):
        super().__init__(data, "MESSAGE_CREATE",  sequence)

    @property
    def id(self) -> int:
        return self.__data["d"]["id"]
    
    @property
    def channel_id(self) -> int:
        return self.__data["d"]["channel_id"]
    
    @property
    def author(self) -> User:
        try:
            return self.__author
        except AttributeError:
            self.__author = User.from_raw(self.__data["d"]["author"])
            return self.__author
    
    @property
    def content(self) -> str:
        return self.__data["d"]["content"]
    
    @property
    def timestamp(self) -> str:
        return self.__data["d"]["timestamp"]
    
    @property
    def edited_timestamp(self) -> str:
        return self.__data["d"]["edited_timestamp"]
    
    @property
    def tts(self) -> bool:
        return self.__data["d"]["tts"]
    
    @property
    def mention_everyone(self) -> bool:
        return self.__data["d"]["mention_everyone"]
    
    @property
    def mentions(self) -> list:
        try:
            return self.__mentioned_users
        except AttributeError:
            self.__mentioned_users = []

            for user in self.__data["d"]["mentions"]:
                self.__mentioned_users.append(User.from_raw(user))

            return self.__mentioned_users
    
    @property
    def mention_roles(self) -> list:
        try:
            return self.__roles
        except AttributeError:
            self.__roles = []

            for role in self.__data["d"]["mention_roles"]:
                self.__roles.append(Role.from_dict(role))

    @property
    def attachments(self) -> list:
        try:
            return self.__attachments
        except AttributeError:
            self.__attachments = []

            for attachment in self.__data["d"]["attachments"]:
                
                attachment_object = Attachment.from_dict(attachment)

                # sets description, height, and width if they exist
                if "description" in attachment:
                    attachment_object.description = attachment["description"]
                
                if "height" in attachment:
                    attachment_object.height = attachment["height"]

                if "width" in attachment:
                    attachment_object.width = attachment["width"]

                self.__attachments.append(attachment_object)

            return self.__attachments