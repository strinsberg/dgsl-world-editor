import uuid

"""
There will need to be some kind of error eventually to
make sure that all objects have necessary values. This could
just be a check when you try to export the file as a data file
for use with the text adventure game. Then it could also
eventually include some warnings or flags for unfinished
objects to make it easier for you to see that you've left them
undone. Or even maybe once there is a program it will make sure
that they are set by forcing you to set them at least once.

Write unit tests using your new unit testing framework.

Work on getting some really basic gui going to start thinking
about good ways to set up the world builder.
"""

# World ###########################################################

class World:
    def __init__(self, name):
        self.name = name
        self.filename = name.replace(" ", "_") + ".world"
        self.player = None
        self.rooms = []
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def to_string(self):
        rep = []
        for room in self.rooms:
            rep.append(all_str(room))
        return str.join("\n", rep)
    
    def __str__(self):
        return self.to_string()

# recursively print a room and its items/events
def all_str(room):
    rep = []
    rep.append(str(room))
    for item in room.items:
        if isinstance(item, Container):
            rep.append(all_str(item))
        else:
            rep.append(str(item))
        for event in item.events:
            rep.append(event_str(event))
    return str.join("\n", rep)

# recursively print an event and its events
def event_str(event):
    rep = []
    rep.append(str(event))
    if isinstance(event, Group):
        for ev in event.events:
            rep.append(event_str(event))
    elif isinstance(event, Conditional):
        rep.append(str(event.cond))
        rep.append(event_str(event.success))
        rep.append(event_str(event.failure))
    elif isinstance(event, Interaction):
        for op in event.options:
            rep.append(event_str(op))
    return str.join("\n", rep)


# Entities ########################################################

class Entity:
    def __init__(self):
        self.kind = "entity"
        self.id = uuid.uuid4()
        self.name = ""
        self.desc = ""
        self.act = True
        self.obt = True
        self.hid = False
        self.here = None
        self.events = []
    
    def add_event(self, event):
        event.owner = self
        if event.owner_type == "":
            event.owner_type = "hidden" + uuid.uuid4().hex
        self.events.append(event)

    def obt_string(self):
        if not self.obt:
            return "obtainable={};".format(self.obt)
        return ""
        
    def to_string(self):
        rep = []
        rep.append("type={};".format(self.kind))
        rep.append("id={};".format(self.id.hex))
        rep.append("name={};".format(self.name))
        rep.append("description={};".format(self.desc))
        if self.here:
            rep.append("here={};".format(self.here.id.hex))
        if not self.act:
            rep.append("active={};".format(self.act))
        if self.hid:
            rep.append("hidden={};".format(self.hid))
        state = self.obt_string()
        if state != "":
            rep.append(state)
        return str.join("\n", rep)
    
    def __str__(self):
        return "{{\n{}\n}}".format(self.to_string())


