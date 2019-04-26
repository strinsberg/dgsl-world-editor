import tkinter as tk
from selector_dialogs import ListSelector

class EditEventFrame(tk.Frame):
    def __init__(self, master, entity_owned = True):
        tk.Frame.__init__(self, master)
        self.pack()
        
        self.entity_owned = entity_owned
        self.events = list()
        
        self.make_widgets()
        self.defaults()
    
    # Needed for every event
    # Set up to go below subclass defined widgets
    def defaults(self):
        if self.entity_owned:
            tk.Label(self, text="Verb").grid(row=1, sticky=tk.W)
            self.verb = tk.Entry(self)
            self.verb.grid(row=1, column=0, sticky=tk.E)
        
        tk.Label(self, text="Once:").grid(row=5, sticky=tk.W)
        
        self.one_time = tk.IntVar()
        self.once = tk.Checkbutton(self, variable=self.one_time)
        self.once.grid(row=5, column=1)
        
        tk.Label(self, text="Subscriptions:").grid(row=80, sticky=tk.W)
        
        self.event_list = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.event_list.grid(row=80, column=1)
    
    # Set the list of events to subscribe to
    def set_events(self, events):
        self.events = events
        for e in self.events:
            self.event_list.insert(tk.END, e["name"])
    
    # Override
    def make_widgets(self):
        pass
    
    # Override
    def get_data(self):
        subjects = list()
        for i in self.event_list.curselection():
            subjects.append(self.events[i]["id"])
        
        self.data = {
            "once": self.one_time.get(),
            "subjects": subjects
        }
        
        if self.entity_owned:
            self.data["verb"] = self.verb.get()
        return self.data
        

# Inform ###########################################################

class EditInformFrame(EditEventFrame):
    def make_widgets(self):
        tk.Label(self, text="Message:").grid(row=10)
        
        self.message = tk.Entry(self)
        self.message.grid(row=10, column=1)
    
    def get_data(self):
        EditEventFrame.get_data(self)
        
        self.data["message"] = self.message.get()
        return self.data


# Kill #############################################################

class EditKillFrame(EditInformFrame):
    def make_widgets(self):
        EditInformFrame.make_widgets(self)
        tk.Label(self, text="Ending:").grid(row=20)
        
        self.end = tk.IntVar()
        self.ending = tk.Checkbutton(self, variable=self.end)
        self.ending.grid(row=20, column=1)
    
    def get_data(self):
        EditInformFrame.get_data(self)
        
        self.data["ending"] = self.end.get()
        return self.data


# Move Player ####################################################

class EditMovePlayer(EditEventFrame):
    def make_widgets(self):
        tk.Label(self, text="Destination:").grid(row=20, sticky=tk.W)
        
        self.room = tk.StringVar()
        self.room.set("Please Choose")
        self.label = tk.Label(self, textvariable=self.room)
        self.label.grid(row=20, column=1)

        self.edit = tk.Button(self, text="Choose",
                              command=self.choose_room)
        self.edit.grid(row=20, column=2)
    
    # Set the list of events to subscribe to
    def set_rooms(self, rooms):
        self.rooms = rooms
        
    # create a dialog to choose a room from a list of rooms
    def choose_room(self, event=None):
        dialog = ListSelector(self, "Choose a destination",
                              self.rooms)
        self.target = dialog.get_result()[0]
        self.room.set(self.target["name"])
        
    def get_data(self):
        EditEventFrame.get_data(self)
        self.data["destination"] = self.target["id"]
        return self.data
        

# Testing #########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    events = [
        {"name":"some event", "id":"38ujd8238"},
        {"name":"some other event", "id":"90u4r0j"}
    ]
    
    rooms = [
        {"name":"some room", "id":"38h6h3g4bd"},
        {"name":"some other room", "id":"3thewj"}
    ]
    
    #frame = EditEventFrame(root)
    #frame = EditInformFrame(root, False)
    #frame = EditKillFrame(root)
    frame = EditMovePlayer(root)
    frame.set_rooms(rooms)
    
    frame.set_events(events)
    
    # button to test the get_data() method
    # should print a dictionary with any data that you enter
    get = tk.Button(frame, text="Print entries",
        command=lambda : print(frame.get_data()))
    get.grid()
    
    root.mainloop()