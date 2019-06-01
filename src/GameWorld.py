from GameObjectFactory import GameObjectFactory
import json


class GameWorld:

    def __init__(self):
        self.name = "untitled"
        self.welcome = "fun is waiting!"
        self.version = 0.0
        self.player = GameObjectFactory().make('player')
        self.objects = {}
        self.first_save = True
    
    def addObject(self, obj):
        self.objects[obj['id']] = obj
    
    def removeObject(self, obj_id):
        self.objects.pop(obj_id)
    
    def getObject(self, obj_id):
        return self.objects['obj_id']
    
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
        if self.first_save:
            if filename in os.listdir():
                # Replace with a dialog. Cancel will return.
                print("World with that name exists")
            self.first_save = False
            
        data = {
            "name": self.name,
            "welcome": self.welcome,
            "version": self.version,
            "player": self.player,
            "object": self.objects,
        }
        
        with open(self.name + ".world", 'w') as f:
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
        