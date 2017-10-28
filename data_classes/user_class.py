from campaign_class import Campaign

class User:
    def __init__(self, name, username, password, parent):
        self.first, self.last = name.split()
        self.parent = parent
        self.children = 6 * []
        self.username = username
        self.password = password
        self.size = 0
        self.campaign = parent.get_campaign()
        
    def get_username(self):
        return self.username
        
    def get_campaign(self):
        return self.campaign
        
    def add_user(self, user_name, user_username, user_password):
        new_user = User(user_name, user_username, user_password)
        self.children[self.size] = new_user
        self.campaign.add_user(user_name, self, str(self.size))
        self.size += 1
        
                 