from GameObjectFactory import GameObjectFactory

class GameWorld:

    def __init__(self):
        self.name = "untitled"
        self.rooms = []
        self.player = GameObjectFactory().make('player')
    
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
        # put everything here to save the world with it's filename
        # etc. Make sure that the world is converted to a dict
        # so that it can be saved and loaded with json
        pass
    
    def load(self, filename):
        pass

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