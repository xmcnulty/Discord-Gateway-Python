
# Role object as defined in the Discord API documentation
class Role:
    def __init__(self, role_id, name, color, hoist, position, permissions, managed, mentionable):
        self.role_id = role_id
        self.name = name
        self.color = color
        self.hoist = hoist
        self.position = position
        self.permissions = permissions
        self.managed = managed
        self.mentionable = mentionable

    # Returns the role's ID
    @property
    def id(self):
        return self.role_id

    # Returns the role's name
    @property
    def name(self):
        return self.name

    # Returns the role's color
    @property
    def color(self):
        return self.color

    # Returns whether the role is hoisted
    @property
    def hoist(self):
        return self.hoist

    # Returns the role's position
    @property
    def position(self):
        return self.position

    # Returns the role's permissions
    @property
    def permissions(self):
        return self.permissions

    # Returns whether the role is managed
    @property
    def managed(self):
        return self.managed

    # Returns whether the role is mentionable
    @property
    def mentionable(self):
        return self.mentionable

    # Returns the role's ID
    @id.setter
    def id(self, role_id):
        self.role_id = role_id

    # Sets the role's name
    @name.setter
    def name(self, name):
        self.name = name

    # Sets the role's color
    @color.setter
    def color(self, color):
        self.color = color

    # Sets whether the role is hoisted
    @hoist.setter
    def hoist(self, hoist):
        self.hoist = hoist

    # Sets the role's position
    @position.setter
    def position(self, position):
        self.position = position

    # Sets the role's permissions
    @permissions.setter
    def permissions(self, permissions):
        self.permissions = permissions

    # Sets whether the role is managed
    @managed.setter
    def managed(self, managed):
        self.managed = managed

    # Sets whether the role is mentionable
    @mentionable.setter
    def mentionable(self, mentionable):
        self.mentionable = mentionable

    # Builds a role object form a dictionary payload
    @staticmethod
    def from_dict(payload: dict):
        role_id = payload["id"]
        name = payload["name"]
        color = payload["color"]
        hoist = payload["hoist"]
        position = payload["position"]
        permissions = payload["permissions"]
        managed = payload["managed"]
        mentionable = payload["mentionable"]

        return Role(role_id, name, color, hoist, position, permissions, managed, mentionable)