import tkinter as tk
from TypeSelector import TypeSelector


class ObjectList(tk.Frame):
    def __init__(self, parent, editor, objects, obj_type, title):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.editor = editor
        self.objects = objects
        self.obj_type = obj_type
        self.title = title
        self.button_text = {
            "edit": "Edit", "add": "Add", "del": "Remove"
        }
        self.makeWidgets()
        
    def makeWidgets(self):
        self.title_text = tk.StringVar()
        self.title_text.set(self.title)
        tk.Label(self, textvariable=self.title_text).grid(row=10)
        
        self.listbox = tk.Listbox(self)
        tk.Grid.rowconfigure(self, 15, weight=1)
        self.listbox.grid(row=15, sticky= tk.N + tk.S)
        self.update()
        
        self.makeButtons()
        
    def makeButtons(self):
        self.buttons = tk.Frame(self)
        
        self.edit_button = tk.Button(self.buttons,
                text=self.button_text['edit'], command=self.edit)
        self.edit_button.grid(row=1)
        
        self.add_button = tk.Button(self.buttons,
                text=self.button_text['add'], command=self.add)
        self.add_button.grid(row=1, column=1)
        
        self.remove_button = tk.Button(self.buttons,
                text=self.button_text['del'], command=self.remove)
        self.remove_button.grid(row=1, column=2)
        
        self.buttons.grid(row=20, sticky=tk.W)
    
    def update(self):
        self.listbox.delete(0, tk.END)
        for obj in self.objects:
            self.listbox.insert(tk.END, obj["name"])
    
    def edit(self, event=None):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            try:
                self.editor.editNew(self.objects[idx])
            except AttributeError:
                pass
        #self.update()
    
    def add(self, event=None):
        dialog = TypeSelector(self, self.obj_type)
        result = dialog.getResult()
        if result:
            self.objects.append(result)
            self.update()
    
    def remove(self, event=None):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            self.objects.pop(idx)
        self.update()


# move to its own file eventually
from GameObjectFactory import GameObjectFactory
from InfoEditorFactory import InfoEditorFactory

class RoomList(ObjectList):
    def __init__(self, parent, editor):
        ObjectList.__init__(self, parent, editor, editor.world.rooms, 'room', 'Rooms')
    
    def add(self, event=None):
        obj = GameObjectFactory().make('room')
        editor = InfoEditorFactory().make(self, obj)
        self.objects.append(obj)
        self.update()


# move to its own file eventually
from ObjectSelector import ObjectSelector
from SimpleDialog import SimpleDialog

class SubjectList(ObjectList):
    def __init__(self, parent, editor, objects):
        ObjectList.__init__(self, parent, editor, objects, 'event', 'Subjects')
    
    def add(self):
        events = self.editor.world.getEvents()
        # would it be better to pass in a list to be excluded???
        events.remove(self.parent.obj)
        
        if len(events) == 0:
            SimpleDialog(self, "There are no events to subscibe to")
            return
        
        for obj in self.objects:
            events.remove(obj)
        dialog = ObjectSelector(self, events)
        result = dialog.getResult()
        
        if result:
            self.objects.append(result)
            self.update()