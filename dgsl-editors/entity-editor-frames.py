import EditEntityFrame as ef
import tkinter as tk

# Atmosphere #######################################################

class EditAtmosphereFrame(ef.EditEntityFrame):
    
    # Adds an atmosphere feild
    # not sure if this should be a forced choice or leave it as
    # a string. Only 3 types right now.
    def make_info(self):
        ef.EditEntityFrame.make_info(self)
        tk.Label(self, text="Atmosphere:").grid(row=5)
        
        self.atmos = tk.Entry(self)
        self.atmos.grid(row=5, column=1)
    
    #
    def get_data(self):
        ef.EditEntityFrame.get_data(self)
        self.data["atmoshpere"] = self.atmos.get()
        return self.data


# Room ##############################################################

class EditRoomFrame(EditAtmosphereFrame):
    def make_obtainable(self):
        self.obtainable = None


# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    #frame = EditAtmosphereFrame(root)
    #frame = EditRoomFrame(root)

    
    # button to test the get_data() method
    # should print a dictionary with any data that you enter
    get = tk.Button(frame, text="Print entries",
        command=lambda : print(frame.get_data()))
    get.grid()
    
    root.mainloop()