import tkinter as tk
from SimpleDialog import SimpleDialog


class InfoEditor(SimpleDialog):
    def __init__(self, parent, obj, widget_info):
        self.obj = obj
        self.widget_info = widget_info
        self.next_row = 0
        SimpleDialog.__init__(self, parent)
    
    def makeWidgets(self, body):
        addEntry("Name", "name")
        for info in self.widget_info:
            if info["type"] is "entry":
                addEntry(info["label"], info["kind"])
            elif info["type"] is "check":
                addCheck(info["label"], info["state"])
            else:
                addOption(info["label"], info["options"],
                        info["first"])
    
    def addEntry(self, label, kind):
        pass
    
    def addCheck(self, label, state):
        pass
    
    def addOption(self, label, options, first):
        pass
    
    def apply():
        pass