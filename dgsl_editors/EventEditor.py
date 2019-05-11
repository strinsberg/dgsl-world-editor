import tkinter as tk
from SimpleDialog import SimpleDialog

class EventEditor(SimpleDialog):
    def __init__(self, master, event):
        self.event = event
        SimpleDialog.__init__(self, master)
        
    def make_widgets(self, master):
        self.make_info(master)
        self.make_state(master)
            
    # Extend to children to add fields
    def make_info(self, master):
        tk.Label(master, text="Name:").grid(row=5)
        tk.Label(master, text="Description:").grid(row=10)

        self.name = tk.Entry(master)
        self.name.insert(0, self.event['name'])
        self.desc = tk.Entry(master)
        self.desc.insert(0, self.event['description'])

        self.name.grid(row=5, column=1)
        self.desc.grid(row=10, column=1)
        
        if "verb" in self.event:
            tk.Label(master, text="Verb:").grid(row=15)
            
            self.verb = tk.StringVar(master)
            self.verb.set(self.event["verb"])
            self.option = tk.OptionMenu(master, self.verb, "use",
                    "talk", "get", "drop", "look")
            self.option.grid(row=15, column=1)
    
    # Extend to add other states
    def make_state(self, master):
        tk.Label(master, text="One Time:").grid(row=20)
        self.once = tk.IntVar()
        self.once.set(self.event["once"])
        
        self.one_time = tk.Checkbutton(master, variable=self.once)
        self.one_time.grid(row=20, column=1)
    
    def apply(self):
        self.event["name"] = self.name.get()
        self.event["description"] = self.desc.get()
        self.event["once"] = int_to_bool(self.once.get())


def int_to_bool(n):
    if n > 0:
        return True
    else:
        return False


# Testing ###########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    obj = {
        "type": "event",
        "id": "23rj23r20r032",
        "name": "some event",
        "description": "turns you into a newt",
        "once": True,
        "verb": "use"
    }
    
    win = EventEditor(root, obj)
    
    root.mainloop()