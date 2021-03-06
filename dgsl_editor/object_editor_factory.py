import tkinter as tk
from . import object_editors
from . import event_editors
from . import condition_editors
from . import game_data as gd


class ObjectEditorFactory:
    def make(self, parent, obj=None, commands=None):
        if obj is None:
            return object_editors.NullEditor(parent)

        kind = obj['type']
        if kind == 'player':
            w = object_editors.PlayerEditor(parent, obj, commands)
        elif kind == 'equipment':
            w = object_editors.EquipmentEditor(parent, obj, commands)
        elif kind in gd.entities:
            w = object_editors.EntityEditor(parent, obj, commands)
        elif kind in ['event', 'end_game']:
            w = object_editors.EventEditor(parent, obj, commands)
        elif kind in ["toggle_active", "toggle_obtainable", "toggle_hidden"]:
            w = event_editors.ToggleEditor(parent, obj, commands)
        elif kind in ['give', 'take']:
            w = event_editors.TransferEditor(parent, obj, commands)
        elif kind == "move":
            w = event_editors.MoveEditor(parent, obj, commands)
        elif kind in ["group", "ordered"]:
            w = object_editors.EventEditor(parent, obj, commands)
        elif kind == 'interaction':
            w = event_editors.InteractionEditor(parent, obj, commands)
        elif kind == "conditional":
            w = event_editors.ConditionalEditor(parent, obj, commands)
        elif kind == "hasItem":
            w = condition_editors.HasItemEditor(parent, obj, commands)
        elif kind == "protected":
            w = condition_editors.ProtectedEditor(parent, obj, commands)
        elif kind == "question":
            w = condition_editors.QuestionEditor(parent, obj, commands)
        elif kind == "is_active":
            w = condition_editors.IsActiveEditor(parent, obj, commands)
        elif kind in ['option', 'conditional_option']:
            w = condition_editors.OptionEditor(parent, obj, commands)
        else:
            raise AttributeError("No editor type: " + kind)

        return w
