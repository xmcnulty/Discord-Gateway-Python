
# Class that represents an attachment as defined by the Discord API.
class Attachment:
    def __init__(self, id, filename, size, url, proxy_url):
        self.id = id
        self.filename = filename
        self.size = size
        self.url = url
        self.proxy_url = proxy_url

    # description property this is optional and may be None
    @property
    def description(self) -> str:
        try:
            return self.__description
        except AttributeError:
            return None
    
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def height(self) -> int:
        try:
            return self.__height
        except AttributeError:
            return None
        
    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        try:
            return self.__width
        except AttributeError:
            return None
        
    @width.setter
    def width(self, width: int):
        self.__width = width

    # static method that creates an attachment object from a dictionary
    @staticmethod
    def from_dict(attachment_dict):
        return Attachment(
            attachment_dict["id"],
            attachment_dict["filename"],
            attachment_dict["size"],
            attachment_dict["url"],
            attachment_dict["proxy_url"]
        )