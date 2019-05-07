import tkinter as tk
from EntityViewer import EntityViewer
from ObjectList import ObjectList

class ObjectViewer(tk.Frame):
    def __init__(self, viewer, obj):
        tk.Frame.__init__(self, viewer)
        self.obj = obj
        self.make_widgets()
        # object info/editor
        # ObjectLists for things that it can contain or subscribe to
        
    def make_widgets(self):
        tk.Label(self, text=self.obj["name"]).pack()