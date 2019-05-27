import tkinter as tk
from ObjectList import ObjectList
import game_data as gd

class ObjectViewer(tk.Frame):
    
    def __init__(self, parent, obj, widget_info):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.obj = obj
        self.next_row = 0
        self.variables = {}
        if widget_info:
            self.makeWidgets(widget_info)
        else:
            self.null()
    
    def makeWidgets(self, widget_info):
        self.info_frame = tk.Frame(self)
        self.info_frame.grid(row=0, columnspan=2, sticky=tk.W)
        self.addLabel("Type", 'type')
        self.addLabel("ID", 'id')
        self.addIdentifier('Name')
        self.addEntry(self.addVariable('name'))
        self.left_list = None
        self.right_list = None
        
        for info in widget_info:
            kind = info['type']
            if kind == 'list':
                self.addList(info)
            else:
                self.addIdentifier(info['label'])
                var = self.addVariable(info['field'])
                if kind == 'entry':
                    self.addEntry(var)
                elif kind == 'check':
                    self.addCheck(var)
                elif kind == 'option':
                    self.addOption(var, info['options'])
    
    def addIdentifier(self, label):
        tk.Label(self.info_frame, text=label+":").grid(
            row=self.next_row, sticky=tk.W)
    
    def addVariable(self, field):
        var = tk.StringVar()
        var.set(self.obj[field])
        self.variables[field] = var
        return var
    
    def addLabel(self, label, field):
        self.addIdentifier(label)
        tk.Label(self.info_frame, text=self.obj[field]).grid(
                row=self.next_row, column=1, columnspan=2,
                sticky='w')
        self.next_row += 5
    
    def addEntry(self, var):
        tk.Entry(self.info_frame, textvariable=var).grid(row=self.next_row,
                column=1, columnspan=2, sticky=tk.W)
        self.next_row += 5
    
    def addCheck(self, var):
        tk.Checkbutton(self.info_frame, variable=var).grid(row=self.next_row,
                column=1, columnspan=2, sticky=tk.W)
        self.next_row += 5
    
    def addOption(self, var, options):
        menu = tk.OptionMenu( *([self.info_frame, var] + options) )
        menu.grid(row=self.next_row, column=1, columnspan=2,
                sticky=tk.W)
        self.next_row += 5
    
    def addList(self, info):
        objects = self.obj[info['objects']]
        object_list = ObjectList(self, self.parent, objects,
                info['obj_type'], info['title'])
        if info['side'] == 'left':
            self.left_list = object_list
            self.left_list.grid(row=1, column=0, sticky='w')
        else:
            self.right_list = object_list
            self.right_list.grid(row=1, column=1, sticky='w')
    
    def updateObj(self):
        for field in self.variables:
            self.obj[field] = self.variables[field].get()
        
    def finish(self):
        self.updateObj()
        if self.obj['name'] == '':
            # give dialog that makes give a name or
            # deletes the object
            print("no name")
    
    def null(self):
        tk.Label(self, text="Please select an object to edit").pack()


class ObjectViewerFactory:
    
    def make(self, parent, obj=None):
        self.obj = obj
        self.widget_info = []
        
        if obj:
            if gd.is_container(obj):
                self.makeContainer()
            elif gd.is_entity(obj):
                self.makeEntity()
            elif gd.is_event(obj):
                self.makeEvent()
            elif obj['type'] == 'player':
                self.makePlayer()
        else:
            self.widget_info = None
        
        return ObjectViewer(parent, self.obj, self.widget_info)
    
    def makeEntity(self):
        w = []
        w.append({"type": "entry", "label": "Description",
                "field": "description"})
        
        if self.obj["type"] is not "room":
            w.append({"type": "check", "label": "Active",
                    "field": "active"})
            w.append({"type": "check", "label": "Obtainable",
                    "field": "obtainable"})
            w.append({"type": "check", "label": "Hidden",
                    "field": "hidden"})
                    
        w.append({"type": "list", "title": "Events", "side": 'left',
            "objects": "events", "obj_type": "event"})
        self.widget_info.extend(w)
        
    
    def makeContainer(self):
        self.makeEntity()
        self.widget_info.append({"type": "list", "title": "Items",
                "side": 'right', "objects": "items",
                "obj_type": "entity"})
        
    
    def makeEvent(self):
        kind = self.obj['type']
        w = []
        
        # Lists
        w.append({"type": "list", "title": "Subjects",
                "side": 'left', "objects": "subjects",
                "obj_type": "event"})
                
        if gd.is_group(self.obj):
            w.append({"type": "list", "title": "Events",
                    "side": 'right', "objects": "events",
                    "obj_type": "event"})
        
        # beginning stuff
        if kind == 'inform' or kind == 'kill':
            w.append({"type": "entry",
                    "label": "Message", "field": "message"})
        elif kind == 'transfer':
            w.append({"type": "check",
                    "label": "Give", "field": "toTarget"})
        elif kind == "toggle":
            w.append({"type": "entry", "label": "Target",
                "field": "target"})
        elif kind == "ordered":
            w.append({"type": "check",
                "label": "Repeats", "field": "repeats"})
        elif kind == "interaction":
            w.append({"type": "check",
                    "label": "Breakout", "field": "breakout"})
            w.append({"type": "list", "title": "Options",
                    "side": 'right', "objects": "options",
                    "obj_type": "event"})
        
        # always
        w.append({"type": "check", "label": "One Time",
                "field": "once"})
        
        # end
        if "verb" in self.obj:
            w.append({"type": "option", "label": "Verb",
                    "field":"verb", "options": gd.verbs})
        
        if kind == 'kill':
            w.append({"type": "check", "label":
                    "Ending", "field": "ending"})
        
        self.widget_info.extend(w)
    
    def makePlayer(self):
        self.widget_info.append({"type": "check",
                "label": "Ask For Name", "field": "get_name"})
    
    def null(self):
        tk.Label(self, text="Please select an object to edit").pack()

# Testing ######################################################
if __name__=='__main__':
    from GameObjectFactory import GameObjectFactory

    root = tk.Tk()
    
    go_fact = GameObjectFactory()
    obj = go_fact.make('toggle', 'use')
    
    ov_fact = ObjectViewerFactory()
    frame = ov_fact.make(root, obj)
    frame.pack()
    
    root.mainloop()