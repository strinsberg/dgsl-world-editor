
class GameWorld:

    def __init__(self):
        self.name = "untitled"
        self.rooms = []
        self.player = None  # add a class or factory method for player
    
    def get_entities(self):
        return []
    
    def get_events(self):
        return []
        
    def save(self):
        # put everything here to save the world with it's filename
        # etc. Make sure that the world is converted to a dict
        # so that it can be saved and loaded with json
        pass
    
    def load(self, filename):
        pass
    