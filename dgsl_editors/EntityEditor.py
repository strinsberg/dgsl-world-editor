import tkinter as tk
from SimpleDialog import SimpleDialog

class EntityEditor(SimpleDialog):
    def __init__(self, master, entity):
        self.entity = entity
        SimpleDialog.__init__(self, master)
        
    def make_widgets(self, master):
        self.make_info(master)
        self.make_state(master)
            
    # Extend to children to add fields
    # Default fields go in row 0 and row 1
    def make_info(self, master):
        tk.Label(master, text="Name:").grid(row=10)
        tk.Label(master, text="Description:").grid(row=15)

        self.name = tk.Entry(master)
        self.name.insert(0, self.entity['name'])
        self.desc = tk.Entry(master)
        self.desc.insert(0, self.entity['description'])

        self.name.grid(row=10, column=1)
        self.desc.grid(row=15, column=1)
    
    # Extend to add other states
    # Default to row 60+ to allow easily putting other
    # rows under the default info entry boxes
    def make_state(self, master):
        tk.Label(master, text="Active:").grid(row=20)
        tk.Label(master, text="Obtainable:").grid(row=25)
        tk.Label(master, text="Hidden:").grid(row=30)
        
        self.act = tk.IntVar()
        self.obt = tk.IntVar()
        self.hid = tk.IntVar()
        
        self.act.set(self.entity["active"])
        self.obt.set(self.entity["obtainable"])
        self.hid.set(self.entity["hidden"])
        
        self.active = tk.Checkbutton(master, variable=self.act)
        self.obtainable = tk.Checkbutton(master, variable=self.obt)
        self.hidden = tk.Checkbutton(master, variable=self.hid)
        
        self.active.grid(row=20, column=1)
        self.obtainable.grid(row=25, column=1)
        self.hidden.grid(row=30, column=1)
    
    def apply(self):
        self.entity["name"] = self.name.get()
        self.entity["description"] = self.desc.get()
        self.entity["active"] = int_to_bool(self.act.get())
        self.entity["obtainable"] = int_to_bool(self.obt.get())
        self.entity["hidden"] = int_to_bool(self.hid.get())

def int_to_bool(n):
    if n > 0:
        return True
    else:
        return False

# Testing ###########################################################

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
    
    win = EntityEditor(root, obj)
    
    root.mainloop()