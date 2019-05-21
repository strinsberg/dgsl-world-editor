from GameObjectFactory import GameObjectFactory
import json


class GameWorld:

    def __init__(self):
        self.name = "untitled"
        self.rooms = []
        self.player = GameObjectFactory().make('player')
        self.version = 0.0
    
    def getObjects(self, kind):
        if kind == 'room':
            return self.getRooms()
        elif kind == 'entity':
            return self.getEntities()
        elif kind == 'event':
            return self.getEvents()
        else:
            return []
    
    def getRooms(self):
        rooms = []
        rooms.extend(self.rooms)
        return rooms
    
    def getEntities(self):
        return []
    
    def getEvents(self):
        events = []
        for room in self.rooms:
            events.extend(getItemEvents(room))
        return events
        
    def save(self):
        # Problem with this is that any time an object is referenced
        # by another object (excluding containment) we have a
        # circular reference. So owners, destinations, items,
        # subjects will need to be sanitized to just id's when
        # we are working with them.
        # this could be either by storing them as id's and looking
        # for the object when asking to edit (or taking away edit
        # for this type of connection). Or by having a function
        # that goes through and turns the owners etc. into just id's
        # the first sounds easier to me.
        data = {
            "world_name": self.name, "all_rooms": self.rooms,
            "world_player": self.player, "version": self.version,
        }
        with open(self.name + ".world", 'w+') as f:
            f.write(str(data))
        
    
    def load(self, filename):
        with open(filename) as f:
            contents = f.read()
        
        data = json.loads(contents)
        self.name = data['name']
        self.rooms = data['rooms']
        self.player = data['player']
        self.version = data['version']

# helpers
def getItemEvents(item):
    events = []
    for event in item['events']:
        events.extend(getEventEvents(event))
        
    if 'items' in item:
        for obj in item['items']:
            events.extend(getItems(obj))
            
    return events

def getEventEvents(event):
    events = []
    if event:
        events.append(event)
        
        if 'events' in event:
            for obj in event['events']:
                events.extend(getEventEvents(obj))
        elif 'options' in event:
            for option in event['options']:
                events.extend(getEventEvents(option[1]))
        elif event['type'] == 'conditional':
            events.extend(getEventEvents(event['success']))
            events.extend(getEventEvents(event['failure']))
        
    return events