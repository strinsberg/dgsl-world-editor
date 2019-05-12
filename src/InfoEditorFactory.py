from InfoEditor import InfoEditor
import game_data as gd

class InfoEditorFactory:
    def make(self, parent, obj):
        self.obj = obj
        self.widget_info = []
        
        if gd.is_entity(self.obj):
            self.makeEntity()
        elif :
            pass
        # here goes the if/elif/else to decide what
        # kind of editor to make
        # the other methods will add what they need to to
        # dict and add those info objects to self.widget_info
        
        return InfoEditor(parent, self.obj, self.widget_info)
    
    # Entities #################################################
    
    def makeEntity(self):
        w = []
        w.append({"type": "entry", "label": "Description",
                "field": "description"})
        w.append({"type": "check", "label": "Active",
                "field": "active"})
        w.append({"type": "check", "label": "Obtainable",
                "field": "obtainable"})
        w.append({"type": "check", "label": "Hidden",
                "field": "Hidden"})
        self.widget_info.extend(w)
    
    # Events ###################################################
    
    def makeEvent(self):
        w = []
        w.append({"type": "check", "label": "One Time",
                "field": "once"})
        if "verb" in self.obj:
            w.append({"type": "option", "label": "Verb",
                "field":"verb", "options": gd.verbs})
        self.widget_info.extend(w)
    
    def makeInform(self):
        self.widget_info.append({"type": "entry", "label":
                "Message", "field": "message"})
        self.makeEvent()
    
    def makeKill(self):
        self.makeInform()
        self.widget_info.append({"type": "check", "label":
                "Ending", "field": "ending"})
    
    def makeToggle(self):
        self.makeEvent()
    
    def makeTransfer(self):
        self.widget_info.append({"type": "check", "label": "Give",
                "field": "toTarget"})
        self.makeEvent()
    
    def makeMove(self):
        self.makeEvent()
    
    # Group Events #############################################
    
    def makeGroup(self):
        if "ordered" in self.obj:
            self.widget_info.append({"type": "check",
                "label": "Repeats", "field": "repeats"})
        self.makeEvent()
    
    def makeInteraction(self):
        self.widget_info.append({"type": "check",
                "label": "Breakout", "field": "breakout"})
        self.makeEvent()
    
    def makeConditional(self):
        self.makeEvent()
    
    # Conditions ###############################################
    
    def makeHasItem(self):
        pass
    
    def makeProtected(self):
        self.widget_info.append({"type": "option",
                "label": "Atmosphere", "field": "atmosphere",
                "options": gd.atmospheres})
    
    def makeQuestion(self):
        self.widget_info.append({"type": "entry",
                "label": "Question", "field": "question"})
        self.widget_info.append({"type": "entry",
                "label": "Answer", "field": "answer"})
    
    # Game #####################################################
    
    def makeGame(self):
        pass
        # Don't know what goes in here yet