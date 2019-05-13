import uuid

# Types ########################################################

entities = ["entity", "door", "suit", "container", "room",
        "npc", "player"]
containers = ["container", "room", "npc", "player"]

events = ["inform", "kill", "transfer", "toggle",
        "move", "group", "interaction", "conditional"]
group_events = ["group", "ordered", "interaction", "conditional"]

conditions = ["hasItem", "protected", "question"]

verbs = ["get", "drop", "look", "use", "talk"]
atmospheres = ["oxygen", "radiation", "space"]


# Type checkers ################################################

def is_entity(obj):
    return obj["type"] in entities

def is_container(obj):
    return obj["type"] in containers

def is_event(obj):
    return obj["type"] in events

def is_group(obj):
    return obj["type"] in group_events

def is_condition(obj):
    return obj["type"] in conditions

