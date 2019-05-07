import tkinter as tk
from EntityViewer import EntityViewer
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

