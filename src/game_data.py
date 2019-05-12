import uuid

# Entity #######################################################

def is_container(entity):
    return entity["type"] in ["container", "room", "npc", "player"]


# Event ########################################################

def is_event(obj):
    return obj["type"] in [
            "event", "inform", "kill", "transfer",
            "toggle", "move", "group", "interaction",
            "conditional"]

# Group event ##################################################

def is_group(obj):
    return obj["type"] in ["group", "ordered", "interaction",
            "conditional"]

# Condition ####################################################

def is_condition(obj):
    return obj["type"] in ["hasItem", "protected", "question"]