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


class EntityEditor(ObjectEditor):
    
    def __init__(self, parent, obj, add, remove, edit):
        self.add_command = add
        self.remove_command = remove
        self.edit_command = edit
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
                self.obj['events'], "Events",
                self.add_command, self.remove_command,
                self.edit_command)
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def makeRightList(self):
        self.right = None
        if gd.is_container(self.obj):
            self.right = ObjectListWithEdit(self.lists,
                    self.obj['items'], "Items",
                    self.add_command, self.remove_command,
                    self.edit_command)
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
    
    def __init__(self, parent, obj, add, remove, edit):
        self.add_command = add
        self.remove_command = remove
        self.edit_command = edit
        ObjectEditor.__init__(self, parent, obj)
    
    def makeWidgets(self):
        ObjectEditor.makeWidgets(self)
        self.once = InfoCheck(self, "One time", self.obj['once'])
        self.once.grid(row=10, sticky='we')
    
    def makeLeftList(self):
        self.left = ObjectList(self.lists,
                self.obj['subjects'], "Subjects",
                self.add_command, self.remove_command)
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def makeRightList(self):
        self.right = None
        if gd.is_group(self.obj):
            self.right = ObjectListWithEdit(self.lists,
                    self.obj['events'], "Events",
                    self.add_command, self.remove_command,
                    self.edit_command)
            self.right.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                    expand=1)
    
    def update(self):
        ObjectEditor.update(self)
        self.obj['once'] = self.once.get()
        self.obj['subjects'] = self.left.get()
        if self.right:
            self.obj['events'] = self.right.get()

class InformEditor(EventEditor):
    
    def makeWidgets(self):
        EventEditor.makeWidgets(self)
        self.message = InfoEntry(self, "Message",
                self.obj['message'])
        self.message.grid(row=5, sticky='we')
    
    def update(self):
        EventEditor.update(self)
        self.obj['message'] = self.message.get()
    
class KillEditor(InformEditor):
    
    def makeWidgets(self):
        InformEditor.makeWidgets(self)
        self.ending = InfoCheck(self, "Ending", self.obj['ending'])
        self.ending.grid(row=11, sticky='we')
    
    def update(self):
        InformEditor.update(self)
        self.obj['ending'] = self.ending.get()


class ToggleEditor(EventEditor):
    
    def makeWidgets(self):
        EventEditor.makeWidgets(self)
        self.target = InfoSelector(self, "Target",
                self.obj['target'], self.add_command)
        self.target.grid(row=5, sticky='we')
    
    def update(self):
        EventEditor.update(self)
        self.obj['target'] = self.target.get()
        
        
class TransferEditor(ToggleEditor):
    
    def makeWidgets(self):
        ToggleEditor.makeWidgets(self)
        self.item = InfoSelector(self, "Item",
                self.obj['item'], self.add_command)
        self.item.grid(row=6, sticky='we')
        self.to_target = InfoCheck(self, "To target",
                self.obj['toTarget'])
        self.to_target.grid(row=11, sticky='we')
        
    def update(self):
        ToggleEditor.update(self)
        self.obj['item'] = self.item.get()
        self.obj['toTarget'] = self.to_target.get()


class MoveEditor(EventEditor):
    
    def makeWidgets(self):
        EventEditor.makeWidgets(self)
        self.dest = InfoSelector(self, "Destination",
                self.obj['destination'], self.add_command)
        self.dest.grid(row=5, sticky='we')
    
    def update(self):
        EventEditor.update(self)
        self.obj['destination'] = self.dest.get()
        
# Testing ######################################################
if __name__=='__main__':
    from GameObjectFactory import GameObjectFactory
    # Testing objects
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
    
    class MockCommand:
        def execute(self, obj_id=None):
            if obj_id:
                print(obj_id)
            else:
                return{'name': 'Book',
                        'id': '113244-sjfk', 'verb': 'read'}
    command = MockCommand()
    
    # Create and run widgets
    root = tk.Tk()
    
    group = 2
    
    if group == 1:
        ent_edit = EntityEditor(root, obj, command, command,command)
        ent_edit.grid(row=0, sticky='w')
        
        room_edit = EntityEditor(root, obj2, command, command, command)
        room_edit.grid(row=1, sticky='w')
        
        inform_edit = InformEditor(root, inf, command, command, command)
        inform_edit.grid(row=0, column=1)
        
        kill_edit = KillEditor(root, kill, command, command, command)
        kill_edit.grid(row=1, column=1)
        
        root.mainloop()
        
        # Test widgets get methods
        print(ent_edit.get())
        print(room_edit.get())
        print(inform_edit.get())
        print(kill_edit.get())
    
    elif group == 2:
        toggle_edit = ToggleEditor(root, toggle, command,
                command, command)
        toggle_edit.grid(row=0)
        
        transfer_edit = TransferEditor(root, transfer, command,
                command, command)
        transfer_edit.grid(row=1)
        
        move_edit = MoveEditor(root, move, command,
                command, command)
        move_edit.grid(row=0, column=1)
        
        
        root.mainloop()
        
        print(toggle_edit.get())
        print(transfer_edit.get())
        print(move_edit.get())
        