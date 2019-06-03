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
        
        self.title = tk.StringVar()
        self.title.set(self.editor.world.name)
        self.title_bar = tk.Label(self, textvariable=self.title)
        self.title_bar.pack(side=tk.LEFT, expand=1, fill=tk.X)
        
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
        self.setTitle(world.name)
        self.editor.setMessage("Loaded: " + filename)
    
    def save(self):
        # Do something to let them know it succeeded
        self.editor.update()
        self.editor.world.save()
        self.setTitle(self.editor.world.name)
        self.editor.setMessage("Saved")
    
    def setTitle(self, title):
        self.title.set(title)
    
    def editing(self):
        self.setTitle("** " + self.editor.world.name + " **")
    
       
    


# Testing ######################################################

if __name__=='__main__':
    root = tk.Tk()
    
    frame = MenuBar(root, {})
    frame.pack()
    
    root.mainloop()