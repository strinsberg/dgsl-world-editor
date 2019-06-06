import tkinter as tk
from GameWorld import GameWorld
from SimpleDialog import *
import os

class MenuBar(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.editor = parent
        self.makeWidgets()
        
    # could set commands to methods so that they can update and
    # set messages etc.
    def makeWidgets(self):
        self.world = tk.Button(self, text="World",
                command=self.editor.editWorld)
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
        dialog = EntryDialog(self, "Enter world name")
        result = dialog.getResult()
        if result:
            world_name = result
        else:
            return
        world = GameWorld()
        world.load(world_name)
        self.editor.loadWorld(world)
        self.setTitle(world.name)
        self.editor.setMessage("Loaded: " + world.name)
    
    def save(self):
        if self.editor.world.name == 'untitled':
            dialog = EntryDialog(self, "Please choose a world name")
            result = dialog.getResult()
            if result:
                self.editor.world.name = result
                self.setTitle(result)
            else:
                return
            
        if (self.editor.world.first_save and
                self.editor.world.filename() in os.listdir()):
            dialog = SimpleDialog(self, "Do you really want to save? \nWorld already exists! Saving will overwrite it. \nThere will be no more Reminders\nCancel and rename world if you don't want this to happen")
            if not dialog.getResult():
                return
                
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