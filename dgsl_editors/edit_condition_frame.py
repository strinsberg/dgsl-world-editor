import tkinter as tk
from selector_dialogs import ListSelector


# Condition ########################################################

class EditConditionFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.make_widgets()
        self.defaults()
        
    def defaults(self):
        pass
        
    def make_widgets(self):
        pass
        
    def get_data(self):
        self.data = {}


# Question ########################################################

class EditQuestionFrame(EditConditionFrame):
    def make_widgets(self):
        tk.Label(self, text="Question:").grid(row=10)
        self.question = tk.Entry(self)
        self.question.grid(row=10, column=1)
        
        tk.Label(self, text="Answer:").grid(row=15)
        self.answer = tk.Entry(self)
        self.answer.grid(row=15, column=1)
        
    def get_data(self):
        EditConditionFrame.get_data(self)
        self.data["question"] = self.question.get()
        self.data["answer"] = self.answer.get()
        return self.data


# HasItem #########################################################

class EditHasItemFrame(EditConditionFrame):
    """
    The code here has to be possible to abstract
    Some of the code in this class is repeated and it is
    identical, except for the text, to EditTransferItemFrame in
    event_edit_frames
    """
    def make_widgets(self):
        self.entities = list()
        
        tk.Label(self, text="Item:").grid(row=19, sticky=tk.W)
        self.item = {"id":None, "name":None}
        self.itemText = tk.StringVar()
        self.itemText.set("Please Choose")
        self.label = tk.Label(self, textvariable=self.itemText)
        self.label.grid(row=19, column=1)

        self.edit = tk.Button(self, text="Choose",
                              command=self.choose_item)
        self.edit.grid(row=19, column=2)
        
        tk.Label(self, text="Other:").grid(row=20, sticky=tk.W)
        self.other = {"id":None, "name":None}
        self.otherText = tk.StringVar()
        self.otherText.set("Please Choose")
        self.label = tk.Label(self, textvariable=self.otherText)
        self.label.grid(row=20, column=1)

        self.edit = tk.Button(self, text="Choose",
                              command=self.choose_other)
        self.edit.grid(row=20, column=2)
    
    # Set the list of entities
    def set_entities(self, entities):
        self.entities = entities
    
    def choose_item(self, event=None):
        self.items = []
        for ent in self.entities:
            #check for only obtainable items
            self.items.append(ent)
        dialog = ListSelector(self, "Choose an item",
                              self.items)
        self.item = dialog.get_result()[0]
        self.itemText.set(self.item["name"])
    
    # create a dialog to choose a room from a list of rooms
    def choose_other(self, event=None):
        self.others = []
        for ent in self.entities:
            #check for only containers somehow
            self.others.append(ent)
        dialog = ListSelector(self, "Choose an other",
                              self.others)
        self.other = dialog.get_result()[0]
        self.otherText.set(self.other["name"])
    
    def get_data(self):
        EditConditionFrame.get_data(self)
        self.data["other"] = self.other["id"]
        self.data["itemId"] = self.item["id"]
        return self.data
 
        
# Protected ########################################################

class EditProtectedFrame(EditConditionFrame):
    def make_widgets(self):
        tk.Label(self, text="Atmosphere:").grid(row=10, sticky=tk.W)
        
        self.atmos = tk.StringVar()
        self.atmos.set("oxygen")
        
        self.option = tk.OptionMenu(self, self.atmos, "oxygen",
                        "space", "radiation")
        self.option.grid(row=10, column=1)
    
    def get_data(self):
        EditConditionFrame.get_data(self)
        self.data["atmosphere"] = self.atmos.get()
        return self.data

# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    entities = [
        {"name":"some item", "id":"38ujd8238"},
        {"name":"some other item", "id":"90u4r0j"}
    ]
    
    #frame = EditQuestionFrame(root)
    #frame = EditHasItemFrame(root)
    #frame.set_entities(entities)
    frame = EditProtectedFrame(root)
    
    frame.pack()
    
    # button to test the get_data() method
    # should print a dictionary with any data that you enter
    get = tk.Button(frame, text="Print entries",
        command=lambda : print(frame.get_data()))
    get.grid()
    
    root.mainloop()