from user_class import User
from NPO_class import NPO

class Campaign:
    def __init__(self, name, catalyst, NPO_input, story):
        self.campaign_name = name
        self.catalyst = catalyst
        self.NPO = NPO_input
        self.description = NPO.get_description()
        self.story = story
        self.users = {}
    
    def get_story(self):
        return self.story
        
    def add_user(self, username, parent = None, size = '0'):
        if self.users == {}:
            self.users[username] = size             #size is a string
        else:
            parent_size = self.users[parent.get_username()]
            self.users[username] = parent_size + size
    