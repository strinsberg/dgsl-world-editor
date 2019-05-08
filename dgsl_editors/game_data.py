import uuid

# Entity #######################################################

def make_entity(kind="entity"):
    return {
        "id": uuid.uuid4(),
        "type": kind,
        "name": "",
        "description": "",
        "events": [],
        "items": [],
        "owner": None
    }

def is_container(entity):
    return entity.kind in ["container", "room", "npc", "player"]

def export_entity(entity):
    pass

# Event ########################################################

def make_event(kind, verb=None):
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

def make_inform(kind="inform", verb=None):
    event = make_event(kind, verb)
    event["message"] = ""
    return event

def make_kill(verb=None):
    event = make_inform("kill", verb)
    event["ending"] = False
    return event

def make_transfer(verb=None):
    event = make_event("transfer", verb)
    event["other"] = None
    event["toTarget"] = False
    event["item"] = None
    return event

def make_toggle(verb=None):
    event = make_event("toggle", verb)
    event["target"] = None
    return event

def make_move_player(verb=None):
    event = make_event("move", verb)
    event["destination"] = None
    return event

def export_event(event):
    pass

# Group event ##################################################

def make_group(kind="group", verb=None):
    event = make_event(kind, verb)
    event["events"] = [],
    event["repeats"] = False,
    return event

def make_interaction(verb=None):
    event = make_event("interaction", verb)
    event["options"] = {}
    event["breakout"] = False
    return event

def make_cond_event(verb=None):
    event = make_event("conditional", verb)
    event["condition"] = None
    event["success"] = None
    event["failure"] = None
    return event

def export_group_event(event):
    pass

# Condition ####################################################

def make_condition(subtype):
    return {
        "subtype": subtype,
    }

def make_has_item():
    cond = make_condition("hasItem")
    cond["itemId"] = ""
    cond["other"] = None
    return cond
    
def make_protected():
    cond = make_condition("protected")
    cond["atmosphere"] = ""
    return cond

def make_question():
    cond = make_condition("question")
    cond["question"] = ""
    cond["answer"] = ""
    return cond

def export_cond(cond):
    pass