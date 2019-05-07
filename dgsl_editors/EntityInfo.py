import tkinter as tk
from EntityEditor import EntityEditor

class EntityInfo(tk.Frame):
    def __init__(self, viewer, obj):
        tk.Frame.__init__(self, viewer)
        self.obj = obj
        self.make_fields()
        self.make_widgets()
    
    def make_fields(self):
        self.fields = {}
        for k in self.obj:
            self.fields[k] = tk.StringVar()
            self.fields[k].set(self.obj[k])
        
    def make_widgets(self):
        tk.Label(self, text="Entity Info").grid(row=1)
        self.edit = tk.Button(self, text="Edit", command=self.edit)
        self.edit.grid(row=1, column=2, sticky=tk.E)
        
        tk.Label(self, text="ID:").grid(row=10, sticky=tk.W)
        self.id_lab = tk.Label(self, textvariable=self.fields['id'])
        self.id_lab.grid(row=10, column=1, columnspan=2, sticky=tk.W)
        
        tk.Label(self, text="Name").grid(row=15, sticky=tk.W)
        self.name_lab = tk.Label(self,
                textvariable=self.fields["name"])
        self.name_lab.grid(row=15, column=1, columnspan=2, sticky=tk.W)
        
        # can we make this wrap after a certain length?
        tk.Label(self, text="Description:").grid(row=20,sticky=tk.W)
        self.desc_lab = tk.Label(self,
                textvariable=self.fields["description"])
        self.desc_lab.grid(row=20, column=1, columnspan=2, sticky=tk.W)
        
        if self.fields["type"] is not "room":
            tk.Label(self, text="Location:").grid(row=25,sticky=tk.W)
            self.loc_lab = tk.Label(self,
                    textvariable=self.fields["here"])
            self.loc_lab.grid(row=25, column=1, sticky=tk.W)
        
        if "active" in self.fields:
            tk.Label(self, text="Active:").grid(row=30,sticky=tk.W)
            self.act_lab = tk.Label(self,
                    textvariable=self.fields["active"])
            self.act_lab.grid(row=30, column=1, sticky=tk.W)
        
        if "obtainable" in self.fields:
            tk.Label(self, text="Obtainable:").grid(row=35,
                    sticky=tk.W)
            self.obt_lab = tk.Label(self,
                    textvariable=self.fields["obtainable"])
            self.obt_lab.grid(row=35, column=1, sticky=tk.W)
        
        if "hidden" in self.fields:
            tk.Label(self, text="Hidden:").grid(row=40,sticky=tk.W)
            self.hid_lab = tk.Label(self, textvariable=self.fields['hidden'])
            self.hid_lab.grid(row=40, column=1, sticky=tk.W)
    
    def update(self):
        for k in self.obj:
            if k in self.fields:
                self.fields[k].set(self.obj[k])
    
    def edit(self, event=None):
        EntityEditor(self, self.obj)
        self.update()


# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    obj = {
        "type": "room",
        "id": "243o4j2oj42",
        "name": "Object",
        "description": "An object in the game that blah blah blah",
        "here": "Some room",
        "obtainable": True, "active": True, "hidden": False
    }
    
    frame = EntityInfo(root, obj)
    frame.pack()
    
    root.mainloop()