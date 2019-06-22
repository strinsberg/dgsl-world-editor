import tkinter as tk


# Widget list of objects that allows adding and removing
class ObjectList(tk.Frame):
    def __init__(self, parent, objects, title, kind, commands):
        tk.Frame.__init__(self, parent)
        self.objects = []
        self.objects.extend(objects)
        self.objects.sort(key=lambda obj: obj['name'])
        self.title = title
        self.kind = kind
        self.commands = commands
        self.makeWidgets()
        self.update()

    def makeWidgets(self):
        tk.Label(self, text=self.title).grid(row=0)

        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=5, sticky='ns')
        tk.Grid.rowconfigure(self, 5, weight=1)

        buttons = tk.Frame(self)
        buttons.grid(row=10)
        self.makeButtons(buttons)

    def makeButtons(self, buttons):
        tk.Button(buttons, text='Add', command=self.add).grid(row=5, column=5)
        tk.Button(buttons, text='Remove', command=self.remove).grid(row=5,
                                                                    column=10)

    def update(self, objects=None):
        if objects:
            self.objects = []
            self.objects.extend(objects)

        self.listbox.delete(0, tk.END)
        for obj in self.objects:
            text = obj['name']
            if 'verb' in obj:
                text += " (" + obj['verb'] + ")"
            self.listbox.insert(tk.END, text)

    def add(self):
        obj = self.commands['add'].execute(self.kind)
        if obj:
            self.objects.append(self.trimObj(obj))
            self.update()

    def remove(self):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            obj = self.objects.pop(idx)
            self.commands['remove'].execute(obj['id'])
            self.update()

    def get(self):
        return self.objects

    def trimObj(self, obj):
        o = {'name': obj['name'], 'id': obj['id']}
        if 'verb' in obj:
            o['verb'] = obj['verb']
        return o


# Widget list of objects that allows editing
class ObjectListWithEdit(ObjectList):
    def makeButtons(self, buttons):
        ObjectList.makeButtons(self, buttons)
        tk.Button(buttons, text='Edit', command=self.edit).grid(row=5)

    def edit(self):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            obj = self.objects[idx]
            self.commands['edit'].execute(obj['id'])


class ObjectListFactory:
    def make(self, parent, objs, title, kind, commands, isEdit=False):
        objects = self.makeObjects(objs)
        if isEdit:
            return ObjectListWithEdit(parent, objects, title, kind, commands)
        else:
            return ObjectList(parent, objects, title, kind, commands)

    def makeObjects(self, objs):
        objects = []
        for obj in objs:
            o = {"id": obj['id'], "name": obj['name']}
            if 'verb' in obj:
                o['verb'] = obj['verb']
            objects.append(o)
        return objects


'''
# Testing ######################################################
if __name__ == '__main__':
    from . import game_object_factory as gof

    # Test objects
    class MockCommand:
        def execute(self, arg):
            print(arg)

    class MockAdd:
        def execute(self, arg):
            return {'name': 'A new name', 'id': '3rh2ih3r2foi2'}

    command = MockCommand()
    commands = {'add': MockAdd(), 'remove': command, 'edit': command}

    close = {'name': 'close door', 'verb': 'use'}
    enter = {'name': 'enter room', 'verb': 'enter'}
    pizza = {'name': 'pizza'}
    fork = {'name': 'fork'}
    book = {'name': 'secrets of soup'}

    fact = gof.GameObjectFactory()
    events = [fact.make('inform', close), fact.make('kill', enter)]
    edit_objs = [
        fact.make('entity', pizza),
        fact.make('entity', fork),
        fact.make('entity', book)
    ]

    # Create and run widgets
    root = tk.Tk()

    obj_list = ObjectListFactory().make(root, events, 'Subjects', 'event',
                                        commands)
    obj_list.pack()

    obj_edit = ObjectListFactory().make(root, edit_objs, 'Items', 'entity',
                                        commands, True)
    obj_edit.pack()

    root.mainloop()

    # Test get
    print()
    print(obj_list.get())
    print(obj_edit.get())

'''
