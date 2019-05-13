import game_data as gd
import uuid

class GameObjectFactory:

    # Given an entity type return that type of game data object
    def make(self, kind, verb=None):
        if kind in gd.entities:
            return self.makeEntity(kind)
        elif kind is "inform":
            return self.makeInform(kind, verb)
        elif kind is "kill":
            return self.makeKill(verb)
        elif kind is "transfer":
            return self.makeTransfer(verb)
        elif kind is "toggle":
            return self.makeToggle(verb)
        elif kind is "move":
            return self.makeMove(verb)
        elif kind in ["group", "ordered"]:
            return self.makeGroup(kind, verb)
        elif kind is "interaction":
            return self.makeInteraction(verb)
        elif kind is "conditional":
            return self.makeConditional(verb)
        elif kind is "hasItem":
            return self.makeHasItem()
        elif kind is "protected":
            return self.makeProtected()
        elif kind is "question":
            return self.makeQuestion()
        else:
            return None
    
    # Entity ###################################################
    def makeEntity(self, kind):
        return {
            "id": uuid.uuid4(),
            "type": kind,
            "name": "",
            "description": "",
            "events": [],
            "items": [],
            "owner": None,
            "active": 1,
            "obtainable": 1,
            "hidden": 0
        }
    
    # Events ###################################################
    def makeEvent(self, kind, verb=None):
        event = {
            "id": uuid.uuid4(),
            "type": kind,
            "name": "",
            "subjects": [],
            "once": 0,
            "owner": None,
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
        event["other"] = None
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

    def makeInteraction(self, verb=None):
        event = self.makeEvent("interaction", verb)
        event["options"] = {}
        event["breakout"] = 0
        return event
    
    def makeConditional(self, verb=None):
        event = self.makeEvent("conditional", verb)
        event["condition"] = None
        event["success"] = None
        event["failure"] = None
        return event
    
    # Conditions ###############################################
    def makeCondition(self, kind):
        return {"type": kind}
    
    def makeHasItem(self):
        cond = self.makeCondition("hasItem")
        cond["item"] = None
        cond["other"] = None
        return cond
        
    def makeProtected(self):
        cond = self.makeCondition("protected")
        cond["atmosphere"] = ""
        return cond
    
    def makeQuestion(self):
        cond = self.makeCondition("question")
        cond["question"] = ""
        cond["answer"] = ""
        return cond