from InfoEditor import InfoEditor


class InfoEditorFactory:
    def make(self, parent, obj):
        self.obj = obj
        self.widget_info = []
        
        # here goes the if/elif/else to decide what
        # kind of editor to make
        # the other methods will add what they need to to
        # dict and add those info objects to self.widget_info
        
        return InfoEditor(parent, self.obj, self.widget_info)
    
    # Entities #################################################
    
    
    # Events ###################################################
    
    
    # Conditions ###############################################
    
    
    # Game #################################################