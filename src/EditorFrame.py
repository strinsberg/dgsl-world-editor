import tkinter as tk
from ObjectViewer import ObjectViewer
from ObjectList import ObjectList
from GameObjectFactory import GameObjectFactory


class EditorFrame(tk.Frame):
    
    def __init__(self, parent, objects, kind, title, obj=None):
        tk.Frame.__init__(self, parent)
        self.list = ObjectList(self, self, objects, kind, title)
        self.viewer = ObjectViewer(self, obj)
        self.history = []
        self.makeWidgets()
    
    def makeWidgets(self):
        self.list.pack(side=tk.LEFT, fill=tk.Y, expand=1)
        self.viewer.pack(side=tk.RIGHT)
        
    def editNew(self, obj):
        self.history.append(self.viewer.obj)
        self.newViewer(obj)
    
    def editLast(self):
        obj = self.history.pop()
        self.newViewer(obj)
    
    def newViewer(self, obj):
        new = ObjectViewer(self, obj)
        self.viewer.destroy()
        self.viewer = new
        self.viewer.pack(side=tk.RIGHT)
        
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