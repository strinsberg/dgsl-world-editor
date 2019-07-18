import tkinter as tk
from . import object_editors
from . import info_widgets
from . import object_lists


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


class TransferEditor(object_editors.EventEditor):
    def makeWidgets(self):
        super(TransferEditor, self).makeWidgets()
        self.item = info_widgets.InfoSelector(
            self, "Item", self.obj['item'], 'entity',
            self.commands.makeSelect(self.validate), self.commands.edit)
        self.item.grid(row=10, sticky='we')

        if self.obj['type'] == 'take':
            owner_label = 'New Owner'
            owner = self.obj['new_owner']
        else:
            owner_label = 'Item Owner'
            owner = self.obj['item_owner']

        self.owner = info_widgets.InfoSelector(
            self, owner_label, owner, 'entity', self.commands.makeSelect(self.validate), self.commands.edit)
        self.owner.grid(row=15, sticky='we')

    def validate(self, obj):
        if (not super(TransferEditor, self).validate(obj)
                or obj['type'] in ['player', 'room']):
            return False
        return True

    def update(self):
        super(TransferEditor, self).update()
        self.obj['item'] = self.item.get()
        owner_type = 'item_owner' if self.obj['type'] == 'give' else 'new_owner'
        self.obj[owner_type] = self.owner.get()


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


class InteractionEditor(object_editors.EventEditor):
    def makeWidgets(self):
        object_editors.EventEditor.makeWidgets(self)
        self.repeats = info_widgets.InfoCheck(self, "Breakout",
                                              self.obj['breakout'])
        self.repeats.grid(row=5, sticky='we')

    def makeRightList(self):
        self.right = None
        self.right = object_lists.ObjectListWithEdit(
            self.lists, self.obj['options'], "Options", 'option',
            self.commands.addList())
        self.right.pack(side=tk.LEFT, anchor='w', fill=tk.Y, expand=1)

    def update(self):
        object_editors.EventEditor.update(self)
        self.obj['options'] = self.right.get()
        self.obj['breakout'] = self.repeats.get()


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
                                              self.commands.edit,
                                              full_obj_info=True)
        self.fail.grid(row=7, sticky='we')

    def update(self):
        object_editors.EventEditor.update(self)
        self.obj['condition'] = self.cond.get()
        self.obj['success'] = self.succ.get()
        self.obj['failure'] = self.fail.get()
