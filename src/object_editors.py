import tkinter as tk
import game_data as gd
from info_widgets import *
from object_lists import *


class ObjectEditor(tk.Frame):
    
    def __init__(self, parent, obj):
        tk.Frame.__init__(self, parent)
        self.obj = {}
        self.obj.update(obj)
        self.makeWidgets()
        self.makeLists()
        
    def makeWidgets(self):
        tk.Grid.columnconfigure(self, 0, weight=1)
        InfoLabel(self, "Type", self.obj['type']).grid(row=0,
                sticky='w')
        self.name = InfoEntry(self, "Name", self.obj['name'])
        self.name.grid(row=1, sticky='we')
    
    def makeLists(self):
        self.lists = tk.Frame(self)
        self.lists.grid(row = 25, sticky='ns')
        tk.Grid.rowconfigure(self.lists, 0, weight=1)
        self.makeLeftList()
        self.makeRightList()
    
    def makeLeftList(self):
        pass
    
    def makeRightList(self):
        pass
    
    def update(self):
        self.obj['name'] = self.name.get()
    
    def get(self):
        self.update()
        return self.obj
    
    def validate(self, obj):
        self.update()
        if self.obj['id'] == obj['id']:
            return False
        return True


class NullEditor(ObjectEditor):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Please select an object to edit").grid(sticky='nwse')
        
        self.obj = {'id': None}
    
    def update(self):
        pass

class PlayerEditor(ObjectEditor):
    def __init__(self, parent, obj, commands):
        self.commands = commands
        ObjectEditor.__init__(self, parent, obj)
    
    def makeWidgets(self):
        tk.Grid.columnconfigure(self, 0, weight=1)
        InfoLabel(self, "Type", self.obj['type']).grid(row=0,
                sticky='w')
        self.desc = InfoEntry(self, "Description",
                self.obj['description'])
        self.desc.grid(row=5, sticky='we')
        self.start = InfoSelector(self, "Starting Room",
                self.obj['start'], 'room',
                self.commands.makeSelect(self.validate),
                self.commands.edit)
        self.start.grid(row=6, sticky='we')
    
    def makeLeftList(self):
        self.left = ObjectListWithEdit(self.lists,
                self.obj['items'], "Items", 'entity',
                self.commands.addList())
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def update(self):
        self.obj['description'] = self.desc.get()
        self.obj['start'] = self.start.get()
        self.obj['items'] = self.left.get()
    

class EntityEditor(ObjectEditor):
    
    def __init__(self, parent, obj, commands):
        self.commands = commands
        ObjectEditor.__init__(self, parent, obj)
    
    def makeWidgets(self):
        ObjectEditor.makeWidgets(self)
        self.desc = InfoEntry(self, "Description",
                self.obj['description'])
        self.desc.grid(row=5, sticky='we')
        
        if self.obj['type'] != 'room':
            self.makeStates()
        
    def makeStates(self):
        self.states = tk.Frame(self)
        self.states.grid(row=15, sticky='we')
        
        self.act = InfoCheck(self.states, "Active",
                self.obj['active'])
        self.act.pack(side=tk.LEFT, anchor='w', fill=tk.X, expand=1)
        self.obt = InfoCheck(self.states, "Obtainable",
                self.obj['obtainable'])
        self.obt.pack(side=tk.LEFT, anchor='w', fill=tk.X, expand=1)
        self.hid = InfoCheck(self.states, "Hidden",
                self.obj['hidden'])
        self.hid.pack(side=tk.LEFT, anchor='w', fill=tk.X, expand=1)
    
    def makeLeftList(self):
        self.left = ObjectListWithEdit(self.lists,
                self.obj['events'], "Events", 'event',
                self.commands.addList())
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def makeRightList(self):
        self.right = None
        if gd.is_container(self.obj):
            self.right = ObjectListWithEdit(self.lists,
                    self.obj['items'], "Items", 'entity',
                    self.commands.addList())
            self.right.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                    expand=1)
    
    def update(self):
        ObjectEditor.update(self)
        self.obj['description'] = self.desc.get()
        if self.obj['type'] != 'room':
            self.obj['active'] = self.act.get()
            self.obj['obtainable'] = self.obt.get()
            self.obj['hidden'] = self.hid.get()
        self.obj['events'] = self.left.get()
        if self.right:
            self.obj['items'] = self.right.get()
          
            
