
class Command:
    def execute(self, arg=None):
        assert False, "Command execute must be overridden"

class AddObj(Command):
    def __init__(self, world):
        self.world = world
        
    def execute(self, kind):
        print(kind)