import uuid

# Types ########################################################

entities = [
    "entity", "suit", "container", "room", "npc", "player", "equipment"
]
containers = ["container", "room", "npc", "player"]

events = [
    "give", "take", "toggle active", "toggle obtainable",
    "toggle hidden", "move", "group", "ordered", "interaction", "conditional",
]
group_events = ["group", "ordered", "interaction"]

conditions = ["hasItem", "protected", "question"]

verbs = ["get", "drop", "look", "use", "talk"]
atmospheres = ["oxygen", "radiation", "space"]

# Types for type selectors #####################################

room_entities = ["entity", "equipment", "container", "npc"]

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
