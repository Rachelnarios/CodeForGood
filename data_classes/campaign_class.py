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
    
    def find_user(self, username):
        user_location = self.users[username]
        user = None
        for char in user_location:
            index = int(char)
            if user == None:
                user = self.catalyst[index]
            else:
                user = user[index]
        return user
            
        