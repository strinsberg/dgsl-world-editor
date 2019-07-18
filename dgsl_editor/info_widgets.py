import tkinter as tk


# Base class widget for object info rows
class InfoWidget(tk.Frame):
    def __init__(self, parent, label):
        tk.Frame.__init__(self, parent)
        self.label = label
        self.makeWidgets()

    def makeWidgets(self):
        tk.Label(self, text=self.label + ": ").grid(row=0, sticky='w')
        tk.Grid.columnconfigure(self, 1, weight=1)

    def get(self):
        assert False, "Must override get"


# Entry widget for object field
class InfoEntry(InfoWidget):
    def __init__(self, parent, label, text):
        self.text_var = tk.StringVar()
        self.text_var.set(text)
        InfoWidget.__init__(self, parent, label)

    def makeWidgets(self):
        InfoWidget.makeWidgets(self)
        tk.Entry(self, textvariable=self.text_var).grid(row=0,
                                                        column=1,
                                                        sticky='we')

    def get(self):
        return self.text_var.get()


# Check box widget for object field
class InfoCheck(InfoWidget):
    def __init__(self, parent, label, state):
        self.state_var = tk.IntVar()
        self.state_var.set(state)
        InfoWidget.__init__(self, parent, label)

    def makeWidgets(self):
        InfoWidget.makeWidgets(self)
        tk.Checkbutton(self, variable=self.state_var).grid(row=0, column=1)

    def get(self):
        return self.state_var.get()


# Option menu widget for object field
class InfoOption(InfoWidget):
    def __init__(self, parent, label, first, options):
        self.text_var = tk.StringVar()
        self.text_var.set(first)
        self.options = options
        InfoWidget.__init__(self, parent, label)

    def makeWidgets(self):
        InfoWidget.makeWidgets(self)
        tk.OptionMenu(*([self, self.text_var] + self.options)).grid(row=0,
                                                                    column=1)

    def get(self):
        return self.text_var.get()


# Label widget for object field
class InfoLabel(InfoWidget):
    def __init__(self, parent, label, text):
        self.text_var = tk.StringVar()
        self.text_var.set(text)
        InfoWidget.__init__(self, parent, label)

    def makeWidgets(self):
        InfoWidget.makeWidgets(self)
        tk.Label(self, textvariable=self.text_var).grid(row=0, column=1)

    def get(self):
        return self.text_var.get()


# Item selector widget with label for object field
class InfoSelector(InfoLabel):
    def __init__(self, parent, label, obj_info, kind, select, edit,
                 full_obj_info=False):
        self.commands = {'edit': edit, 'select': select}
        self.obj_info = obj_info
        self.kind = kind
        self.full_obj_info = full_obj_info
        name = self.obj_info['name'] if obj_info else None
        InfoLabel.__init__(self, parent, label, name)

    def makeWidgets(self):
        InfoLabel.makeWidgets(self)
        tk.Button(self, text="Edit", command=self.edit).grid(row=0,
                                                             column=2,
                                                             sticky='e')
        tk.Button(self, text="New", command=self.select).grid(row=0,
                                                              column=3,
                                                              sticky='e')

    def select(self):
        obj = self.commands['select'].execute(self.kind, is_selector=True)
        if obj:
            if self.full_obj_info:
                self.obj_info = obj
            else:
                self.obj_info = {'name': obj['name'], 'id': obj['id']}
                if 'verb' in obj:
                    self.obj_info['verb'] = obj['verb']
                self.text_var.set(self.obj_info['name'])

    def edit(self):
        if self.obj_info:
            self.commands['edit'].execute(self.obj_info['id'])

    def get(self):
        return self.obj_info


'''
# Testing ######################################################
if __name__ == '__main__':
    # Mock command class
    class MockNew:
        def execute(self):
            return {'name': 'A new name', 'id': '3rh2ih3r2foi2'}

    class MockEdit:
        def execute(self, ID):
            print('edit', ID)

    # Create and run widgets
    root = tk.Tk()

    lab = InfoLabel(root, "Name", "Steven of sexsmith")
    lab.pack(anchor='w', fill=tk.X, expand=1)

    ent = InfoEntry(root, "Description", "A nice man")
    ent.pack(anchor='w', fill=tk.X, expand=1)

    check = InfoCheck(root, "Awake", 1)
    check.pack(anchor='w', fill=tk.X, expand=1)

    opt = InfoOption(root, "Strength", "1", ["1", "2", "3", "4"])
    opt.pack(anchor='w', fill=tk.X, expand=1)

    sel = InfoSelector(root, "School", {
        'name': 'University of Lethbridge',
        'id': 'iiie474-4858'
    }, 'entity', MockNew(), MockEdit())
    sel.pack(anchor='w', fill=tk.X, expand=1)

    root.mainloop()

    # Show results of the get functions after the editing
    print(lab.get())
    print(ent.get())
    print(check.get())
    print(opt.get())
    print(sel.get())
'''
