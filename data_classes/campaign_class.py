from user_class import User
from NPO_class import NPO

class Campaign:
    def __init__(self, name, catalyst, NPO_input):
        self.campaign_name = name
        self.catalyst = catalyst
        self.NPO = NPO_input
        self.description = NPO.get_description()