class Container(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.kind = "container"
        self.items = []
    
    def add_entity(self, entity):
        entity.here = self
        self.items.append(entity)
    
class Room(Container):
    def __init__(self):
        Container.__init__(self)
        self.kind = "room"
        self.obt = False
    
    def obt_string(self):
        return ""


class Door(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.kind = "door"
        self.there = None
        self.obt = False

    def obt_string(self):
        if self.obt:
            return "obtainable={};".format(self.obt)
        return ""

    def to_string(self):
        return "{}\nthere={};".format(Entity.to_string(self), self.there.id)


class Npc(Container):
    def __init__(self):
        Container.__init__(self)
        self.kind = "npc"
        self.obt = False

    def obt_string(self):
        if self.obt:
            return "obtainable={};".format(self.obt)
        return ""

# Single events ##################################################

class Event:
    def __init__(self):
        self.id = uuid.uuid4()
        self.once = False
        self.owner = None  # event or entity
        self.owner_type = ""  # verb or parent event type
        self.option_text = ""
        self.condition = ""
        self.subject = None
        self.observers = []
    
    def subscribe(self, event):
        event.subject = self
        self.observers.append(event)
    
    def to_string(self):
        rep = []
        rep.append("type={};".format(self.kind))
        rep.append("id={};".format(self.id.hex))
        if self.owner and isinstance(self.owner, Entity):
            own = "entity={};"
            own_type = "verb={};"
        else:
            own = "event={};"
            own_type = "ownertype={};"
        rep.append(own.format(self.owner.id.hex))
        rep.append(own_type.format(self.owner_type))
        if self.once:
            rep.append("once={};".format(self.once))
        if self.subject:
            rep.append("subject={};".format(self.subject.id.hex))
        return str.join("\n", rep)
    
    def __str__(self):
        return "{{\n{}\n}}".format(self.to_string())


class Inform(Event):
    def __init__(self):
        Event.__init__(self)
        self.kind = "inform"
        self.message = ""
    
    def to_string(self):
        return "{}\nmessage={};".format(Event.to_string(self),
                                        self.message)


class Kill(Inform):
    def __init__(self):
        Inform.__init__(self)
        self.kind = "kill"
        self.ending = False
        
    def to_string(self):
        if self.ending:
            return "{}\nending={};".format(Event.to_string(self),
                                           self.ending)
        else:
            return Inform.to_string(self)

class Toggle(Event):
    def __init__(self):
        Event.__init__(self)
        self.kind = "toggle"
        self.target = None
    
    def to_string(self):
        return "{}\ntarget={};".format(Event.to_string(self),
                                        self.target.id.hex)


class Transfer(Event):
    def __init__(self):
        Event.__init__(self)
        self.kind = "transfer"
        self.other = None
        self.item = None
        self.to_target = False

    def to_string(self):
        return "{}\nitemid={};\ntotarget={};\nother={};".format(
                    Event.to_string(self),
                    self.item.id.hex, self.to_target,
                    self.other.id.hex)

class MovePlayer(Event):
    def __init__(self):
        Event.__init__(self)
        self.kind = "move"
        self.door = None
    
    # Should take a destination rather than a door
    def to_string(self):
        return "{}\ndoor={};".format(Event.to_string(self),
                                        self.door.id.hex)


class EquipSuit(Event):
    def __init__(self):
        Event.__init__(self)
        self.kind = "equipsuit"
        self.suit = None
    
    def to_string(self):
        return "{}\nsuit={};".format(Event.to_string(self),
                                        self.suit.id.hex)

# Composite events ##############################################

class Group(Event):
    def __init__(self):
        Event.__init__(self)
        self.kind = "group"
        self.events = []
    
    def add_event(self, event):
        event.owner = self
        event.owner_type = self.kind
        events.append(event)


class Structured(Group):
    def __init__(self):
        Event.__init__(self)
        self.kind = "structured"
        self.repeats = True
    
    def to_string(self):
        return "{}\nrepeats={};".format(Event.to_string(self),
                                        self.repeats)

class Conditional(Event):
    def __init__(self):
        Event.__init__(self)
        self.kind = "conditionalevent"
        self.cond = None
        self.success = None
        self.failure = None
    
    def set_cond(self, condition):
        condition.event = self
        self.cond = condition
    
    def set_success(self, success):
        success.owner = self
        success.condition = "success"
        success.owner_type = self.kind
        self.success = success
    
    def set_failure(self, failure):
        failure.owner = self
        failure.condition = "failure"
        failure.owner_type = self.kind
        self.failure = failure


class Interaction(Group):
    def __init__(self):
        Event.__init__(self)
        self.kind = "interaction"
        self.breakout = False
        
    def to_string(self):
        return "{}\nbreakout={};".format(Event.to_string(self),
                                        self.breakout)


# Conditions ####################################################

class Condition:
    def __init__(self):
        self.kind = "condition"
        self.sub_type = ""
        self.event = None

    def to_string(self):
        return "type={};\nsubtype={};\nevent={};".format(
                    self.kind, self.sub_type,
                    self.event.id.hex)
    
    def __str__(self):
        return "{{\n{}\n}}".format(self.to_string())


class HasItem(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.sub_type = "hasitem"
        self.item = None
        self.other = None

    def to_string(self):
        return "{}\nitemid={};\nother={};".format(
                    Condition.to_string(self),
                    self.item.id.hex, self.other.id.hex)


class Protected(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.sub_type = "protected"
        self.atmos = ""


class Question(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.sub_type = "question"
        self.question = ""
        self.answer = ""

    def to_string(self):
        return "{}\nquestion={};\nanswer={};".format(
                    Condition.to_string(self),
                    self.question, self.answer)

# Main ##########################################################

if __name__=='__main__':
    # create some test objects
    room = Room()
    room.name = "Captain's room"
    room.desc = "The best room on the ship!"
    
    rmcom = Room()
    rmcom.name = "Common room"
    rmcom.desc = "A place to relax with your crew."
    
    door = Door()
    door.name = "Common room door"
    door.desc = "A door to the common room."
    door.there = rmcom
    room.add_entity(door)
    
    box = Container()
    box.name = "Metal box"
    box.desc = "A shiny metal container."
    room.add_entity(box)
    
    item = Entity()
    item.name = "Gold watch"
    item.desc = "This looks expensive!"
    box.add_entity(item)
    
    npc = Npc()
    npc.name = "Joey Temporary"
    npc.desc = "This guy."
    room.add_entity(npc)
    
    inform = Inform()
    inform.message = "Give me all your money."
    inform.owner_type = "talk"
    npc.add_event(inform)
    
    kill = Kill()
    kill.message = "poison sprays from the dials into your eyes."
    kill.owner_type = "use"
    item.add_event(kill)
    
    kill2 = Kill()
    kill2.message = "you choke on it. duh."
    kill2.owner_type = "eat"
    kill2.ending = True
    item.add_event(kill2)
    
    move = MovePlayer()
    
    equip = EquipSuit()
    
    toggle = Toggle()
    
    group = Group()
    
    structured = Structured()
    
    interaction = Interaction()
    
    cond_event = Conditional()
    cond_event.owner_type = "open"
    box.add_event(cond_event)
    
    has = HasItem()
    has.item = item
    has.other = box
    cond_event.set_cond(has)
    
    inform2 = Inform()
    inform2.message = "There is a nice watch for you."
    cond_event.set_success(inform2)
    
    inform3 = Inform()
    inform3.message = "Can't you do anything right?"
    cond_event.set_failure(inform3)
    
    transfer = Transfer()
    transfer.item = item
    transfer.to_target = True
    transfer.other = box
    box.add_event(transfer)
    inform2.subscribe(transfer)


    
    question = Question()
    
    protect = Protected()
    
    
    
    # test print
    print(room)
    print(rmcom)
    print(door)
    print(box)
    print(item)
    print(npc)
    print(inform)
    print(kill)
    print(kill2)
    print(cond_event)
    print(has)
    print(inform2)
    print(inform3)
    print(transfer)