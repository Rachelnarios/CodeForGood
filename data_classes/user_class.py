from campaign_class import Campaign

class User:
    def __init__(self, name):
        self.first, self.last = name.split()
        self.parent = None
        self.children = 6 * []
        self.login = None
        self.password = None
        self.size = 0