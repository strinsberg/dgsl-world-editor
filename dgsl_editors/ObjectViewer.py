import tkinter as tk
from EntityInfo import EntityInfo
from EventInfo import EventInfo
from ObjectList import ObjectList

class ObjectViewer(tk.Frame):
    def __init__(self, viewer, obj):
        tk.Frame.__init__(self, viewer)
        self.obj = obj
        self.make_widgets()
        
    def make_widgets(self):
        self.info = self.make_info()
        self.info.grid(row=0, columnspan=2)
        
        self.left_list = self.make_left()
        self.left_list.grid(row=5, column=0)
        
        self.right_list = self.make_right()
        self.right_list.grid(row=5, column=1)
    
    def make_info(self):
        pass
    
    def make_left(self):
        pass
    
    def make_right(self):
        pass


class EntityViewer(ObjectViewer):
    pass
    def make_info(self):
        return EntityInfo(self, self.obj)
    def make_left(self):
        return ObjectList(self, self.obj['items'], 'Items')
    def make_right(self):
        return ObjectList(self, self.obj['events'], 'Events')


class EventViewer(ObjectViewer):
    pass
    def make_info(self):
        return EventInfo(self, self.obj)
    def make_left(self):
        return ObjectList(self, self.obj['subjects'], 'Subjects')
    def make_right(self):
        return ObjectList(self, self.obj['events'], 'Events')


# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    entity = {
        "type": "room",
        "id": "243o4j2oj42",
        "name": "Object",
        "description": "An object in the game that blah blah blah",
        "here": "Some room",
        "obtainable": True, "active": True, "hidden": False,
        "items": [],
        "events": [],
    }
    
    event = {
        "type": "group",
        "id": "243o4j2oj42",
        "name": "open cage",
        "once": True,
        "subjects": [],
        "events": [],
    }
    
    #frame = EntityViewer(root, entity)
    frame = EventViewer(root, event)
    
    frame.pack()
    
    root.mainloop()