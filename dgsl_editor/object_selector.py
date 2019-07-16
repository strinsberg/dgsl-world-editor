import tkinter as tk
from . import simple_dialog


class ObjectSelector(simple_dialog.SimpleDialog):
    def __init__(self, parent, objects):
        self.objects = objects
        simple_dialog.SimpleDialog.__init__(self, parent)

    def makeWidgets(self, body):
        self.listbox = tk.Listbox(body)
        self.listbox.pack()

        for obj in self.objects:
            self.listbox.insert(tk.END, obj['name'])

    def apply(self):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            self.result = self.objects[idx]

    def validate(self):
        if len(self.listbox.curselection()) > 0:
            return True
        return False