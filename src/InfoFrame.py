import game_data as gd
import tkinter as tk
from InfoEditorFactory import InfoEditorFactory
from ObjectSelector import ObjectSelector
from TypeSelector import TypeSelector


class InfoFrame(tk.Frame):
    def __init__(self, parent, obj):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.obj = obj
        self.fields = {}
        self.next_row = 5
        self.makeFields()
        self.makeWidgets()
    
    def makeFields(self):
        for k in self.obj:
            self.fields[k] = tk.StringVar()
            try:
                self.fields[k].set(self.obj[k]['name'])
            except TypeError:
                self.fields[k].set(self.obj[k])
    
    def makeWidgets(self):
        tk.Label(self, text="Type: "+self.obj["type"].upper()).grid(     row=1, columnspan=2, sticky=tk.W)
        self.edit = tk.Button(self, text="Edit Info",
                command=self.edit)
        self.edit.grid(row=1, column=2, sticky=tk.E)
        
        if not gd.is_condition(self.obj):
            self.addLabel("ID", 'id')
        self.addLabel("Name", 'name')
    
    def addLabel(self, label, kind):
        tk.Label(self, text=label + ":").grid(row=self.next_row,
                sticky=tk.W)
        lab = tk.Label(self, textvariable=self.fields[kind])
        lab.grid(row=self.next_row, column=1, columnspan=2,
                sticky=tk.W)
        self.next_row += 5
    
    def addSelector(self, label, kind, obj_type, pick=True):
        tk.Label(self, text=label + ":").grid(row=self.next_row,
                sticky=tk.W)
        lab = tk.Label(self, textvariable=self.fields[kind])
        lab.grid(row=self.next_row, column=1, columnspan=1,
                sticky=tk.W)
        
        if pick:
            callback = lambda : self.edit_selector(kind,
                obj_type)
        else:
            callback = lambda : self.edit_object(kind, obj_type)
            
        tk.Button(self, text="Edit", command=callback).grid(
                row=self.next_row, column=2, sticky=tk.E)
        self.next_row += 5
    
    def addPicker(self, label, kind, select_type):
        tk.Button(self, text="Edit",
                command=lambda:print(select_type)).grid(
                row=self.next_row, column=2, sticky=tk.E)
        self.addLabel(label, kind)
    
    def update(self):
        for k in self.obj:
            if k in self.fields:
                try:
                    self.fields[k].set(self.obj[k]['name'])
                except TypeError:
                    self.fields[k].set(self.obj[k])
    
    def edit(self):
        editor = InfoEditorFactory().make(self, self.obj)
        self.update()
        self.parent.editor.update()

    def edit_selector(self, kind, obj_type):
        if self.obj[kind]:
            self.parent.editor.editNew(self.obj[kind])
        else:
            objects = self.parent.editor.world.getObjects(obj_type)
            try:
                objects.remove(self.obj['owner'])
            except ValueError:
                pass
            except KeyError:
                pass
            
            dialog = ObjectSelector(self, objects)
            result = dialog.getResult()
            if result:
                self.obj[kind] = result
                self.update()
    
    def edit_object(self, field, kind):
        if self.obj[field]:
            self.parent.editor.editNew(self.obj[field])
        else:
            selector = TypeSelector(self, kind)
            obj = selector.getResult()
            if not obj:
                return
            
            editor = InfoEditorFactory().make(self, obj)
            result = editor.getResult()
            if result:
                self.obj[field] = result
                self.update()