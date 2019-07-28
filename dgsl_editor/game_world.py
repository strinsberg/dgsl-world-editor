from . import game_object_factory
from . import game_data as gd
import json
import os


class GameWorld:
    def __init__(self):
        self.name = "untitled"
        self.welcome = "fun is waiting!"
        self.version = "0.0"
        self.objects = {}
        player = game_object_factory.GameObjectFactory().make('player')
        self.addObject(player)
        self.player = player['id']
        self.first_save = True

    def addObject(self, obj):
        self.objects[obj['id']] = obj

    def removeObject(self, obj_id):
        obj = self.objects[obj_id]
        self.removeAll(obj)

    def getObject(self, obj_id):
        return self.objects[obj_id]

    def updateObject(self, obj):
        if obj['id'] in self.objects:
            self.objects[obj['id']].update(obj)
        elif obj is not None:
            self.addObject(obj)

    def hasObject(self, obj_id):
        return obj_id in self.objects

    def getObjects(self, kind):
        objects = []

        if kind == 'container':
            def isType(x): return x in gd.containers
        elif kind == 'event':
            def isType(x): return x in gd.events
        elif kind == 'entity':
            def isType(x): return x in gd.entities
        else:
            def isType(x): return False

        for ID in self.objects:
            obj = self.objects[ID]
            if obj['type'] == kind or isType(obj['type']):
                objects.append(obj)

        return objects

    def changeName(self, name):
        self.name = name
        self.first_save = True

    def save(self):
        data = {
            "name": self.name,
            "welcome": self.welcome,
            "version": self.version,
            "player": self.player,
            "objects": self.objects,
        }

        with open(self.filepath(), 'w') as f:
            json.dump(data, f, indent=2, sort_keys=True)

        self.first_save = False

    def load(self, world_name):
        self.name = world_name
        with open(self.filepath()) as f:
            data = json.load(f)

        self.name = data['name']
        self.welcome = data['welcome']
        self.version = data['version']
        self.player = data['player']
        self.objects = data['objects']

        self.first_save = True

    def removeAll(self, obj):
        self.objects.pop(obj['id'])
        if 'items' in obj:
            for i in obj['items']:
                self.removeAll(i)
        if 'events' in obj:
            for e in obj['events']:
                self.removeAll(e)

    def filepath(self):
        home = os.path.expanduser('~')
        return os.path.join(home, ".dgsl", "worlds", self.filename())

    def filename(self):
        name = self.name.replace(' ', '_') + '.world'
        return name.lower()
