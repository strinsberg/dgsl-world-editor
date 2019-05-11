import tkinter as tk
import game_data as gd
from EventEditor import EventEditor


class EventInfo(tk.Frame):
    def __init__(self, viewer, obj):
        tk.Frame.__init__(self, viewer)
        self.obj = obj
        self.fields = {}
        self.make_fields()
        self.make_widgets()
       
    def make_fields(self):
        for k in self.obj:
            self.fields[k] = tk.StringVar()
            self.fields[k].set(self.obj[k])
     
    def make_widgets(self):
        tk.Label(self, text="Event Info").grid(row=1)
        self.edit = tk.Button(self, text="Edit", command=self.edit)
        self.edit.grid(row=1, column=2, sticky=tk.E)
    
        tk.Label(self, text="ID:").grid(row=10, sticky=tk.W)
        self.id_lab = tk.Label(self, textvariable=self.fields['id'])
        self.id_lab.grid(row=10, column=1, columnspan=2, sticky=tk.W)
        
        tk.Label(self, text="Name").grid(row=15, sticky=tk.W)
        self.name_lab = tk.Label(self,
                textvariable=self.fields["name"])
        self.name_lab.grid(row=15, column=1, columnspan=2, sticky=tk.W)

        tk.Label(self, text="One Time:").grid(row=25, sticky=tk.W)
        self.once_lab = tk.Label(self,
                textvariable=self.fields["once"])
        self.once_lab.grid(row=25, column=1, columnspan=2, sticky=tk.W)
        
        if "verb" in self.fields:
            tk.Label(self, text="Verb:").grid(row=30, sticky=tk.W)
            self.verb_lab = tk.Label(self,
                    textvariable=self.fields["verb"])
            self.verb_lab.grid(row=30, column=1, columnspan=2,
                    sticky=tk.W)
    
    
    def update(self):
        for k in self.obj:
            if k in self.fields:
                self.fields[k].set(self.obj[k])
    
    def edit(self, event=None):
        EventEditor(self, self.obj)
        self.update()


# Testing ######################################################

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
    
    frame = EventInfo(root, obj)
    frame.pack()
    
    root.mainloop()