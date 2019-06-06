import tkinter as tk
from object_lists import *
from object_editors import *
from ObjectEditorFactory import ObjectEditorFactory
from GameObjectFactory import GameObjectFactory
from MenuBar import MenuBar
from GameWorld import GameWorld
import commands as com


class EditorFrame(tk.Frame):
    
    def __init__(self, parent, world):
        tk.Frame.__init__(self, parent)
        self.world = world
        self.history = []
        self.commands = com.Commands(self)
        self.makeWidgets()
    
    def makeWidgets(self):
        self.menu = MenuBar(self)
        self.menu.grid(row=0, sticky="nwe", padx=5, pady=(5,5))
        tk.Grid.columnconfigure(self, 0, weight=1)
        
        self.makeBody()
        
        self.message = tk.StringVar()
        self.message.set("  ")
        self.message_bar = tk.Label(self, textvariable=self.message)
        self.message_bar.grid(row=2, sticky='w', padx=5)
        
    def makeBody(self):
        self.body = tk.Frame(self, bd=4, relief=tk.GROOVE)
        self.body.grid(row=1, sticky="nswe", padx=2, pady=(0, 2))
        tk.Grid.rowconfigure(self, 1, weight=1)
        
        self.list = ObjectListWithEdit(self.body,
                self.world.getObjects('room'), "Rooms", 'room',
                self.commands.addList())
        self.list.grid(row=0, column=0, sticky='nsw')
        
        self.obj_editor = ObjectEditorFactory().make(self.body)
        self.obj_editor.grid(row=0, column=1)
        
        tk.Grid.rowconfigure(self.body, 0, weight=1)
        tk.Grid.columnconfigure(self.body, 1, weight=1)
        
    def editNew(self, obj_id):
        try:
            self.history.append(self.obj_editor.obj['id'])
        except TypeError:
            pass
        self.newObjEditor(self.world.getObject(obj_id))
    
    def editLast(self):
        while len(self.history) > 0:
            obj_id = self.history.pop()
            # could add something to skip if obj is the same
            if self.world.hasObject(obj_id) or obj_id is None:
                obj = self.world.getObject(obj_id) if obj_id else None
                self.newObjEditor(obj)
                break
                
    
    def newObjEditor(self, obj):
        self.update()
        self.objectUpdate(obj)
        new = ObjectEditorFactory().make(self.body, obj,
                self.commands)
        self.obj_editor.destroy()
        self.obj_editor = new
        self.obj_editor.grid(row=0, column=1)
    
    def editWorld(self):
        self.history.append(self.obj_editor.obj['id'])
        self.update()
        new = WorldEditor(self.body, self.world, self.commands)
        self.obj_editor.destroy()
        self.obj_editor = new
        self.obj_editor.grid(row=0, column=1)
    
    def update(self):
        self.list.update()
        self.obj_editor.update()
        old_obj = self.obj_editor.get()
        if old_obj['id'] is not None:
            self.world.updateObject(old_obj)
    
    def loadWorld(self, world):
        self.world = world
        self.history = []
        self.body.destroy()
        self.makeBody()
    
    def setMessage(self, message):
        self.message.set(message)
    
    def clearMessage(self):
        self.message.set("   ")
    
    def objectUpdate(self, obj):
        for field in obj:
            try:
                o = obj[field]
                actual = self.world.getObject(o['id'])
                o['name'] = actual['name']
                if 'verb' in o:
                    o['verb'] = actual['verb']

            except TypeError:
                try:
                    for e in obj[field]:
                        actual = self.world.getObject(e['id'])
                        e['name'] = actual['name']
                        if 'verb' in e:
                            e['verb'] = actual['verb']
                except TypeError:
                    pass
                    


# Testing ######################################################

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("555x400")
    
    fact = GameObjectFactory()
    room = fact.make('room', {'name': 'captains room'})
    
    world = GameWorld()
    world.addObject(room)
    
    frame = EditorFrame(root, world)
    frame.pack_propagate(0)
    frame.pack(fill=tk.BOTH, expand=1)
    
    root.mainloop()