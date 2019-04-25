import tkinter as tk

class EditEventFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        
        self.make_widgets()
        self.defaults()
    
    def defaults(self):
        tk.Label(self, text="Once:").grid(row=50)
        
        self.one_time = tk.IntVar()
        self.once = tk.Checkbutton(self, variable=self.one_time)
        self.once.grid(row=50, column=1)
    
    # Override
    def make_widgets(self):
        pass
    
    # Override
    def get_data(self):
        self.data = {
            "once": self.one_time.get()
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
    
    #frame = EditInformFrame(root)
    frame = EditKillFrame(root)
    
    # button to test the get_data() method
    # should print a dictionary with any data that you enter
    get = tk.Button(frame, text="Print entries",
        command=lambda : print(frame.get_data()))
    get.grid()
    
    root.mainloop()