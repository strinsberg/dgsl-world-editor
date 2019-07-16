import tkinter as tk
from . import game_data as gd
from . import info_widgets
from . import object_lists


class ObjectEditor(tk.Frame):
    def __init__(self, parent, obj):
        tk.Frame.__init__(self, parent)
        self.obj = {}
        self.obj.update(obj)
        self.makeWidgets()
        self.makeLists()

    def makeWidgets(self):
        tk.Grid.columnconfigure(self, 0, weight=1)
        info_widgets.InfoLabel(self, "Type", self.obj['type']).grid(row=0,
                                                                    sticky='w')
        self.name = info_widgets.InfoEntry(self, "Name", self.obj['name'])
        self.name.grid(row=1, sticky='we')

    def makeLists(self):
        self.lists = tk.Frame(self)
        self.lists.grid(row=25, sticky='ns')
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
        tk.Label(self,
                 text="Please select an object to edit").grid(sticky='nwse')

        self.obj = {'id': None}

    def update(self):
        pass


class PlayerEditor(ObjectEditor):
    def __init__(self, parent, obj, commands):
        self.commands = commands
        ObjectEditor.__init__(self, parent, obj)

    def makeWidgets(self):
        tk.Grid.columnconfigure(self, 0, weight=1)
        info_widgets.InfoLabel(self, "Type", self.obj['type']).grid(row=0,
                                                                    sticky='w')
        self.desc = info_widgets.InfoEntry(self, "Description",
                                           self.obj['description'])
        self.desc.grid(row=5, sticky='we')
        self.start = info_widgets.InfoSelector(
            self, "Starting Room", self.obj['start'], 'room',
            self.commands.makeSelect(self.validate), self.commands.edit)
        self.start.grid(row=6, sticky='we')

    def makeLeftList(self):
        self.left = object_lists.ObjectListWithEdit(self.lists,
                                                    self.obj['items'], "Items",
                                                    'entity',
                                                    self.commands.addList())
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=1)

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
        self.desc = info_widgets.InfoEntry(self, "Description",
                                           self.obj['description'])
        self.desc.grid(row=5, sticky='we')

        if self.obj['type'] != 'room':
            self.makeStates()

    def makeStates(self):
        self.states = tk.Frame(self)
        self.states.grid(row=15, sticky='we')

        self.act = info_widgets.InfoCheck(self.states, "Active",
                                          self.obj['active'])
        self.act.pack(side=tk.LEFT, anchor='w', fill=tk.X, expand=1)
        self.obt = info_widgets.InfoCheck(self.states, "Obtainable",
                                          self.obj['obtainable'])
        self.obt.pack(side=tk.LEFT, anchor='w', fill=tk.X, expand=1)
        self.hid = info_widgets.InfoCheck(self.states, "Hidden",
                                          self.obj['hidden'])
        self.hid.pack(side=tk.LEFT, anchor='w', fill=tk.X, expand=1)

    def makeLeftList(self):
        self.left = object_lists.ObjectListWithEdit(self.lists,
                                                    self.obj['events'],
                                                    "Events", 'event',
                                                    self.commands.addList())
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=1)

    def makeRightList(self):
        self.right = None
        if gd.is_container(self.obj):
            self.right = object_lists.ObjectListWithEdit(
                self.lists, self.obj['items'], "Items", 'entity',
                self.commands.addList())
            self.right.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=1)

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


class EquipmentEditor(EntityEditor):
    def makeWidgets(self):
        super(EquipmentEditor, self).makeWidgets()

        eff = 'enter effects as space separated list'
        if self.obj['protects']:
            eff = " ".join(self.obj['protects'])
        self.protects = info_widgets.InfoEntry(self, "Protects", eff)
        self.protects.grid(row=20, sticky='we')

        self.slot = info_widgets.InfoEntry(self, "Slot", self.obj['slot'])
        self.slot.grid(row=21, sticky='we')

        self.must_equip = info_widgets.InfoCheck(
            self, 'Must Be Equipped', self.obj['must_equip'])

    def update(self):
        super(EquipmentEditor, self).update()
        self.obj['protects'] = self.protects.get().split()
        self.obj['slot'] = self.slot.get()
        self.obj['must_equip'] = self.must_equip.get()


class EventEditor(ObjectEditor):
    def __init__(self, parent, obj, commands):
        self.commands = commands
        ObjectEditor.__init__(self, parent, obj)

    def makeWidgets(self):
        ObjectEditor.makeWidgets(self)
        if self.obj['verb'] is not None:
            self.verb = info_widgets.InfoEntry(self, "Verb", self.obj['verb'])
            self.verb.grid(row=2, sticky='we')
        self.once = info_widgets.InfoCheck(self, "One time", self.obj['once'])
        self.once.grid(row=10, sticky='we')

    def makeLeftList(self):
        self.left = object_lists.ObjectList(
            self.lists, self.obj['subjects'], "Subjects", 'event',
            self.commands.selectList(self.validate))
        self.left.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=1)

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
            self.right = object_lists.ObjectListWithEdit(
                self.lists, self.obj['events'], "Events", 'event',
                self.commands.addList())
            self.right.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=1)

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
        self.name = info_widgets.InfoEntry(self, "Name", self.obj.name)
        self.name.grid(row=0)
        self.welcome = info_widgets.InfoEntry(self, "Welcome",
                                              self.obj.welcome)
        self.welcome.grid(row=2)
        self.version = info_widgets.InfoEntry(self, "Version",
                                              self.obj.version)
        self.version.grid(row=4)

    def update(self):
        self.obj.name = self.name.get()
        self.obj.welcome = self.welcome.get()
        self.obj.version = self.version.get()

    def get(self):
        return {'id': None}
