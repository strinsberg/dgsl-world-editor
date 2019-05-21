from InfoFrame import InfoFrame
import game_data as gd
import tkinter as tk
from GameObjectFactory import GameObjectFactory


class InfoFrameFactory:
    def make(self, parent, obj):
        self.obj = obj
        self.frame = InfoFrame(parent, obj)
        
        kind = obj["type"]
        if kind == 'player':
            self.makePlayer()
        elif kind in gd.entities:
            self.makeEntity()
        elif kind == "inform":
            self.makeInform()
        elif kind == "kill":
            self.makeKill()
        elif kind == "toggle":
            self.makeToggle()
        elif kind == "transfer":
            self.makeTransfer()
        elif kind == "move":
            self.makeMove()
        elif kind in ["group", "ordered"]:
            self.makeGroup()
        elif kind == "interaction":
            self.makeInteraction()
        elif kind == "conditional":
            self.makeConditional()
        elif kind == "hasItem":
            self.makeHasItem()
        elif kind == "protected":
            self.makeProtected()
        elif kind == "question":
            self.makeQuestion()
        else:
            return None
        
        return self.frame
    
    # Player ###################################################
    
    def makePlayer(self):
        self.frame.addLabel("Ask For Name", "get_name")
        self.frame.addSelector("Starting Room", "start", 'room')
    
    # Entity Info ##############################################
    
    def makeEntity(self):
        self.frame.addLabel("Description", "description")
        if self.obj["type"] != "room":
            self.frame.addLabel("Active", "active")
            self.frame.addLabel("Obtainable", "obtainable")
            self.frame.addLabel("Hidden", "hidden")
        if self.obj["type"] == 'door':
            self.frame.addSelector("Destination", "destination", "room")
    
    
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
        self.frame.addSelector("Destination", "destination", "room")
    
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
        self.frame.addSelector("Condition", "condition", "condition", False)
        self.frame.addSelector("Success", "success", "event", False)
        self.frame.addSelector("Failure", "failure", "event", False)
        
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
    obj = fact.make("inform")
    obj["name"] = "Test Entity"
    obj["verb"] = "use"
    
    frame = InfoFrameFactory().make(root, obj)
    frame.pack()
    
    root.mainloop()