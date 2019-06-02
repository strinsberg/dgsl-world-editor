from GameObjectFactory import GameObjectFactory
import json
import os


class GameWorld:

    def __init__(self):
        self.name = "untitled"
        self.welcome = "fun is waiting!"
        self.version = 0.0
        self.objects = {}
        player = GameObjectFactory().make('player')
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
            isType = gd.is_container(kind)
        else:
            isType = lambda x: False
            
        for field in self.objects:
            obj = self.objects[field]
            if obj['type'] == kind or isType(kind):
                objects.append(obj)
                
        return objects
        
    def save(self):
        filename = self.name + ".world"
        '''
        if self.first_save:
            if filename in os.listdir():
                # Replace with a dialog. Cancel will return.
                print("World with that name exists")
            self.first_save = False
        '''
        #hack
        #self.objects.pop(None)
        data = {
            "name": self.name,
            "welcome": self.welcome,
            "version": self.version,
            "player": self.player,
            "objects": self.objects,
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f)
        
    
    def load(self, filename):
        with open(filename) as f:
            data = json.load(f)
        
        self.name = data['name']
        self.welcome = data['welcome']
        self.version = data['version']
        self.player = data['player']
        self.objects = data['objects']
        
        self.first_save = False
        
    def removeAll(self, obj):
        self.objects.pop(obj['id'])
        if 'items' in obj:
            for i in obj['items']:
                self.removeAll(i)
        if 'events' in obj:
            for e in obj['events']:
                self.removeAll(e)