import tkinter as tk

class Viewer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.make_widgets()
        # list of things we are editing
        # the current thing being edited
            # its info
            # its entities or subscritpions or events
        # previous thing edited
        
    
    def make_widgets(self):
        self.obj_list = None
        self.obj_viewer = None


# Testing ##########################################################

if __name__=='__main__':
    root = tk.Tk()
    
    root.mainloop()