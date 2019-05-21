import tkinter as tk
from SimpleDialog import SimpleDialog


class InfoEditor(SimpleDialog):
    def __init__(self, parent, obj, widget_info, show_name=True):
        self.obj = obj
        self.widget_info = widget_info
        self.show_name = show_name
        self.variables = {}
        self.next_row = 5
        SimpleDialog.__init__(self, parent)
    
    def makeWidgets(self, body):
        if self.show_name:
            self.addEntry(body, "Name", "name")
        
        for info in self.widget_info:
            if info["type"] is "entry":
                self.addEntry(body, info["label"], info["field"])
            elif info["type"] is "check":
                self.addCheck(body, info["label"], info["field"])
            elif info["type"] is "option":
                self.addOption(body, info["label"], info["field"],
                        info["options"])
    
    def addEntry(self, body, label, field):
        tk.Label(body, text=label).grid(row=self.next_row,
                sticky=tk.W)
        var = tk.StringVar()
        var.set(self.obj[field])
        self.variables[field] = var
        tk.Entry(body, textvariable=var).grid(row=self.next_row,
                column=1, columnspan=2, sticky=tk.W)
        self.next_row += 5
    
    def addCheck(self, body, label, field):
        tk.Label(body, text=label).grid(row=self.next_row,
                sticky=tk.W)
        var = tk.IntVar()
        var.set(self.obj[field])
        self.variables[field] = var
        tk.Checkbutton(body, variable=var).grid(row=self.next_row,
                column=1, columnspan=2, sticky=tk.W)
        self.next_row += 5
    
    def addOption(self, body, label, field, options):
        tk.Label(body, text=label).grid(row=self.next_row,
                sticky=tk.W)
        var = tk.StringVar()
        var.set(self.obj[field])
        self.variables[field] = var
        menu = tk.OptionMenu( *([body, var] + options) )
        menu.grid(row=self.next_row, column=1, columnspan=2,
                sticky=tk.W)
        self.next_row += 5

    def apply(self):
        for field in self.variables:
            self.obj[field] = self.variables[field].get()
        self.result = self.obj
    
    def validate(self):
        try:
            if self.variables['name'].get() == '':
                return False
        except KeyError:
            pass
        return True