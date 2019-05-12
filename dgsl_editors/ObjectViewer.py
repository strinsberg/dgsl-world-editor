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
        self.info = self.make_info()
        self.info.grid(row=0, columnspan=2, sticky=tk.W)
        
        self.left_list = self.make_left()
        self.left_list.grid(row=5, column=0, sticky=tk.W)
        
        self.right_list = self.make_right()
        self.right_list.grid(row=5, column=1, sticky=tk.W)
    
    ''' Once you get some new design implemented
    def make_widgets(self):
        self.info = InfoFrameFactory.make(self.obj)
        self.info.grid(row=0, columnspan=2, sticky=tk.W)
        
        self.left_list = ObjectListFactory.make(self.obj)
        self.left_list.grid(row=5, column=0, sticky=tk.W)
        
        if gd.is_container(self.obj) or gd.is_group(self.obj):
            self.right_list = ObjectListFactory.make(self.obj)
            self.right_list.grid(row=5, column=1, sticky=tk.W)
    '''


class EntityViewer(ObjectViewer):
    pass
    def make_info(self):
        return EntityInfo(self, self.obj)
    def make_left(self):
        return ObjectList(self, self.obj['events'], 'Events')
    def make_right(self):
        if gd.is_container(self.obj):
            return ObjectList(self, self.obj['items'], 'Items')
        else:
            return tk.Frame(self)


class EventViewer(ObjectViewer):
    pass
    def make_info(self):
        return EventInfo(self, self.obj)
    def make_left(self):
        return ObjectList(self, self.obj['subjects'], 'Subjects')
    def make_right(self):
        if gd.is_group(self.obj):
            return ObjectList(self, self.obj['events'], 'Events')
        else:
            return tk.Frame(self)


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
    frame = EventViewer(root, event)
    
    frame.pack()
    
    root.mainloop()