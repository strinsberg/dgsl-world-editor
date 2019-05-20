import tkinter as tk
from ObjectList import ObjectList, SubjectList
from GameObjectFactory import GameObjectFactory
from InfoFrameFactory import InfoFrameFactory
import game_data as gd

class ObjectViewer(tk.Frame):
    def __init__(self, parent, editor, obj=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.editor = editor
        self.obj = obj
        if obj:
            self.make_widgets()
        else:
            self.null()
        # make it possible for obj to be none and return a null

    def make_widgets(self):
        self.info = InfoFrameFactory().make(self, self.obj)
        self.info.grid(row=0, columnspan=2, sticky=tk.W)
        
        if "subjects" in self.obj:
            objs = self.obj["subjects"]
            self.left_list = SubjectList(self, self.editor, objs)
        elif "events" in self.obj:
            objs = self.obj["events"]
            kind = "event"
            title = "Events"
            self.left_list = ObjectList(self, self.editor, objs,
                    kind, title)
        
       
        self.left_list.grid(row=5, column=0, sticky=tk.W)
        
        if gd.is_container(self.obj):
            objs = self.obj["items"]
            kind = "entity"
            title = "Items"
        elif gd.is_group(self.obj):
            objs = self.obj["events"]
            kind = "event"
            title = "Events"
        elif self.obj['type'] == "interaction":
            objs = self.obj['options']
            kind = 'options'
            title = 'Options'
        else:
            # exit before making the right list
            # there isn't one with other object types
            return
        
        self.right_list = ObjectList(self, self.editor, objs, kind, title)
        self.right_list.grid(row=5, column=1, sticky=tk.W)
    
    def null(self):
        tk.Label(self, text="Please select an object to edit").pack()

# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    obj = GameObjectFactory().make("container")
    obj["name"] = "Test Entity"
    
    frame = ObjectViewer(root, obj)
    frame.pack()
    
    root.mainloop()