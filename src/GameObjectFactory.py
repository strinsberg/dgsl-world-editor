class GameDataFactory:
    def __init__(self):
        self.entity_types = ["entity", "room", "container", "room",
                "npc", "player", "suit"]

    # Given an entity type return that type of game data object
    def make(self, kind, verb=None):
        if kind in self.entity_types:
            return self.make_entity(kind)
        elif kind is "inform":
            return self.make_inform(kind, verb)
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
            "owner": None
        }
    
    # Events ###################################################
    def makeEvent(self, kind, verb=None):
        event = {
            "id": uuid.uuid4(),
            "type": kind,
            "name": "",
            "subjects": [],
            "once": False,
            "owner": None,
        }
        if verb:
            event["verb"] = verb
        return event

    def makeInform(self, kind, verb=None):
        event = make_event(kind, verb)
        event["message"] = ""
        return event
    
    def makeKill(self, verb=None):
        event = make_inform("kill", verb)
        event["ending"] = False
        return event
    
    def makeTransfer(self, verb=None):
        event = make_event("transfer", verb)
        event["other"] = None
        event["toTarget"] = False
        event["item"] = None
        return event
    
    def makeToggle(self, verb=None):
        event = make_event("toggle", verb)
        event["target"] = None
        return event
    
    def makeMove_player(self, verb=None):
        event = make_event("move", verb)
        event["destination"] = None
        return event
    
    # Group Events #############################################
    def makeGroup(kind, verb=None):
        event = make_event(kind, verb)
        event["events"] = [],
        event["repeats"] = False,
        return event

    def makeInteraction(verb=None):
        event = make_event("interaction", verb)
        event["options"] = {}
        event["breakout"] = False
        return event
    
    def makeConditional(verb=None):
        event = make_event("conditional", verb)
        event["condition"] = None
        event["success"] = None
        event["failure"] = None
        return event
    
    # Conditions ###############################################
    def makeCondition(self, kind):
        return {"type": kind}
    
    def makeHas_item(self):
        cond = makeCondition("hasItem")
        cond["itemId"] = ""
        cond["other"] = None
        return cond
        
    def makeProtected(self):
        cond = makeCondition("protected")
        cond["atmosphere"] = ""
        return cond
    
    def makeQuestion(self):
        cond = makeCondition("question")
        cond["question"] = ""
        cond["answer"] = ""
        return cond