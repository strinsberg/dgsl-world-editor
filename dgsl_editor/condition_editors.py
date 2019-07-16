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


class OptionEditor(object_editors.ObjectEditor):
    def __init__(self, parent, obj, commands):
        self.commands = commands
        self.condition = False
        if obj['type'] == 'conditional_option':
            self.condition = True
        object_editors.ObjectEditor.__init__(self, parent, obj)

    def makeWidgets(self):
        super(OptionEditor, self).makeWidgets()
        self.text = info_widgets.InfoEntry(self, "Menu Text", self.obj['text'])
        self.text.grid(row=10, sticky='we')
        self.event = info_widgets.InfoSelector(
            self, 'Event', self.obj['event'], 'event',
            self.commands.add, self.commands.edit)

        if self.condition:
            self.cond = info_widgets.InfoSelector(
                self, "Condition", self.obj['condition'], 'condition',
                self.commands.add, self.commands.edit)
            self.cond.grid(row=15, sticky='we')

    def update(self):
        super(OptionEditor, self).update()
        self.obj['text'] = self.text.get()
        self.obj['event'] = self.event.get()

        if self.condition:
            self.obj['condition'] = self.event.get()
