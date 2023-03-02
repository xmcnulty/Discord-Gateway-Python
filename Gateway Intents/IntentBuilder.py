class IntentBuilder:
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