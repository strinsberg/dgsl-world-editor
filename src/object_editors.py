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
                self.obj['events'], "Events",
                self.commands['add'], self.commands['remove'],
                self.commands['edit'])
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def makeRightList(self):
        self.right = None
        if gd.is_container(self.obj):
            self.right = ObjectListWithEdit(self.lists,
                    self.obj['items'], "Items",
                    self.commands['add'], self.commands['remove'],
                    self.commands['edit'])
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
                self.obj['subjects'], "Subjects",
                self.commands['select_event'],
                self.commands['remove'])
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y,
                expand=1)
    
    def makeRightList(self):
        self.right = None
        if gd.is_group(self.obj):
            self.right = ObjectListWithEdit(self.lists,
                    self.obj['events'], "Events",
                    self.commands['add'], self.commands['remove'],
                    self.commands['edit'])
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
                self.obj['target'],
                self.commands['select_container'])
        self.target.grid(row=5, sticky='we')
    
    def update(self):
        EventEditor.update(self)
        self.obj['target'] = self.target.get()
        
        
class TransferEditor(ToggleEditor):
    
    def makeWidgets(self):
        ToggleEditor.makeWidgets(self)
        self.item = InfoSelector(self, "Item",
                self.obj['item'], self.commands['select_entity'])
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
                self.obj['destination'],
                self.commands['select_room'])
        self.dest.grid(row=5, sticky='we')
    
    def update(self):
        EventEditor.update(self)
        self.obj['destination'] = self.dest.get()
        

class GroupEditor(EventEditor):
    
    def makeWidgets(self):
        EventEditor.makeWidgets(self)
        self.repeats = InfoCheck(self, "Repeats",
                self.obj['repeats'])
        self.repeats.grid(row=5, sticky='we')

    def update(self):
        EventEditor.update(self)
        self.obj['repeats'] = self.repeats.get()


class ConditionalEditor(EventEditor):
    
    def makeWidgets(self):
        EventEditor.makeWidgets(self)
        self.cond = InfoSelector(self, "Condition",
                self.obj['condition'], self.commands['select_cond'])
        self.cond.grid(row=5, sticky='we')
        
        self.succ = InfoSelector(self, "Success",
                self.obj['success'], self.commands['select_event'])
        self.succ.grid(row=6, sticky='we')
        
        self.fail = InfoSelector(self, "Failure",
                self.obj['failure'], self.commands['select_event'])
        self.fail.grid(row=7, sticky='we')
    
    def update(self):
        EventEditor.update(self)
        self.obj['condition'] = self.cond.get()
        self.obj['success'] = self.succ.get()
        self.obj['failure'] = self.fail.get()
    

class HasItemEditor(ObjectEditor):
    
    def __init__(self, parent, obj, commands):
        self.commands = commands
        ObjectEditor.__init__(self, parent, obj)
    
    def makeWidgets(self):
        ObjectEditor.makeWidgets(self)
        self.item = InfoSelector(self, "Item",
                self.obj['item'], self.commands['select_entity'])
        self.item.grid(row=5, sticky='we')
        self.other = InfoSelector(self, "Other",
                self.obj['other'],self.commands['select_container'])
        self.other.grid(row=6, sticky='we')

    def update(self):
        ObjectEditor.update(self)
        self.obj['item'] = self.item.get()
        self.obj['other'] = self.other.get()


class QuestionEditor(ObjectEditor):
    
    def __init__(self, parent, obj, commands):
        self.commands = commands
        ObjectEditor.__init__(self, parent, obj)
    
    def makeWidgets(self):
        ObjectEditor.makeWidgets(self)
        self.question = InfoEntry(self, "Question",
                self.obj['question'])
        self.question.grid(row=5, sticky='we')
        self.answer = InfoEntry(self, "Answer",
                self.obj['answer'])
        self.answer.grid(row=6, sticky='we')

    def update(self):
        ObjectEditor.update(self)
        self.obj['question'] = self.question.get()
        self.obj['answer'] = self.answer.get()
        
        
class ProtectedEditor(ObjectEditor):
    
    def __init__(self, parent, obj, commands):
        self.commands = commands
        ObjectEditor.__init__(self, parent, obj)
    
    def makeWidgets(self):
        ObjectEditor.makeWidgets(self)
        self.atmos = InfoOption(self, "Atmosphere",
                self.obj['atmosphere'], gd.atmospheres)
        self.atmos.grid(row=5, sticky='we')

    def update(self):
        ObjectEditor.update(self)
        self.obj['atmosphere'] = self.atmos.get()


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
            if obj_id:
                print(obj_id)
            else:
                return{'name': 'Book',
                        'id': '113244-sjfk', 'verb': 'read'}
    command = MockCommand()
    commands = {'add':command, 'remove':command, 'edit':command,
            'select_entity':command, 'select_event':command,
            'select_room':command, 'select_container':command,
            'select_cond':command}
    
    # Create and run widgets
    root = tk.Tk()
    
    group = 3
    
    if group == 1:
        ent_edit = EntityEditor(root, obj, commands)
        ent_edit.grid(row=0, sticky='w')
        
        room_edit = EntityEditor(root, obj2, commands)
        room_edit.grid(row=1, sticky='w')
        
        inform_edit = InformEditor(root, inf, commands)
        inform_edit.grid(row=0, column=1)
        
        kill_edit = KillEditor(root, kill, commands)
        kill_edit.grid(row=1, column=1)
        
        root.mainloop()
        
        # Test widgets get methods
        print(ent_edit.get())
        print(room_edit.get())
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