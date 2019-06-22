import tkinter as tk
from . import simple_dialog
from . import game_object_factory
from . import game_data as gd


class TypeSelector(simple_dialog.SimpleDialog):
    def __init__(self, parent, kind, has_verb=False):
        self.kind = kind
        self.has_verb = has_verb
        simple_dialog.SimpleDialog.__init__(self, parent)

    def makeWidgets(self, master):
        tk.Label(master, text="Type:").grid(row=0, sticky=tk.W)
        self.choice = tk.StringVar(master)

        if self.kind == "entity":
            self.choice.set(gd.room_entities[0])
            self.menu = tk.OptionMenu(*(
                (master, self.choice) + tuple(gd.room_entities)))
        elif self.kind == "event":
            self.choice.set(gd.events[0])
            self.menu = tk.OptionMenu(*(
                (master, self.choice) + tuple(gd.events)))
        elif self.kind == "condition":
            self.choice.set(gd.conditions[0])
            self.menu = tk.OptionMenu(*(
                (master, self.choice) + tuple(gd.conditions)))
        else:
            self.menu = tk.Label(master, text=self.kind)

        self.menu.grid(row=0, column=1)

        tk.Label(master, text="Name:").grid(row=5)
        self.name = tk.Entry(master)
        self.name.grid(row=5, column=1)

        if self.has_verb:
            tk.Label(master, text="Verb:").grid(row=10)
            self.verb = tk.Entry(master)
            self.verb.grid(row=10, column=1)

    def validate(self):
        if self.name.get() == "":
            return False
        else:
            return True

    def apply(self):
        fact = game_object_factory.GameObjectFactory()
        choice = self.choice.get()
        kind = choice if choice else self.kind
        self.result = fact.make(kind)
        self.result["name"] = self.name.get()
        try:
            self.result['verb'] = self.verb.get()
        except AttributeError:
            pass
