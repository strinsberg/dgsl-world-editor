import EditEntityFrame as ef
import tkinter as tk

# Atmosphere #######################################################

class EditAtmosphereFrame(ef.EditEntityFrame):
    
    # Adds an atmosphere feild
    # not sure if this should be a forced choice or leave it as
    # a string. Only 3 types right now.
    def make_info(self):
        ef.EditEntityFrame.make_info(self)
        tk.Label(self, text="Atmosphere:").grid(row=10)
        
        self.atmos = tk.Entry(self)
        self.atmos.grid(row=10, column=1)
    
    #
    def get_data(self):
        ef.EditEntityFrame.get_data(self)
        self.data["atmoshpere"] = self.atmos.get()
        return self.data


# Room ############################################################

class EditRoomFrame(EditAtmosphereFrame):
    def make_obtainable(self):
        self.obtainable = None

# Npc #############################################################

class EditNpcFrame(ef.EditEntityFrame):
    def make_obtainable(self):
        self.obtainable = None

# Door ############################################################

class EditDoorFrame(EditNpcFrame):
    
    # Adds destination field
    # not sure exactly how to do this with ID's and such
    # I think probably give the room name and then use
    # validate to make sure that it exists before it let's
    # you move on. Or give a list box with rooms before or
    # after to select the room it will lead to.
    def make_info(self):
        ef.EditEntityFrame.make_info(self)
        tk.Label(self, text="Destination:").grid(row=10)
        
        self.dest = tk.Entry(self)
        self.dest.grid(row=10, column=1)
    
    #
    def get_data(self):
        ef.EditEntityFrame.get_data(self)
        self.data["destination"] = self.dest.get()
        return self.data


# Testing #########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    frame = EditAtmosphereFrame(root)
    #frame = EditRoomFrame(root)
    #frame = EditNpcFrame(root)
    #frame = EditDoorFrame(root)
    
    # button to test the get_data() method
    # should print a dictionary with any data that you enter
    get = tk.Button(frame, text="Print entries",
        command=lambda : print(frame.get_data()))
    get.grid()
    
    root.mainloop()