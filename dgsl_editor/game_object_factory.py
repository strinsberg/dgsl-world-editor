from . import game_data as gd
import uuid


class GameObjectFactory:

    # Given an entity type return that type of game data object
    def make(self, kind, obj=None):
        if kind == 'player':
            newObj = self.makePlayer()
        elif kind == 'room':
            newObj = self.makeRoom(kind)
        elif kind == 'equipment':
            newObj = self.makeEquipment(kind)
        elif kind in gd.entities:
            newObj = self.makeEntity(kind)
        elif kind == "toggle active":
            newObj = self.makeToggleActive()
        elif kind == "toggle obtainable":
            newObj = self.makeToggleObtainable()
        elif kind == "toggle hidden":
            newObj = self.makeToggleHidden()
        elif kind == 'give':
            newObj = self.makeGive()
        elif kind == 'take':
            newObj = self.makeTake()
        elif kind == "move":
            newObj = self.makeMove()
        elif kind in ["group", "ordered"]:
            newObj = self.makeGroup(kind)
        elif kind == "interaction":
            newObj = self.makeInteraction()
        elif kind == "conditional":
            newObj = self.makeConditional()
        elif kind == "hasItem":
            newObj = self.makeHasItem()
        elif kind == "protected":
            newObj = self.makeProtected()
        elif kind == "question":
            newObj = self.makeQuestion()
        elif kind == 'option':
            newObj = self.makeStandardOption()
        elif kind == 'conditional option':
            newObj = self.makeConditionalOption()
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

    def makeEquipment(self, kind):
        equip = self.makeEntity(kind)
        equip['protects'] = []
        equip['slot'] = 'generic',
        equip['must_equip'] = 1
        return equip

    # Events ###################################################
    def makeEvent(self, kind):
        event = {
            "id": str(uuid.uuid4()),
            "type": kind,
            "name": "",
            "verb": None,
            "subjects": [],
            "once": 0,
            "message": ''
        }
        return event

    def makeTransfer(self, kind):
        event = self.makeEvent(kind)
        event['item'] = None
        return event

    def makeGive(self):
        event = self.makeTransfer('give')
        event['item_owner'] = None
        return event

    def makeTake(self):
        event = self.makeTransfer('take')
        event['new_owner'] = None
        return event

    def makeToggle(self):
        event = self.makeEvent("toggle")
        event["target"] = None
        return event

    def makeToggleActive(self):
        event = self.makeEvent("toggle_active")
        event["target"] = None
        event['state'] = 'Active'
        return event

    def makeToggleObtainable(self):
        event = self.makeEvent("toggle_obtainable")
        event["target"] = None
        event['state'] = 'Obtainable'
        return event

    def makeToggleHidden(self):
        event = self.makeEvent("toggle_hidden")
        event["target"] = None
        event['state'] = 'Hidden'
        return event

    def makeMove(self):
        event = self.makeEvent("move")
        event["destination"] = None
        event['name'] = 'unamed move'
        return event

    # Group Events #############################################
    def makeGroup(self, kind):
        event = self.makeEvent(kind)
        event["events"] = []
        event["repeats"] = 0  # dont need
        return event

    def makeConditional(self):
        event = self.makeEvent("conditional")
        event["condition"] = None
        event["success"] = None
        event["failure"] = None
        return event

    def makeInteraction(self):
        event = self.makeEvent("interaction")
        event["options"] = []
        event['breakout'] = 0
        return event

    # Options ##################################################
    def makeOption(self, kind):
        return {
            'name': '',
            'text': '',
            'event': None,
            'type': kind,
            'id': str(uuid.uuid4()),
        }

    def makeStandardOption(self):
        return self.makeOption("option")

    def makeConditionalOption(self):
        opt = self.makeOption('conditional_option')
        opt['condition'] = None
        return opt

    # Conditions ###############################################
    def makeCondition(self, kind):
        return {
            "type": kind,
            'name': '',
            "id": str(uuid.uuid4()),
        }

    def makeHasItem(self):
        cond = self.makeCondition("hasItem")
        cond["item"] = None
        cond["other"] = None  # dont need
        return cond

    def makeProtected(self):
        cond = self.makeCondition("protected")
        cond["atmosphere"] = 'oxygen'  # dont need
        cond['effects'] = []
        return cond

    def makeQuestion(self):
        cond = self.makeCondition("question")
        cond["question"] = ""
        cond["answer"] = ""
        return cond
