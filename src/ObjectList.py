import tkinter as tk


class ObjectList(tk.Frame):
    def __init__(self, viewer, objects, title="Rooms"):
        tk.Frame.__init__(self, viewer)
        self.objects = objects
        self.title = title
        self.makeWidgets()
        
    def makeWidgets(self):
        # title
        self.title_text = tk.StringVar()
        self.title_text.set(self.title)
        tk.Label(self, textvariable=self.title_text).grid(row=10)
        
        # list
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=15)
        
        # buttons
        self.makeButtons()
        
    
    def makeButtons(self):
        self.buttons = tk.Frame(self)
        
        self.edit = tk.Button(self.buttons, text="Edit", command=self.edit)
        self.edit.grid(row=1)
        
        self.add = tk.Button(self.buttons, text="Add", command=self.add)
        self.add.grid(row=1, column=1)
        
        self.remove = tk.Button(self.buttons, text="Remove", command=self.remove)
        self.remove.grid(row=1, column=2)
        
        self.buttons.grid(row=20, sticky=tk.W)
    
    def update(self):
        pass
    
    def edit(self, event=None):
        print("edit")
    
    def add(self, event=None):
        dialog = TypeSelector(kind)
        self.objects.append(dialog.getResult())
    
    def remove(self, event=None):
        print("remove")
