from InfoFrame import InfoFrame
import game_data as gd
import tkinter as tk
from GameObjectFactory import GameObjectFactory


class InfoFrameFactory:
    def make(self, parent, obj):
        self.obj = obj
        self.frame = InfoFrame(parent, obj)
        
        kind = obj["type"]
        if kind in gd.entities:
            self.makeEntity()
        elif kind is "inform":
            self.makeInform()
        elif kind is "kill":
            self.makeKill()
        elif kind is "toggle":
            self.makeToggle()
        elif kind is "transfer":
            self.makeTransfer()
        elif kind is "move":
            self.makeMove()
        elif kind in ["group", "ordered"]:
            self.makeGroup()
        elif kind is "interaction":
            self.makeInteraction()
        elif kind is "conditional":
            self.makeConditional()
        elif kind is "hasItem":
            self.makeHasItem()
        elif kind is "protected":
            self.makeProtected()
        elif kind is "question":
            self.makeQuestion()
        else:
            return None
        
        return self.frame
    
    # Entity Info ##############################################
    
    def makeEntity(self):
        self.frame.addLabel("Description", "description")
        if self.obj["type"] is not "room":
            self.frame.addLabel("Active", "active")
            self.frame.addLabel("Obtainable", "obtainable")
            self.frame.addLabel("Hidden", "hidden")
    
    
    # Event Info ###############################################
    
    def makeEvent(self):
        self.frame.addLabel("One Time", "once")
        if "verb" in self.obj:
            self.frame.addLabel("Verb", "verb")
    
    def makeInform(self):
        self.frame.addLabel("Message", "message")
        self.makeEvent()
    
    def makeKill(self):
        self.makeInform()
        self.frame.addLabel("Ending", "ending")
    
    def makeTransfer(self):
        self.frame.addLabel("Give", "toTarget")
        self.makeEvent()
        self.frame.addPicker("Item", "item", "entity")
        self.frame.addPicker("Other", "other", "container")
        
    
    def makeToggle(self):
        self.makeEvent()
        self.frame.addPicker("Target", "target", "entity")
    
    def makeMove(self):
        self.makeEvent()
        self.frame.addPicker("Destination", "destination", "room")
    
    # Group Event Info #########################################
    
    def makeGroup(self):
        if self.obj["type"] is "ordered":
            self.frame.addLabel("Repeats", "repeats")
        self.makeEvent()
    
    def makeInteraction(self):
        self.frame.addLabel("Breakout", "breakout")
        self.makeEvent()
    
    def makeConditional(self):
        self.makeEvent()
        self.frame.addPicker("Condition", "condition", "condition")
        self.frame.addPicker("Success", "success", "event")
        self.frame.addPicker("Failure", "failure", "event")
        
    
    # Condition Info ###########################################
    
    def makeHasItem(self):
        self.frame.addPicker("Item", "item", "entity")
    
    def makeProtected(self):
        self.frame.addLabel("Atmosphere", "atmosphere")
    
    def makeQuestion(self):
        self.frame.addLabel("Question", "question")
        self.frame.addLabel("Answer", "answer")
    
    # Game Info ################################################
    
    def makeGame(self):
        pass

# Testing ######################################################

if __name__=='__main__':
    root = tk.Tk()
    
    fact = GameObjectFactory()
    obj = fact.make("hasItem")
    obj["name"] = "Test Entity"
    obj["description"] = "An entity that I am using for testing"
    
    frame = InfoFrameFactory().make(root, obj)
    frame.pack()
    
    root.mainloop()