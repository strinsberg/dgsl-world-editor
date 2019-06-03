import game_data as gd
import uuid


class GameObjectFactory:

    # Given an entity type return that type of game data object
    def make(self, kind, obj=None):
        if kind == 'player':
             newObj = self.makePlayer()
        elif kind == 'room':
            newObj = self.makeRoom(kind)
        elif kind == 'door':
            newObj = self.makeDoor(kind)
        elif kind in gd.entities:
            newObj = self.makeEntity(kind)
        elif kind == "inform":
            newObj = self.makeInform(kind)
        elif kind == "kill":
            newObj = self.makeKill()
        elif kind == "transfer":
            newObj = self.makeTransfer()
        elif kind == "toggle":
            newObj = self.makeToggle()
        elif kind == "move":
            newObj = self.makeMove()
        elif kind in ["group", "ordered", "interaction"]:
            newObj = self.makeGroup(kind)
        elif kind == "conditional":
            newObj = self.makeConditional()
        elif kind == "hasItem":
            newObj = self.makeHasItem()
        elif kind == "protected":
            newObj = self.makeProtected()
        elif kind == "question":
            newObj = self.makeQuestion()
        else:
            assert False, "Object factory has no type: " + kind
        
        if obj:
            newObj.update(obj)
        return newObj
    
    # Player ###################################################
    
    def makePlayer(self):
        return {
            "id": "player",
            "type": "player",
            "name": "player",
            "description": "",
            "items": [],
            "start": None,
        }
    
    # Entity ###################################################
    def makeEntity(self, kind):
        return {
            "id": str(uuid.uuid4()),
            "type": kind,
            "name": '',
            "description": "",
            "events": [],
            "items": [],
            "active": 1,
            "obtainable": 1,
            "hidden": 0
        }
        # need to make some kind of alteration to accomadate
        # other types of entities. Like rooms have default states
    
    def makeRoom(self, kind):
        room = self.makeEntity(kind)
        room['obtainable'] = 0
        return room
        
    
    # Events ###################################################
    def makeEvent(self, kind):
        event = {
            "id": str(uuid.uuid4()),
            "type": kind,
            "name": "",
            "subjects": [],
            "once": 0,
        }
        return event

    def makeInform(self, kind):
        event = self.makeEvent(kind)
        event["message"] = ""
        return event
    
    def makeKill(self):
        event = self.makeInform("kill")
        event["ending"] = 0
        return event
    
    def makeTransfer(self):
        event = self.makeEvent("transfer")
        event["target"] = None
        event["toTarget"] = 0
        event["item"] = None
        return event
    
    def makeToggle(self):
        event = self.makeEvent("toggle")
        event["target"] = None
        return event
    
    def makeMove(self):
        event = self.makeEvent("move")
        event["destination"] = None
        return event
    
    # Group Events #############################################
    def makeGroup(self, kind):
        event = self.makeEvent(kind)
        event["events"] = []
        event["repeats"] = 0
        return event
    
    def makeConditional(self):
        event = self.makeEvent("conditional")
        event["condition"] = None
        event["success"] = None
        event["failure"] = None
        return event
    
    # Conditions ###############################################
    def makeCondition(self, kind):
        return {"type": kind, 'name': '', "id": str(uuid.uuid4()),}
    
    def makeHasItem(self):
        cond = self.makeCondition("hasItem")
        cond["item"] = None
        cond["other"] = None
        return cond
        
    def makeProtected(self):
        cond = self.makeCondition("protected")
        cond["atmosphere"] = 'oxygen'
        return cond
    
    def makeQuestion(self):
        cond = self.makeCondition("question")
        cond["question"] = ""
        cond["answer"] = ""
        return cond