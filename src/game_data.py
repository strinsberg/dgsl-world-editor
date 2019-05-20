import uuid

# Types ########################################################

entities = ["entity", "door", "suit", "container", "room",
        "npc", "player"]
containers = ["container", "room", "npc", "player"]

events = ["inform", "kill", "transfer", "toggle",
        "move", "group", "interaction", "conditional"]
group_events = ["group", "ordered"]

conditions = ["hasItem", "protected", "question"]

verbs = ["get", "drop", "look", "use", "talk"]
atmospheres = ["oxygen", "radiation", "space"]


# Types for type selectors #####################################

room_entities = ["entity", "door", "suit", "container", "npc"]


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

def get_base_type(obj):
    if is_entity(obj):
        return "entity"
    elif is_event(obj):
        return "event"
    else:
        return "condition"