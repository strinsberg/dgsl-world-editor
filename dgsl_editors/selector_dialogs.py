from SimpleDialog import SimpleDialog
import tkinter as tk

# Entity types #####################################################

class EntityTypeSelector(SimpleDialog):
    def make_widgets(self, master):
        tk.Label(master, text="Choose an Entity type:").pack()
        
        self.choice = tk.StringVar()
        self.choice.set("Entity")
        
        self.type_menu = tk.OptionMenu(master, self.choice,
                            "Entity", "Room", "Container",
                            "NPC", "Door")
        self.type_menu.pack()
    
    def apply(self):
        self.result = self.choice.get()


# Event types ######################################################

class EventTypeSelector(SimpleDialog):
    def make_widgets(self, master):
        tk.Label(master, text="Choose an Event type:").pack()
        
        self.choice = tk.StringVar()
        self.choice.set("Inform")
        
        self.type_menu = tk.OptionMenu(master, self.choice,
                            "Inform", "Kill", "Transfer Item",
                            "Toggle Active", "Move Player",
                            "Equip Suit", "Group",
                            "Ordered", "Interaction",
                            "Conditional")
        self.type_menu.pack()
    
    def apply(self):
        self.result = self.choice.get()


# List selector ###################################################

class ListSelector(SimpleDialog):
    def __init__(self, master, message, items=[], mode=tk.BROWSE,
                 active=[]):
        self.message = message
        self.items = items
        self.mode = mode
        self.active = active
        
        SimpleDialog.__init__(self, master)
    
    def make_widgets(self, master):
        tk.Label(master, text=self.message).pack()
        
        self.item_list = tk.Listbox(master, selectmode=self.mode)
        self.item_list.pack()
        
        for item in self.items:
            self.item_list.insert(tk.END, item["name"])
        
        if len(self.items) > 0 and (self.mode is tk.BROWSE
                                    or self.mode is tk.SINGLE):
            self.item_list.selection_set(0)
        
        for idx in self.active:
            self.item_list.selection_set(idx)
    
    def apply(self):
        self.result = []
        for i in self.item_list.curselection():
            item = self.items[i]
            item["index"] = i
            self.result.append(item)
        
    def cancel(self, event=None):
        self.result = None
        SimpleDialog.cancel(self, event)
        
        

# Testing ##########################################################

if __name__=='__main__':
    root=tk.Tk()
    
    items = [
        {"name": "Some item", "id": "48jd939i3er"},
        {"name": "Other item", "id": "fsjoiej984j"}
    ]
    
    #dialog = EntityTypeSelector(root)
    #dialog = EventTypeSelector(root)
    #dialog = ListSelector(root, "Please select an item", items)
    dialog = ListSelector(root, "Please select an item",
                          items, tk.MULTIPLE)
    
    result = dialog.get_result()
    print(result)
    
    root.mainloop()