class EventEditor(ObjectEditor):
    
    def __init__(self, parent, obj, commands):
        self.commands = commands
        ObjectEditor.__init__(self, parent, obj)
    
    def makeWidgets(self):
        ObjectEditor.makeWidgets(self)
        if self.obj['verb'] is not None:
            self.verb = InfoEntry(self, "Verb",
                    self.obj['verb'])
            self.verb.grid(row=2, sticky='we')
        self.once = InfoCheck(self, "One time", self.obj['once'])
        self.once.grid(row=10, sticky='we')
    
    def makeLeftList(self):
        self.left = ObjectList(self.lists,
                self.obj['subjects'], "Subjects", 'event',
                self.commands.selectList(self.validate))
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def select(self, obj):
        self.update()
        if self.obj['id'] == obj['id']:
            return False
        return True

        
    def validate(self, obj):
        if not self.select(obj):
            return False
        
         # What this really needs to do is make subjects
        # into a graph and check for cycles. If the addition
        # of an object will create a cycle then it is invalid
        # unfortunately it would also have to check conditional
        # success and failure. Will turn into a real affair
        for o in self.obj['subjects']:
            if o['id'] == obj['id']:
                return False
        for o in obj['subjects']:
            if o['id'] == self.obj['subjects']:
                return False
        return True
    
    def makeRightList(self):
        self.right = None
        if gd.is_group(self.obj):
            self.right = ObjectListWithEdit(self.lists,
                    self.obj['events'], "Events", 'event',
                    self.commands.addList())
            self.right.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                    expand=1)
    
    def update(self):
        ObjectEditor.update(self)
        self.obj['once'] = self.once.get()
        self.obj['subjects'] = self.left.get()
        if self.right:
            self.obj['events'] = self.right.get()

class WorldEditor(tk.Frame):
    
    def __init__(self, parent, obj, commands):
        tk.Frame.__init__(self, parent)
        self.obj = obj
        self.commands = commands
        self.makeWidgets()
    
    def makeWidgets(self):
        self.name = InfoEntry(self, "Name", self.obj.name)
        self.name.grid(row=0)
        self.welcome = InfoEntry(self, "Welcome", self.obj.welcome)
        self.welcome.grid(row=2)
        self.version = InfoEntry(self, "Version", self.obj.version)
        self.version.grid(row=4)
    
    def update(self):
        self.obj.name = self.name.get()
        self.obj.welcome = self.welcome.get()
        self.obj.version = self.version.get()
    
    def get(self):
        return {'id':None}
    

# Testing ######################################################
if __name__=='__main__':
    from GameObjectFactory import GameObjectFactory
    
    # Testing objects
    class MockCommand:
        def execute(self, arg):
            print(arg)
    
    class AddCommand:
        def execute(self, arg):
            return {'name': 'A new name', 'id': '3rh2ih3r2foi2'}
            
    class MockCommands:
        def __init__(self):
            self.add = AddCommand()
            self.remove = MockCommand()
            self.edit = MockCommand()
            self.select = MockCommand()
        
        def addList(self, isSelect=False):
            return{
                'add': self.add,
                'remove': self.remove,
                'edit': self.edit,
            }
    
        def makeSelect(self, obj, validate=None):
            return self.add
        
        def selectList(self, obj, validate=None):
            return {
                'add': self.add,
                'remove': self.remove,
                'edit': self.edit,
            }
    
    commands = MockCommands()
    
    pizza = {'name': 'pizza'}
    room = {'name': 'captains room'}
    event = {'name': 'enter', 'verb': 'enter'}
    
    fact = GameObjectFactory()
    obj = fact.make('entity', pizza)
    obj2 = fact.make('room', room)
    obj3 = fact.make('inform', event)
    obj4 = fact.make('group', event)
    
    
    # Create and run widgets
    root = tk.Tk()
    
    ent_edit = EntityEditor(root, obj, commands)
    ent_edit.grid(row=0, sticky='w')
    
    room_edit = EntityEditor(root, obj2, commands)
    room_edit.grid(row=1, sticky='w')
    
    event_edit = EventEditor(root, obj3, commands)
    event_edit.grid(row=1, column=1)
    
    group_edit = EventEditor(root, obj4, commands)
    group_edit.grid(row=0, column=1)

    root.mainloop()

    # Test widgets get methods
    print(ent_edit.get())
    print(room_edit.get())
    print(event_edit.get())
    print(group_edit.get())