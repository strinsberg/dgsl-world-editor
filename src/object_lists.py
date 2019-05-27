import tkinter as tk

# Widget list of objects that allows adding and removing
class ObjectList(tk.Frame):
    
    def __init__(self, parent, objects, title, add, remove):
        tk.Frame.__init__(self, parent)
        self.objects = []
        self.objects.extend(objects)
        self.title = title
        self.add_command = add
        self.remove_command = remove
        self.makeWidgets()
        self.update()
    
    def makeWidgets(self):
        tk.Label(self, text=self.title).grid(row=0)
        
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=5, sticky='ns')
        tk.Grid.rowconfigure(self, 5, weight=1)
        
        buttons = tk.Frame(self)
        buttons.grid(row=10)
        self.makeButtons(buttons)
    
    def makeButtons(self, buttons):
        tk.Button(buttons, text='Add', command=self.add).grid(
                row=5, column=5)
        tk.Button(buttons, text='Remove', command=self.remove).grid(
                row=5, column=10)
    
    def update(self):
        self.listbox.delete(0, tk.END)
        for obj in self.objects:
            text = obj['name']
            if 'verb' in obj:
                text += " (" + obj['verb'] + ")"
            self.listbox.insert(tk.END, text)
    
    def add(self):
        obj = self.add_command.execute()
        if obj:
            self.objects.append(obj)
            self.update()
    
    def remove(self):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            obj = self.objects.pop(idx)
            self.remove_command.execute(obj['id'])
            self.update()
    
    def get(self):
        return self.objects
            

# Widget list of objects that allows editing
class ObjectListWithEdit(ObjectList):
    
    def __init__(self, parent, objects, title, add, remove, edit):
        self.edit_command = edit
        ObjectList.__init__(self,parent, objects, title, add, remove)
    
    def makeButtons(self, buttons):
        ObjectList.makeButtons(self, buttons)
        tk.Button(buttons, text='Edit', command=self.edit).grid(
                row=5)
    
    def edit(self):
        if len(self.listbox.curselection()) > 0:
            idx = self.listbox.curselection()[0]
            obj = self.objects[idx]
            self.edit_command.execute(obj['id'])


# Testing ######################################################
if __name__=='__main__':
    # Test objects
    class MockCommand:
        def execute(self, obj_id=None):
            if obj_id:
                print(obj_id)
            else:
                return {'name': 'secrets of soup',
                        'id': '113244-sjfk', 'verb': 'read'}
    command = MockCommand()
    
    objects = [{'name': 'close door', 'id': '7j4y-9du'},
                {'name': 'enter room', 'id': 'hs6-shc3'}]
    
    edit_objects = [{'name': 'pizza', 'id': '7j4y-9du'},
                {'name': 'fork', 'id': 'hs6-shc3'}]
    
    # Create and run widgets
    root = tk.Tk()
    
    obj_list = ObjectList(root, objects, 'Subjects',
            command, command)
    obj_list.pack()
    
    obj_edit = ObjectListWithEdit(root, edit_objects, 'Items',
            command, command, command)
    obj_edit.pack()
    
    
    root.mainloop()
    
    # Test get
    print(obj_list.get())
    print()
    print(obj_edit.get())