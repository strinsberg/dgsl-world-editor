import object_editors as ed
import game_data as gd
import tkinter as tk

class ObjectEditorFactory:
    
    def make(parent, obj={}, commands={}):
        
        kind = None if 'type' not in obj else obj['type']
        if kind in gd.entities:
            w = ed.EntityEditor(parent, obj, commands)
        elif kind == "inform":
            w = ed.InformEditor(parent, obj, commands)
        elif kind == "kill":
            w = ed.KillEditor(parent, obj, commands)
        elif kind == "toggle":
            w = ed.ToggleEditor(parent, obj, commands)
        elif kind == "transfer":
            w = ed.TransferEditor(parent, obj, commands)
        elif kind == "move":
            w = ed.MoveEditor(parent, obj, commands)
        elif kind in ["group", "ordered"]:
            w = w = ed.GroupEditor(parent, obj, commands)
        elif kind == "interaction":
            w = ed.InteractionEditor(parent, obj, commands)
        elif kind == "conditional":
            w = ed.ConditionalEditor(parent, obj, commands)
        elif kind == "hasItem":
            w = ed.HasItemEditor(parent, obj, commands)
        elif kind == "protected":
            w = ed.ProtectedEditor(parent, obj, commands)
        elif kind == "question":
            w = ed.QuestionEditor(parent, obj, commands)
        else:
            w = tk.Label(parent, text="Please select an object to edit")
        
        return w