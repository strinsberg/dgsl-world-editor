import tkinter as tk
from SimpleDialog import SimpleDialog
from GameObjectFactory import GameObjectFactory
import game_data as gd

class TypeSelector(SimpleDialog):
    def __init__(self, parent, kind):
        self.kind = kind
        SimpleDialog.__init__(self, parent)
        
    def makeWidgets(self, master):
        tk.Label(master, text = self.kind + " Type:").grid(row=0, sticky=tk.W)
        self.choice = tk.StringVar(master)
        
        if self.kind is "entity":
            self.choice.set(gd.entities[0])
            self.menu = tk.OptionMenu(
                    *((master, self.choice) + tuple(gd.entities)))
        if self.kind is "event":
            self.choice.set(gd.events[0])
            self.menu = tk.OptionMenu(
                    *((master, self.choice) + tuple(gd.events)))
        else:
            self.choice.set(gd.conditions[0])
            self.menu = tk.OptionMenu(
                    *((master, self.choice) + tuple(gd.conditions)))
        
        self.menu.grid(row=0, column=1)
        
        tk.Label(master, text="Name:").grid(row=5)
        self.name = tk.Entry(master)
        self.name.grid(row=5, column=1)
    
    def apply(self):
        fact = GameObjectFactory()
        self.result = fact.make(self.choice.get())
        self.result["name"] = self.name.get()
            