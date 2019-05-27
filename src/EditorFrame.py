import tkinter as tk
from ObjectViewerFactory import ObjectViewer, ObjectViewerFactory
from ObjectList import ObjectList, RoomList
from GameObjectFactory import GameObjectFactory
from MenuBar import MenuBar
from GameWorld import GameWorld


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
        
        self.list = RoomList(self.body, self)
        self.list.grid(row=0, column=0, sticky='nsw')
        
        fact = ObjectViewerFactory()
        self.viewer = fact.make(self.body, self)
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
        fact = ObjectViewerFactory()
        new = fact.make(self.body, self, obj)
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
    rooms = [fact.make('room', name='captains room'),
            fact.make('room', name='common room')]
    
    world = GameWorld()
    world.rooms = rooms
    
    obj = rooms[0]
    
    frame = EditorFrame(root, world)
    frame.pack_propagate(0)
    frame.pack(fill=tk.BOTH, expand=1)
    
    root.mainloop()