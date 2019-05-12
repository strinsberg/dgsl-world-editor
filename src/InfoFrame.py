import tkinter as tk

class InfoFrame(tk.Frame):
    def __init__(self, parent, obj):
        tk.Frame.__init__(self, parent)
        self.obj = obj
        self.fields = {}
        self.nextRow = 0
        self.makeFields()
        self.makeWidgets()
    
    def makeFields(self):
        for k in self.obj:
            self.fields[k] = tk.StringVar()
            self.fields[k].set(self.obj[k])
    
    def makeWidgets(self):
        tk.Label(self, text="Attributes").grid(row=1)
        self.edit = tk.Button(self, text="Edit", command=self.edit)
        self.edit.grid(row=1, column=2, sticky=tk.E)
        
        self.addLabel("ID", 'id')
        self.addLabel("Name", 'name')
    
    def addLabel(self, label, kind):
        tk.Label(self, text=label + ":").grid(row=self.nextRow,
                sticky=tk.W)
        self.id_lab = tk.Label(self, textvariable=self.fields[kind])
        self.id_lab.grid(row=self.nextRow, column=1, columnspan=2,
                sticky=tk.W)
        self.nextRow += 5
    
    def update(self):
        for k in self.obj:
            if k in self.fields:
                self.fields[k].set(self.obj[k])
    
    def edit(self):
        editor = InfoEditorFactory()
        editor.make(self.obj)  # Create/run editor dialog
        self.update()
        