import tkinter as tk
from GameWorld import GameWorld

class MenuBar(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.editor = parent
        self.makeWidgets()
        
    def makeWidgets(self):
        self.world = tk.Button(self, text="World",
                command=lambda: print('world'))
        self.world.pack(side=tk.LEFT)
        
        self.player = tk.Button(self, text="Player",
                command=lambda :
                self.editor.editNew(self.editor.world.player))
        self.player.pack(side=tk.LEFT)
        
        self.back = tk.Button(self, text="Back", command=lambda: self.editor.editLast())
        self.back.pack(side=tk.LEFT)
        
        self.load = tk.Button(self, text="Load", command=self.load)
        self.load.pack(side=tk.RIGHT)
        
        self.save = tk.Button(self, text="Save", command=self.save)
        self.save.pack(side=tk.RIGHT)
    
    def load(self):
        # need to get them to select a world name
        filename = "untitled.world"
        world = GameWorld()
        world.load(filename)
        self.editor.loadWorld(world)
    
    def save(self):
        # Do something to let them know it succeeded
        self.editor.update()
        self.editor.world.save()
    
       
    


# Testing ######################################################

if __name__=='__main__':
    root = tk.Tk()
    
    frame = MenuBar(root, {})
    frame.pack()
    
    root.mainloop()