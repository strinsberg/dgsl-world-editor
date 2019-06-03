from object_editors import *
from event_editors import *
from condition_editors import *
import game_data as gd
import tkinter as tk

class ObjectEditorFactory:
    
    def make(self, parent, obj=None, commands=None):
        if obj is None:
            return NullEditor(parent)
            
        kind = obj['type']
        if kind == 'player':
            w = PlayerEditor(parent, obj, commands)
        elif kind in gd.entities:
            w = EntityEditor(parent, obj, commands)
        elif kind == "inform":
            w = InformEditor(parent, obj, commands)
        elif kind == "kill":
            w = KillEditor(parent, obj, commands)
        elif kind == "toggle":
            w = ToggleEditor(parent, obj, commands)
        elif kind == "transfer":
            w = TransferEditor(parent, obj, commands)
        elif kind == "move":
            w = MoveEditor(parent, obj, commands)
        elif kind in ["group", "ordered", 'interaction']:
            w = GroupEditor(parent, obj, commands)
        elif kind == "conditional":
            w = ConditionalEditor(parent, obj, commands)
        elif kind == "hasItem":
            w = HasItemEditor(parent, obj, commands)
        elif kind == "protected":
            w = ProtectedEditor(parent, obj, commands)
        elif kind == "question":
            w = QuestionEditor(parent, obj, commands)
        
        return w