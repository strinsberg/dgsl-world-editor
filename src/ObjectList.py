import tkinter as tk
from TypeSelector import TypeSelector



class ObjectList(tk.Frame):
    def __init__(self, viewer, objects, obj_type, title):
        tk.Frame.__init__(self, viewer)
        self.objects = objects
        self.obj_type = obj_type
        self.title = title
        self.makeWidgets()
        
    def makeWidgets(self):
        self.title_text = tk.StringVar()
        self.title_text.set(self.title)
        tk.Label(self, textvariable=self.title_text).grid(row=10)
        
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=15)
        self.update()
        
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
        self.listbox.delete(0, tk.END)
        for obj in self.objects:
            self.listbox.insert(tk.END, obj["name"])
    
    def edit(self, event=None):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            # Some code to change object viewer to the
            # selected obj at self.objects[idx]
        print("edit")
        self.update()
    
    def add(self, event=None):
        dialog = TypeSelector(self, self.obj_type)
        result = dialog.getResult()
        if result:
            self.objects.append(result)
            self.update()
    
    def remove(self, event=None):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            self.objects.pop(idx)
        self.update()
