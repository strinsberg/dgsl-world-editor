import uuid


def make_entity(kind="entity"):
    return {
        "id": uuid.uuid4(),
        "type": "entity",
        "name": "",
        "description": "",
        "events": {},
        "items": [],
    }


def is_container(entity):
    return entity.kind in ["container", "room", "npc", "player"]


def entity_string(entity):
    string = []
    for k, v in entity:
        if k not in ["items", "events"]:
            string.append(k + "=" + v + ";;")
    return str.join("\n", string)