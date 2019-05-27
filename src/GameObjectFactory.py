import game_data as gd
import uuid


class GameObjectFactory:

    # Given an entity type return that type of game data object
    def make(self, kind, verb=None, name=''):
        if kind == 'player':
            return self.makePlayer()
        elif kind == 'room':
            return self.makeRoom(kind, name)
        elif kind == 'door':
            return self.makeDoor(kind, name)
        elif kind in gd.entities:
            return self.makeEntity(kind, name)
        elif kind == "inform":
            return self.makeInform(kind, verb)
        elif kind == "kill":
            return self.makeKill(verb)
        elif kind == "transfer":
            return self.makeTransfer(verb)
        elif kind == "toggle":
            return self.makeToggle(verb)
        elif kind == "move":
            return self.makeMove(verb)
        elif kind in ["group", "ordered", "interaction"]:
            return self.makeGroup(kind, verb)
        elif kind == "conditional":
            return self.makeConditional(verb)
        elif kind == "hasItem":
            return self.makeHasItem(name)
        elif kind == "protected":
            return self.makeProtected(name)
        elif kind == "question":
            return self.makeQuestion(name)
        else:
            assert False, "Object factory has no type: " + kind
    
    # Player ###################################################
    
    def makePlayer(self):
        return {
            "id": "None",
            "type": "player",
            "items": [],
            "start": None,
            "name": "user supplied",
            "get_name": True,
        }
    
    # Entity ###################################################
    def makeEntity(self, kind, name):
        return {
            "id": str(uuid.uuid4()),
            "type": kind,
            "name": name,
            "description": "",
            "events": [],
            "items": [],
            "active": 1,
            "obtainable": 1,
            "hidden": 0
        }
        # need to make some kind of alteration to accomadate
        # other types of entities. Like rooms have default states
    
    def makeRoom(self, kind, name):
        room = self.makeEntity(kind, name)
        room['obtainable'] = 0
        return room
        
    
    # Events ###################################################
    def makeEvent(self, kind, verb=None):
        event = {
            "id": str(uuid.uuid4()),
            "type": kind,
            "name": "",
            "subjects": [],
            "once": 0,
        }
        if verb:
            event["verb"] = verb
        return event

    def makeInform(self, kind, verb=None):
        event = self.makeEvent(kind, verb)
        event["message"] = ""
        return event
    
    def makeKill(self, verb=None):
        event = self.makeInform("kill", verb)
        event["ending"] = 0
        return event
    
    def makeTransfer(self, verb=None):
        event = self.makeEvent("transfer", verb)
        event["target"] = None
        event["toTarget"] = 0
        event["item"] = None
        return event
    
    def makeToggle(self, verb=None):
        event = self.makeEvent("toggle", verb)
        event["target"] = None
        return event
    
    def makeMove(self, verb=None):
        event = self.makeEvent("move", verb)
        event["destination"] = None
        return event
    
    # Group Events #############################################
    def makeGroup(self, kind, verb=None):
        event = self.makeEvent(kind, verb)
        event["events"] = []
        event["repeats"] = 0
        return event
    
    def makeConditional(self, verb=None):
        event = self.makeEvent("conditional", verb)
        event["condition"] = None
        event["success"] = None
        event["failure"] = None
        return event
    
    # Conditions ###############################################
    def makeCondition(self, kind, name):
        return {"type": kind, 'name': name}
    
    def makeHasItem(self, name):
        cond = self.makeCondition("hasItem", name)
        cond["item"] = None
        cond["other"] = None
        return cond
        
    def makeProtected(self, name):
        cond = self.makeCondition("protected", name)
        cond["atmosphere"] = 'oxygen'
        return cond
    
    def makeQuestion(self, name):
        cond = self.makeCondition("question", name)
        cond["question"] = ""
        cond["answer"] = ""
        return cond