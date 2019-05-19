import tkinter as tk
from EditorFrame import EditorFrame
from MenuBar import MenuBar
from GameObjectFactory import GameObjectFactory


class WorldEditor(tk.Frame):

    def __init__(self, parent, world):
      tk.Frame.__init__(self, parent)
      self.parent = parent
      self.world = world
      self.makeWidgets()
    
    def makeWidgets(self):
        self.parent.title(self.world['title'])
        
        self.editor = EditorFrame(self, self.world['rooms'], 'room', 'Rooms')
        self.menu_bar = MenuBar(self, self.editor, self.world)
        
        self.menu_bar.grid(row=0, sticky="nwe", padx=5, pady=(5,5))
        tk.Grid.columnconfigure(self, 0, weight=1)
        self.editor.grid(row=1, sticky="nswe", padx=2, pady=(0, 2))
        tk.Grid.rowconfigure(self, 1, weight=1)

# Testing ######################################################

if __name__=='__main__':
    root = tk.Tk()
    #root.resizable(0,0)
    root.geometry("546x384")
    
    fact = GameObjectFactory()
    world = {
        'title': 'A Test Adventure',
        'rooms': [fact.make('entity', name='book'),
                fact.make('entity', name='rock')],
    }
    
    frame = WorldEditor(root, world)
    frame.pack_propagate(0)
    frame.pack(fill=tk.BOTH, expand=1)
    
    root.mainloop()