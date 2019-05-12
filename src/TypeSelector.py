import tkinter as tk
from SimpleDialog import SimpleDialog
from GameObjectFactory import GameObjectFactory

class TypeSelector(SimpleDialog):
    def __init__(self, parent, kind):
        self.kind = kind
        SimpleDialog.__init(self, parent)
        
    def makeWidgets(self, master):
        tk.Label(text = self.kind + " Type:").grid(row=0, sticky=tk.W)
        self.choice = tk.StringVar(master)
        
        if self.kind is "Entity":
            self.choice.set(self.entities[0])
            self.menu = apply(tk.OptionMenu,
                    (master, self.choice) + self.self.entities)
        if self.kind is "Event":
            self.choice.set(self.events[0])
            self.menu = apply(tk.OptionMenu,
                    (master, self.choice) + self.events)
        else:
            self.choice.set(self.conds[0])
            self.menu = apply(tk.OptionMenu,
                    (master, self.choice) + self.conds)
    
    def apply():
        fact = GameObjectFactory()
        self.result = fact.make(self.choice.get())
            