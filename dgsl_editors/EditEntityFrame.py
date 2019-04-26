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
    
    # Extend to children to add fields
    # Default fields go in row 0 and row 1
    def make_info(self):
        tk.Label(self, text="Name:").grid(row=0)
        tk.Label(self, text="Description:").grid(row=1)
        
        self.name = tk.Entry(self)
        self.desc = tk.Entry(self)
        
        self.name.grid(row=0, column=1)
        self.desc.grid(row=1, column=1)
    
    # Extend to add other states
    # Default to row 60+ to allow easily putting other
    # rows under the default info entry boxes
    def make_state(self):
        tk.Label(self, text="Active:").grid(row=60)
        tk.Label(self, text="Hidden:").grid(row=61)
        
        self.act = tk.IntVar()
        self.hid = tk.IntVar()
        self.act.set(1)
        
        self.active = tk.Checkbutton(self, variable=self.act)
        self.hidden = tk.Checkbutton(self, variable=self.hid)
        
        self.active.grid(row=60, column=1)
        self.hidden.grid(row=61, column=1)
        
        self.make_obtainable()
    
    # Overide if you want to change obtainable
    # ie. for classes that it is fixed
    # If you don't want obtainable then set
    # self.obtainalbe = None
    def make_obtainable(self):
        tk.Label(self, text="Obtainable:").grid(row=62)
        
        self.obt = tk.IntVar()
        self.obt.set(1)
        
        self.obtainable = tk.Checkbutton(self, variable=self.obt)
        self.obtainable.grid(row=62, column=1)
    
    # Extend in children to pass on all fields
    # Returns data from all fields in a dictionary
    # Can be used as a callback
    def get_data(self, event=None):
        self.data = {
            "name": self.name.get(),
            "desc": self.desc.get(),
            "active": self.act.get(),
            "hidden": self.hid.get()
        }
        if self.obtainable:
            self.data["obtainable"] = self.obt.get()
        return self.data


# Main for testing ################################################

if __name__=='__main__':
    root=tk.Tk()
    
    frame = EditEntityFrame(root)
    
    # button to test the get_data() method
    # should print a dictionary with any data that you enter
    get = tk.Button(frame, text="Print entries",
        command=lambda : print(frame.get_data()))
    get.grid()
    
    root.mainloop()