import tkinter as tk
from ObjectList import ObjectList
from GameObjectFactory import GameObjectFactory
from InfoFrameFactory import InfoFrameFactory
import game_data as gd

class ObjectViewer(tk.Frame):
    def __init__(self, parent, obj):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.obj = obj
        self.make_widgets()
        

    def make_widgets(self):
        self.info = InfoFrameFactory().make(self, self.obj)
        self.info.grid(row=0, columnspan=2, sticky=tk.W)
        
        if "events" in self.obj:
            objs = self.obj["events"]
            kind = "event"
            title = "Events"
        elif "subjects" in self.obj:
            objs = self.obj["subjects"]
            kind = "event"
            title = "Subjects"
        else:
            # Object is the game object
            objs = self.obj["rooms"]
            kind = "room"
            title = "Rooms"
        
        self.left_list = ObjectList(self, self.parent, objs, kind, title)
        self.left_list.grid(row=5, column=0, sticky=tk.W)
        
        if gd.is_container(self.obj):
            objs = self.obj["items"]
            kind = "entity"
            title = "Items"
        elif gd.is_group(self.obj):
            objs = self.obj["events"]
            kind = "event"
            title = "Events"
        else:
            # exit before making the right list
            # there isn't one with other object types
            return
        
        self.right_list = ObjectList(self, self.parent, objs, kind, title)
        self.right_list.grid(row=5, column=1, sticky=tk.W)


# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    obj = GameObjectFactory().make("container")
    obj["name"] = "Test Entity"
    
    frame = ObjectViewer(root, obj)
    frame.pack()
    
    root.mainloop()