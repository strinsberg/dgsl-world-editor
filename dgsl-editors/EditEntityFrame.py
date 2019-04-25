import tkinter as tk

class EditEntityFrame(tk.Frame):
    """
    Base frame for editing an entity.
    
    Lists base entity fields name and description with entry boxes.
    Lists base entity states active, hidden, and obtainable with
    checkbuttons.
    
    Allows all data to be retrieved in a dictionairy.
    """
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        
        self.make_info()
        self.make_state()
    
    def make_info(self):
        # Extend to children to add fields
        # default is row 0-4. 0-3 if make_obtainable is
        # overriden to make self.obtainable=None
        tk.Label(self, text="Name:").grid(row=0)
        tk.Label(self, text="Description:").grid(row=1)
        
        self.name = tk.Entry(self)
        self.desc = tk.Entry(self)
        
        self.name.grid(row=0, column=1)
        self.desc.grid(row=1, column=1)
    
    def make_state(self):
        # Extend to add other states
        tk.Label(self, text="Active:").grid(row=2)
        tk.Label(self, text="Hidden:").grid(row=3)
        
        self.act = tk.IntVar()
        self.hid = tk.IntVar()
        
        self.active = tk.Checkbutton(self, variable=self.act)
        self.hidden = tk.Checkbutton(self, variable=self.hid)
        
        self.active.grid(row=2, column=1)
        self.hidden.grid(row=3, column=1)
        
        self.make_obtainable()
    
    def make_obtainable(self):
        # Overide if you want to change obtainable
        # ie. for classes that it is fixed
        # If you don't want obtainable then set
        # self.obtainalbe = None and start your other
        # widgets in row=4
        tk.Label(self, text="Obtainable:").grid(row=4)
        self.obt = tk.IntVar()
        self.obtainable = tk.Checkbutton(self, variable=self.obt)
        self.obtainable.grid(row=4, column=1)
    
    def get_data(self, event=None):
        # Extend in children to pass on all fields
        # Returns data from all fields in a dictionary
        # Can be used as a callback
        data = {
            "name": self.name.get(),
            "desc": self.desc.get(),
            "active": self.act.get(),
            "hidden": self.hid.get()
        }
        if self.obtainable:
            data["obtainable"] = self.obt.get()
        return data


# Main for testing ################################################

if __name__=='__main__':
    root=tk.Tk()
    
    frame = EditEntity(root)
    
    get = tk.Button(frame, text="Print entries", command=lambda : print(frame.get_data()))
    get.grid()
    
    root.mainloop()