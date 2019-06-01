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
        self.makeWidgets()
    
    def makeWidgets(self):
        self.menu = MenuBar(self)
        self.menu.grid(row=0, sticky="nwe", padx=5, pady=(5,5))
        tk.Grid.columnconfigure(self, 0, weight=1)
        
        self.body = tk.Frame(self, bd=4, relief=tk.GROOVE)
        self.body.grid(row=1, sticky="nswe", padx=2, pady=(0, 2))
        tk.Grid.rowconfigure(self, 1, weight=1)
        
        self.list = ObjectListWithEdit(self.body,
                self.world.getObjects('room'), "Rooms", 'room',
                {'add': com.AddObj(self, 'entity'),
                'edit': com.EditObj(),
                'remove': com.RemoveObj()})
        self.list.grid(row=0, column=0, sticky='nsw')
        
        self.viewer = ObjectEditorFactory.make(self.body)
        self.viewer.grid(row=0, column=1)
        
        tk.Grid.rowconfigure(self.body, 0, weight=1)
        tk.Grid.columnconfigure(self.body, 1, weight=1)
        
    def editNew(self, obj):
        self.history.append(self.viewer.obj)
        self.newViewer(obj)
    
    def editLast(self):
        if len(self.history) > 0:
            obj = self.history.pop()
            self.newViewer(obj)
    
    def newViewer(self, obj):
        #print(obj)
        new = tk.Label(self.body, text="nothing here!")
        #print(new)
        self.viewer.finish()
        self.viewer.destroy()
        self.viewer = new
        self.viewer.grid(row=0, column=1)
    
    def update(self):
        self.list.update()


# Testing ######################################################

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("555x384")
    
    fact = GameObjectFactory()
    room = fact.make('room', name='captains room')
    
    world = GameWorld()
    world.addObject(room)
    
    frame = EditorFrame(root, world)
    frame.pack_propagate(0)
    frame.pack(fill=tk.BOTH, expand=1)
    
    root.mainloop()