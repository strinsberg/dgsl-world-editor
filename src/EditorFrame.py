import tkinter as tk
from ObjectViewer import ObjectViewer
from ObjectList import ObjectList
from GameObjectFactory import GameObjectFactory


class EditorFrame(tk.Frame):
    
    def __init__(self, parent, objects, kind, title, obj=None):
        tk.Frame.__init__(self, parent, bd=4, relief=tk.GROOVE)
        self.list = ObjectList(self, self, objects, kind, title)
        self.viewer = ObjectViewer(self, obj)
        self.history = []
        self.makeWidgets()
    
    def makeWidgets(self):
        self.list.grid(row=0, column=1, sticky='nsw')
        self.viewer.grid(row=0, column=2)
        
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)
        
    def editNew(self, obj):
        self.history.append(self.viewer.obj)
        self.newViewer(obj)
    
    def editLast(self):
        if len(self.history) > 0:
            obj = self.history.pop()
            self.newViewer(obj)
    
    def newViewer(self, obj):
        #print(obj)
        new = ObjectViewer(self, obj)
        #print(new)
        self.viewer.destroy()
        self.viewer = new
        self.viewer.grid(row=0, column=2)
        
# Testing ######################################################

if __name__=='__main__':
    root = tk.Tk()
    root.resizable(False, False)
    
    fact = GameObjectFactory()
    rooms = [fact.make('entity', name='book'),
            fact.make('entity', name='rock')]
    
    obj = rooms[0]
    
    frame = EditorFrame(root, rooms, 'entity', 'items', obj)
    frame.pack()
    
    root.mainloop()