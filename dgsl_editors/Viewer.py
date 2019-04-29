import tkinter as tk

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


class EntityViewer(tk.Frame):
    def __init__(self, viewer, obj):
        tk.Frame.__init__(self, viewer)
        self.obj = obj
        self.make_widgets()
        
    def make_widgets(self):
        tk.Label(self, text="Entity Info").grid(row=1)
        self.edit = tk.Button(self, text="Edit", command=self.edit)
        self.edit.grid(row=1, column=2, sticky=tk.E)
        
        tk.Label(self, text="ID:").grid(row=10, sticky=tk.W)
        self.id = tk.StringVar()
        self.id.set(self.obj["id"])
        self.id_lab = tk.Label(self, textvariable=self.id)
        self.id_lab.grid(row=10, column=1, columnspan=2, sticky=tk.W)
        
        tk.Label(self, text="Name").grid(row=15, sticky=tk.W)
        self.name = tk.StringVar()
        self.name.set(self.obj["name"])
        self.name_lab = tk.Label(self, textvariable=self.name)
        self.name_lab.grid(row=15, column=1, columnspan=2, sticky=tk.W)
        
        tk.Label(self, text="Description:").grid(row=20,sticky=tk.W)
        self.desc = tk.StringVar()
        self.desc.set(self.obj["description"])
        self.desc_lab = tk.Label(self, textvariable=self.desc)
        self.desc_lab.grid(row=20, column=1, columnspan=2, sticky=tk.W)
        
        if self.obj["type"] is not "room":
            tk.Label(self, text="Location:").grid(row=25,sticky=tk.W)
            self.loc = tk.StringVar()
            self.loc.set(self.obj["here"])
            self.loc_lab = tk.Label(self, textvariable=self.loc)
            self.loc_lab.grid(row=25, column=1, sticky=tk.W)
        
        tk.Label(self, text="Active:").grid(row=30,sticky=tk.W)
        self.act = tk.StringVar()
        self.act.set(self.obj["active"])
        self.act_lab = tk.Label(self, textvariable=self.act)
        self.act_lab.grid(row=30, column=1, sticky=tk.W)
        
        tk.Label(self, text="Obtainable:").grid(row=35,sticky=tk.W)
        self.obt = tk.StringVar()
        self.obt.set(self.obj["obtainable"])
        self.obt_lab = tk.Label(self, textvariable=self.obt)
        self.obt_lab.grid(row=35, column=1, sticky=tk.W)
        
        tk.Label(self, text="Hidden:").grid(row=40,sticky=tk.W)
        self.hid = tk.StringVar()
        self.hid.set(self.obj["hidden"])
        self.hid_lab = tk.Label(self, textvariable=self.hid)
        self.hid_lab.grid(row=40, column=1, sticky=tk.W)
    
    def edit(self, event=None):
        print("edit")

# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    obj = {
        "type": "room",
        "id": "243o4j2oj42",
        "name": "Object",
        "description": "An object in the game",
        "here": "Some room",
        "obtainable": True, "active": True, "hidden": False
    }
    
    frame = EntityViewer(root, obj)
    frame.pack()
    
    root.mainloop()