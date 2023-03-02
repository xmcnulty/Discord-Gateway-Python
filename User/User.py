import json

class User:
    """
A wrapper class for Discord API User object.

This class provides a way to store and manipulate User object attributes returned by Discord API.

Attributes:
id (str): The ID of the user.
username (str): The username of the user.
discriminator (str): The discriminator of the user.
avatar (str): The avatar URL of the user.

Properties:
bot (bool): Whether the user is a bot or not.
system (bool): Whether the user is a Discord system user or not.
mfa_enabled (bool): Whether the user has two-factor authentication enabled on their account or not.
locale (str): The user's chosen language option.
verified (bool): Whether the user's email has been verified or not.
email (str): The email associated with the user's account.
flags (int): The user's flags.
premium_type (int): The type of Nitro subscription on a user's account.
public_flags (int): The user's public flags.
banner (str): The URL of the user's banner image.
accent_color (int): The user's chosen accent color.

Methods:
dict() -> dict: Returns a dictionary containing all the object attributes and their respective values.
json() -> str: Returns a JSON representation of the object attributes and their respective values.

from_dict(user_dict: dict) -> User: Creates a new User object from a dictionary representation of the object attributes and their respective values.
    """

    def __init__(
            self, 
            id: str, 
            username: str,
            discriminator: str,
            avatar: str):
        self.id = id
        self.username = username
        self.discriminator = discriminator
        self.avatar = avatar

    @property
    def bot(self) -> bool:
        try:
            return self.__bot
        except AttributeError:
            return None
        
    @bot.setter
    def bot(self, bot: bool):
        self.__bot = bot

    @property
    def system(self) -> bool:
        try:
            return self.__system
        except AttributeError:
            return None
        
    @system.setter
    def system(self, system: bool):
        self.__system = system

    @property
    def mfa_enabled(self) -> bool:
        try:
            return self.__mfa_enabled
        except AttributeError:
            return None
        
    @mfa_enabled.setter
    def mfa_enabled(self, mfa_enabled: bool):
        self.__mfa_enabled = mfa_enabled

    @property
    def locale(self) -> str:
        try:
            return self.__locale
        except AttributeError:
            return None
        
    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale

    @property
    def verified(self) -> bool:
        try:
            return self.__verified
        except AttributeError:
            return None
        
    @verified.setter
    def verified(self, verified: bool):
        self.__verified = verified

    @property
    def email(self) -> str:
        try:
            return self.__email
        except AttributeError:
            return None
        
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def flags(self) -> int:
        try:
            return self.__flags
        except AttributeError:
            return None
        
    @flags.setter
    def flags(self, flags: int):
        self.__flags = flags

    @property
    def premium_type(self) -> int:
        try:
            return self.__premium_type
        except AttributeError:
            return None
        
    
    @premium_type.setter
    def premium_type(self, premium_type: int):
        self.__premium_type = premium_type

    @property
    def public_flags(self) -> int:
        try:
            return self.__public_flags
        except AttributeError:
            return None
        
    @public_flags.setter
    def public_flags(self, public_flags: int):
        self.__public_flags = public_flags

    @property
    def banner(self) -> str:
        try:
            return self.__banner
        except AttributeError:
            return None
        
    @banner.setter
    def banner(self, banner: str):
        self.__banner = banner

    @property
    def accent_color(self) -> int:
        try:
            return self.__accent_color
        except AttributeError:
            return None
        
    @accent_color.setter
    def accent_color(self, accent_color: int):
        self.__accent_color = accent_color

    def __dict__(self) -> dict:
        payload = {
            "id": self.id,
            "username": self.username,
            "discriminator": self.discriminator,
            "avatar": self.avatar
        }

        # Add optional fields if they exist
        if self.bot is not None:
            payload["bot"] = self.bot
        
        if self.system is not None:
            payload["system"] = self.system
        
        if self.mfa_enabled is not None:
            payload["mfa_enabled"] = self.mfa_enabled

        if self.locale is not None:
            payload["locale"] = self.locale

        if self.verified is not None:
            payload["verified"] = self.verified

        if self.email is not None:
            payload["email"] = self.email

        if self.flags is not None:
            payload["flags"] = self.flags

        if self.premium_type is not None:
            payload["premium_type"] = self.premium_type

        if self.public_flags is not None:
            payload["public_flags"] = self.public_flags

        if self.banner is not None:
            payload["banner"] = self.banner

        if self.accent_color is not None:
            payload["accent_color"] = self.accent_color

        return payload
    
    def json(self) -> str:
        return json.dumps(self.__dict__())
    
    @staticmethod
    def from_dict(user_dict: dict) -> "User":
        user = User(
            id=user_dict["id"],
            username=user_dict["username"],
            discriminator=user_dict["discriminator"],
            avatar=user_dict["avatar"]
        )

        # Add optional fields if they exist
        if "bot" in user_dict:
            user.bot = user_dict["bot"]
        
        if "system" in user_dict:
            user.system = user_dict["system"]
        
        if "mfa_enabled" in user_dict:
            user.mfa_enabled = user_dict["mfa_enabled"]

        if "locale" in user_dict:
            user.locale = user_dict["locale"]

        if "verified" in user_dict:
            user.verified = user_dict["verified"]

        if "email" in user_dict:
            user.email = user_dict["email"]

        if "flags" in user_dict:
            user.flags = user_dict["flags"]

        if "premium_type" in user_dict:
            user.premium_type = user_dict["premium_type"]

        if "public_flags" in user_dict:
            user.public_flags = user_dict["public_flags"]

        if "banner" in user_dict:
            user.banner = user_dict["banner"]

        if "accent_color" in user_dict:
            user.accent_color = user_dict["accent_color"]

        return user