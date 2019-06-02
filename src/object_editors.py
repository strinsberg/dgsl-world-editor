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


class NullEditor(ObjectEditor):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Please select an object to edit").grid(sticky='nwse')
        
        self.obj = {'id': None}
    
    def update(self):
        pass


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
                self.commands.listCommands())
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def makeRightList(self):
        self.right = None
        if gd.is_container(self.obj):
            self.right = ObjectListWithEdit(self.lists,
                    self.obj['items'], "Items", 'entity',
                    self.commands.listCommands())
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
        self.once = InfoCheck(self, "One time", self.obj['once'])
        self.once.grid(row=10, sticky='we')
    
    def makeLeftList(self):
        self.left = ObjectList(self.lists,
                self.obj['subjects'], "Subjects", 'entity',
                self.commands.listCommands(True))
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def makeRightList(self):
        self.right = None
        if gd.is_group(self.obj):
            self.right = ObjectListWithEdit(self.lists,
                    self.obj['events'], "Events", 'event',
                    self.commands.listCommands())
            self.right.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                    expand=1)
    
    def update(self):
        ObjectEditor.update(self)
        self.obj['once'] = self.once.get()
        self.obj['subjects'] = self.left.get()
        if self.right:
            self.obj['events'] = self.right.get()


# Testing ######################################################
if __name__=='__main__':
    from GameObjectFactory import GameObjectFactory
    
    class MockCommand:
        def execute(self, arg):
            print(arg)
    
    class AddCommand:
        def execute(self, arg):
            return {'name': 'A new name', 'id': '3rh2ih3r2foi2'}
            
    # Testing objects
    class MockCommands:
        def __init__(self):
            self.add = AddCommand()
            self.remove = MockCommand()
            self.edit = MockCommand()
            self.select = MockCommand()
        
        def listCommands(self, isSelect=False):
            return{
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
    
    '''
        inform_edit = InformEditor(root, inf, commands)
        inform_edit.grid(row=0, column=1)
        
        kill_edit = KillEditor(root, kill, commands)
        kill_edit.grid(row=1, column=1)
        
        root.mainloop()
        
       
        print(inform_edit.get())
        print(kill_edit.get())
    
    elif group == 2:
        toggle_edit = ToggleEditor(root, toggle, commands)
        toggle_edit.grid(row=0)
        
        transfer_edit = TransferEditor(root, transfer, commands)
        transfer_edit.grid(row=1)
        
        move_edit = MoveEditor(root, move, commands)
        move_edit.grid(row=0, column=1)
        
        group_edit = GroupEditor(root, ordered, commands)
        group_edit.grid(row=1, column=1)
        
        
        root.mainloop()
        
        print(toggle_edit.get())
        print(transfer_edit.get())
        print(move_edit.get())
        print(group_edit.get())
    
    elif group == 3:
        cond_edit = ConditionalEditor(root, conditional, commands)
        cond_edit.grid(row=0)
        
        atmos_edit = ProtectedEditor(root, atmos, commands)
        atmos_edit.grid(row=1)
        
        has_edit = HasItemEditor(root, has, commands)
        has_edit.grid(row=0, column=1)
        
        question_edit = QuestionEditor(root, question, commands)
        question_edit.grid(row=1, column=1)
        
        
        root.mainloop()
        
        print(cond_edit.get())
        print(atmos_edit.get())
        print(has_edit.get())
        print(question_edit.get())
    
        obj = {
        'type':'entity',
        'name': 'Secret of soup',
        'id': '1234-rhfg',
        'description': 'Everything you ever wanted to know',
        'active': 1, 'obtainable': 1, 'hidden': 0,
        'events': [{'name': 'close', 'verb': 'use', 'id': '8d-r'}],
    }
    
    box = {'name': 'box', 'id': 'w-40'}
    cake = {'name': 'cake', 'id': 'r-7u'}
    room = {'name': 'hall', 'id': 'er-89'}
    cond = {'name': 'hasItem', 'id': 'jsdf8'}
    event = {'name': 'event', 'id': '9af0'}
    
    obj2 = {
        'type':'room',
        'name': 'captains room',
        'id': 'he562-osp',
        'description': 'Best room on the ship',
        'active': 1, 'obtainable': 1, 'hidden': 0,
        'events': [{'name': 'enter', 'verb':'enter', 'id': 'r-7u'}],
        'items': [{'name': 'cake', 'id': 'r-7u'}]
    }
    
    fact = GameObjectFactory()
    inf = fact.make('inform')
    kill = fact.make('kill')
    toggle = fact.make('toggle')
    toggle['target'] = box
    transfer = fact.make('transfer')
    transfer['target'] = box
    transfer['item'] = cake
    move = fact.make('move')
    move['destination'] = room
    ordered = fact.make('ordered')
    conditional = fact.make('conditional')
    conditional['condition'] = cond
    conditional['success'] = event
    conditional['failure'] = event
    has = fact.make('hasItem')
    has['item'] = box
    has['other'] = room
    question = fact.make('question')
    atmos = fact.make('protected')
    
    class MockCommand:
        def execute(self, obj_id=None):
            if obj_id in ['event', 'entity'] or obj_id is None:
                return {'name': 'close door', 'id': '7j4y-9du'}
            print(obj_id)
            
    command = MockCommand()
    commands = {'add':command, 'remove':command, 'edit':command,
            'select_entity':command, 'select_event':command,
            'select_room':command, 'select_container':command,
            'select_cond':command}
    '''