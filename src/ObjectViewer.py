import tkinter as tk
from EntityInfo import EntityInfo
from EventInfo import EventInfo
from ObjectList import ObjectList
import game_data as gd

class ObjectViewer(tk.Frame):
    def __init__(self, viewer, obj):
        tk.Frame.__init__(self, viewer)
        self.obj = obj
        self.make_widgets()
        

    def make_widgets(self):
        self.info = InfoFrameFactory.make(self.obj)
        self.info.grid(row=0, columnspan=2, sticky=tk.W)
        
        if "events" is self.obj:
            objs = self.obj["events"]
            title = "Events"
        elif "subjects" in self.obj:
            objs = self.obj["subjects"]
            title = "Subjects"
        else:
            # Object is the game object
            objs = self.obj["rooms"]
            title = "Rooms"
        
        self.left_list = ObjectList(objs, title)
        self.left_list.grid(row=5, column=0, sticky=tk.W)
        
        if gd.is_container(self.obj):
            objs = self.obj["items"]
            title = "Items"
        elif gd.is_group(self.obj):
            objs = self.obj["events"]
            title = "Events"
        else:
            # exit before making the right list
            # there isn't one with other object types
            return
        
        self.right_list = ObjectList(objs, title)
        self.right_list.grid(row=5, column=1, sticky=tk.W)


# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    entity = {
        "type": "container",
        "id": "243o4j2oj42",
        "name": "Object",
        "description": "An object in the game that blah blah blah",
        "here": "Some room",
        "obtainable": True, "active": True, "hidden": False,
        "items": [],
        "events": [],
    }
    
    event = {
        "type": "ordered",
        "id": "243o4j2oj42",
        "name": "open cage",
        "once": True,
        "subjects": [],
        "events": [],
    }
    
    #frame = EntityViewer(root, entity)
    #frame = EventViewer(root, event)
    
    #frame.pack()
    
    root.mainloop()