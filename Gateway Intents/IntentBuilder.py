class IntentBuilder:
    """
    A class for building Intent values for the Discord API.

    Intents allow you to specify which events your bot should receive from Discord.
    You can create an IntentBuilder object and use its methods to add the desired intents.

    To get the final Intent value, call the `build()` method.

    Note:
        This class is specific to the Discord API and should not be used for other purposes.

    Attributes:
        __intent (int): The final Intent value.

    Methods:
        add_guilds: Adds the guilds intent.
        add_guild_members: Adds the guild members intent.
        add_guild_moderation: Adds the guild moderation intent.
        add_guild_emojis_and_stickers: Adds the guild emojis and stickers intent.
        add_guild_integrations: Adds the guild integrations intent.
        add_guild_webhooks: Adds the guild webhooks intent.
        add_guild_invites: Adds the guild invites intent.
        add_guild_voice_states: Adds the guild voice states intent.
        add_guild_presences: Adds the guild presences intent.
        add_guild_messages: Adds the guild messages intent.
        add_guild_message_reactions: Adds the guild message reactions intent.
        add_guild_message_typing: Adds the guild message typing intent.
        add_direct_messages: Adds the direct messages intent.
        add_direct_message_reactions: Adds the direct message reactions intent.
        add_direct_message_typing: Adds the direct message typing intent.
        add_guild_schedule_events: Adds the guild schedule events intent.
        add_auto_moderation_configuration: Adds the auto-moderation configuration intent.
        add_auto_moderation_execution: Adds the auto-moderation execution intent.
        add_all: Adds all available intents.
        build: Gets the final Intent value.

    Usage example:

        # Create an IntentBuilder object and add the desired intents
        intents = IntentBuilder().add_guilds().add_guild_members().add_guild_messages().build()

        # Use the intents variable when creating the bot client
        client = discord.Client(intents=intents)
    """
    def __init__(self) -> None:
        self.__intent = 0

    def add_guilds(self):
        self.__intent |= 1 << 0
        return self
    
    def add_guild_members(self):
        self.__intent |= 1 << 1
        return self
    
    def add_guild_moderation(self):
        self.__intent |= 1 << 2
        return self
    
    def add_guild_emojis_and_stickers(self):
        self.__intent |= 1 << 3
        return self
    
    def add_guild_integrations(self):
        self.__intent |= 1 << 4
        return self
    
    def add_guild_webhooks(self):
        self.__intent |= 1 << 5
        return self 
    
    def add_guild_invites(self):
        self.__intent |= 1 << 6
        return self
    
    def add_guild_voice_states(self):
        self.__intent |= 1 << 7
        return self
    
    def add_guild_presences(self):
        self.__intent |= 1 << 8
        return self
    
    def add_guild_messages(self):
        self.__intent |= 1 << 9
        return self
    
    def add_guild_message_reactions(self):
        self.__intent |= 1 << 10
        return self
    
    def add_guild_message_typing(self):
        self.__intent |= 1 << 11
        return self
    
    def add_direct_messages(self):
        self.__intent |= 1 << 12
        return self
    
    def add_direct_message_reactions(self):
        self.__intent |= 1 << 13
        return self
    
    def add_direct_message_typing(self):
        self.__intent |= 1 << 14
        return self
    
    def add_guild_schedule_events(self):
        self.__intent |= 1 << 16
        return self
    
    def add_auto_moderation_configuration(self):
        self.__intent |= 1 << 20
        return self
    
    def add_auto_moderation_execution(self):
        self.__intent |= 1 << 21
        return self
    
    def add_all(self):
        # calls all the add functions
        self.add_guilds()
        self.add_guild_members()
        self.add_guild_moderation()
        self.add_guild_emojis_and_stickers()
        self.add_guild_integrations()
        self.add_guild_webhooks()
        self.add_guild_invites()
        self.add_guild_voice_states()
        self.add_guild_presences()
        self.add_guild_messages()
        self.add_guild_message_reactions()
        self.add_guild_message_typing()
        self.add_direct_messages()
        self.add_direct_message_reactions()
        self.add_direct_message_typing()
        self.add_guild_schedule_events()
        self.add_auto_moderation_configuration()
        self.add_auto_moderation_execution()
        return self
    
    def build(self) -> int:
        return self.__intent