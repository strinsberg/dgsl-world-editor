import tkinter as tk
from EntityEditor import EntityEditor

class Viewer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.make_widgets()
        # list of things we are editing
        # the current thing being edited
            # its info
            # its entities or subscritpions or events
        # previous thing edited
        
    
    def make_widgets(self):
        self.prev = tk.Frame(self)
        self.prev.pack() #temp
        tk.Label(self.prev, text="Entity info here").pack()
        self.obj_list = ObjectList(self, []).pack(side=tk.LEFT) #temp
        self.obj_viewer = ObjectViewer(self, {"name":"TempViewer"}).pack(side=tk.RIGHT) #temp


class ObjectList(tk.Frame):
    def __init__(self, viewer, objects, title="Rooms"):
        tk.Frame.__init__(self, viewer)
        self.viewer = viewer
        self.objects = objects
        self.title = title
        self.make_widgets()
        
    def make_widgets(self):
        # title
        self.titleText = tk.StringVar()
        self.titleText.set(self.title)
        tk.Label(self, textvariable=self.titleText).grid(row=10)
        
        # list
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=15)
        
        # buttons
        self.make_buttons()
        
    
    def make_buttons(self):
        self.buttons = tk.Frame(self)
        
        self.edit = tk.Button(self.buttons, text="Edit", command=self.edit)
        self.edit.grid(row=1)
        
        self.add = tk.Button(self.buttons, text="Add", command=self.add)
        self.add.grid(row=1, column=1)
        
        self.remove = tk.Button(self.buttons, text="Remove", command=self.remove)
        self.remove.grid(row=1, column=2)
        
        self.buttons.grid(row=20, sticky=tk.W)
    
    def edit(self, event=None):
        print("edit")
    
    def add(self, event=None):
        print("add")
    
    def remove(self, event=None):
        print("remove")


class ObjectViewer(tk.Frame):
    def __init__(self, viewer, obj):
        tk.Frame.__init__(self, viewer)
        self.obj = obj
        self.make_widgets()
        # object info/editor
        # ObjectLists for things that it can contain or subscribe to
        
    def make_widgets(self):
        tk.Label(self, text=self.obj["name"]).pack()


# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    root.mainloop()