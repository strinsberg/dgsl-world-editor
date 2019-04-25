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


# Testing ##########################################################

if __name__=='__main__':
    root=tk.Tk()
    
    #dialog = EntityTypeSelector(root)
    dialog = EventTypeSelector(root)
    
    result = dialog.get_result()
    print(result)
    
    root.mainloop()