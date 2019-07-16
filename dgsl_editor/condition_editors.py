import tkinter as tk
from . import object_editors
from . import info_widgets
from . import game_data as gd


class HasItemEditor(object_editors.ObjectEditor):
    def __init__(self, parent, obj, commands):
        self.commands = commands
        object_editors.ObjectEditor.__init__(self, parent, obj)

    def makeWidgets(self):
        object_editors.ObjectEditor.makeWidgets(self)
        self.item = info_widgets.InfoSelector(
            self, "Item", self.obj['item'], 'entity',
            self.commands.makeSelect(self.validate), self.commands.edit)
        self.item.grid(row=5, sticky='we')
        self.other = info_widgets.InfoSelector(
            self, "Other", self.obj['other'], 'container',
            self.commands.makeSelect(self.validate), self.commands.edit)
        self.other.grid(row=6, sticky='we')

    def update(self):
        object_editors.ObjectEditor.update(self)
        self.obj['item'] = self.item.get()
        self.obj['other'] = self.other.get()


class QuestionEditor(object_editors.ObjectEditor):
    def __init__(self, parent, obj, commands):
        self.commands = commands
        object_editors.ObjectEditor.__init__(self, parent, obj)

    def makeWidgets(self):
        object_editors.ObjectEditor.makeWidgets(self)
        self.question = info_widgets.InfoEntry(self, "Question",
                                               self.obj['question'])
        self.question.grid(row=5, sticky='we')
        self.answer = info_widgets.InfoEntry(self, "Answer",
                                             self.obj['answer'])
        self.answer.grid(row=6, sticky='we')

    def update(self):
        object_editors.ObjectEditor.update(self)
        self.obj['question'] = self.question.get()
        self.obj['answer'] = self.answer.get()


class ProtectedEditor(object_editors.ObjectEditor):
    def __init__(self, parent, obj, commands):
        self.commands = commands
        object_editors.ObjectEditor.__init__(self, parent, obj)

    def makeWidgets(self):
        object_editors.ObjectEditor.makeWidgets(self)

        eff = 'enter effects as space separated list'
        if self.obj['effects']:
            eff = " ".join(self.obj['effects'])
        self.effects = info_widgets.InfoEntry(self, "Effects", eff)
        self.effects.grid(row=10, sticky='we')

    def update(self):
        object_editors.ObjectEditor.update(self)
        self.obj['effects'] = self.effects.get().split()
