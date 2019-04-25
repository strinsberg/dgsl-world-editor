import tkinter as tk

class EditEventFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        
        self.events = list()
        
        self.make_widgets()
        self.defaults()
    
    # Needed for every event
    # Set up to go below subclass defined widgets
    def defaults(self):
        tk.Label(self, text="Once:").grid(row=50)
        
        self.one_time = tk.IntVar()
        self.once = tk.Checkbutton(self, variable=self.one_time)
        self.once.grid(row=50, column=1)
        
        tk.Label(self, text="Subscriptions:").grid(row=80)
        
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



# Testing #########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    events = [
        {"name":"some event", "id":"38ujd8238"},
        {"name":"some other event", "id":"90u4r0j"}
    ]
    
    frame = EditEventFrame(root)
    #frame = EditInformFrame(root)
    #frame = EditKillFrame(root)
    
    frame.set_events(events)
    
    # button to test the get_data() method
    # should print a dictionary with any data that you enter
    get = tk.Button(frame, text="Print entries",
        command=lambda : print(frame.get_data()))
    get.grid()
    
    root.mainloop()