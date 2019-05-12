from InfoFrame import InfoFrame
import tkinter as tk
from GameObjectFactory import GameObjectFactory


class InfoFrameFactory:
    def make(self, parent, obj):
        self.frame = InfoFrame(parent, obj)
        return self.frame
    
    # Entity Info ##############################################
    
    
    
    # Event Info ###############################################
    
    
    
    # Condition Info ###########################################
    
    
    
    # Game Info ################################################

# Testing ######################################################

if __name__=='__main__':
    root = tk.Tk()
    
    fact = GameObjectFactory()
    obj = fact.make("entity")
    obj["name"] = "Test Entity"
    obj["description"] = "An entity that I am using for testing"
    
    frame = InfoFrameFactory().make(root, obj)
    frame.pack()
    
    root.mainloop()