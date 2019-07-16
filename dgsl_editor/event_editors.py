import tkinter as tk
from . import object_editors
from . import info_widgets


class ToggleEditor(object_editors.EventEditor):
    def makeWidgets(self):
        object_editors.EventEditor.makeWidgets(self)
        self.type = info_widgets.InfoLabel(
            self, "Toggle State", self.obj['state'])
        self.type.grid(row=0, sticky='we')
        self.target = info_widgets.InfoSelector(
            self, "Target", self.obj['target'], 'entity',
            self.commands.makeSelect(self.validate), self.commands.edit)
        self.target.grid(row=5, sticky='we')

    def validate(self, obj):
        if (not self.select(obj) or obj['type'] in ['player', 'room']):
            return False
        return True

    def update(self):
        object_editors.EventEditor.update(self)
        self.obj['target'] = self.target.get()


class TransferEditor(ToggleEditor):
    def makeWidgets(self):
        ToggleEditor.makeWidgets(self)
        self.target.kind = 'container'
        self.item = info_widgets.InfoSelector(
            self, "Item", self.obj['item'], 'entity',
            self.commands.makeSelect(self.validate), self.commands.edit)
        self.item.grid(row=6, sticky='we')
        self.to_target = info_widgets.InfoCheck(self, "To target",
                                                self.obj['toTarget'])
        self.to_target.grid(row=11, sticky='we')

    def update(self):
        ToggleEditor.update(self)
        self.obj['item'] = self.item.get()
        self.obj['toTarget'] = self.to_target.get()


class MoveEditor(object_editors.EventEditor):
    def makeWidgets(self):
        object_editors.EventEditor.makeWidgets(self)
        self.dest = info_widgets.InfoSelector(
            self, "Destination", self.obj['destination'], 'room',
            self.commands.makeSelect(self.select), self.commands.edit)
        self.dest.grid(row=5, sticky='we')

    def update(self):
        object_editors.EventEditor.update(self)
        self.obj['destination'] = self.dest.get()


class GroupEditor(object_editors.EventEditor):
    def makeWidgets(self):
        object_editors.EventEditor.makeWidgets(self)
        self.repeats = info_widgets.InfoCheck(self, "Repeats",
                                              self.obj['repeats'])
        self.repeats.grid(row=5, sticky='we')

    def update(self):
        object_editors.EventEditor.update(self)
        self.obj['repeats'] = self.repeats.get()


class ConditionalEditor(object_editors.EventEditor):
    def makeWidgets(self):
        object_editors.EventEditor.makeWidgets(self)
        self.cond = info_widgets.InfoSelector(self, "Condition",
                                              self.obj['condition'],
                                              'condition', self.commands.add,
                                              self.commands.edit)
        self.cond.grid(row=5, sticky='we')

        self.succ = info_widgets.InfoSelector(self, "Success",
                                              self.obj['success'], 'event',
                                              self.commands.add,
                                              self.commands.edit)
        self.succ.grid(row=6, sticky='we')

        self.fail = info_widgets.InfoSelector(self, "Failure",
                                              self.obj['failure'], 'event',
                                              self.commands.add,
                                              self.commands.edit)
        self.fail.grid(row=7, sticky='we')

    def update(self):
        object_editors.EventEditor.update(self)
        self.obj['condition'] = self.cond.get()
        self.obj['success'] = self.succ.get()
        self.obj['failure'] = self.fail.get()
