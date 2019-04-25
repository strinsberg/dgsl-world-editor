import tkinter as tk

class SimpleDialog(Toplevel):
    def __init__(self, parent, title =""):
        Toplevel.__init__(self, parent)
        self.transient(parent)
        
        self.result = None
        
        self.parent = parent
        body = tk.Frame(self)
        self.make_widgets(body)
        body.pack()
        self.make_buttons()
        
        self.initial_focus = self

    def show(self):
        self.grab_set()
        
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        
        self.initial_focus.focus_set()
        self.wait_window(self)
        return self.result
    
    def make_widgets(self, master):
        pass
    
    def make_buttons(self):
        box = tk.Frame(self)
        k = tk.Button(box, text="OK", width=10, command=self.ok,
                   default=tk.ACTIVE)
        k.pack(side=tk.LEFT, padx=5, pady=5)
        c = tk.Button(box, text="Cancel", width=10,
                   command=self.cancel, default=tk.ACTIVE)
        c.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        
        box.pack()
    
    def ok(self, event=None):
        if not self.validate():
            pass # do something
        
        self.withdraw()
        self.update_idletasks()
        
        self.apply()
        self.cancel()
    
    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()
    
    # override if input needs validation
    def validate(self):
        return True
    
    # override
    def apply(self):
        pass