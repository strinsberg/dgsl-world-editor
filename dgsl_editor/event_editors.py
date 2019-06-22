import tkinter as tk
from . import object_editors
from . import info_widgets


class InformEditor(object_editors.EventEditor):
    def makeWidgets(self):
        object_editors.EventEditor.makeWidgets(self)
        self.message = info_widgets.InfoEntry(self, "Message",
                                              self.obj['message'])
        self.message.grid(row=5, sticky='we')

    def update(self):
        object_editors.EventEditor.update(self)
        self.obj['message'] = self.message.get()


class KillEditor(InformEditor):
    def makeWidgets(self):
        InformEditor.makeWidgets(self)
        self.ending = info_widgets.InfoCheck(self, "Ending",
                                             self.obj['ending'])
        self.ending.grid(row=11, sticky='we')

    def update(self):
        InformEditor.update(self)
        self.obj['ending'] = self.ending.get()


class ToggleEditor(object_editors.EventEditor):
    def makeWidgets(self):
        object_editors.EventEditor.makeWidgets(self)
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


# Testing ######################################################
if __name__ == '__main__':
    from . import game_object_factory

    # Testing objects
    class MockCommand:
        def execute(self, arg):
            print(arg)

    class AddCommand:
        def execute(self, arg):
            return {'name': 'A new name', 'id': '3rh2ih3r2foi2'}

    class MockCommands:
        def __init__(self):
            self.add = AddCommand()
            self.remove = MockCommand()
            self.edit = MockCommand()
            self.select = MockCommand()

        def addList(self, isSelect=False):
            return {
                'add': self.add,
                'remove': self.remove,
                'edit': self.edit,
            }

        def makeSelect(self, obj, validate=None):
            return self.add

        def selectList(self, obj, validate=None):
            return {
                'add': self.add,
                'remove': self.remove,
                'edit': self.edit,
            }

    commands = MockCommands()

    fact = game_object_factory.GameObjectFactory()
    inf = fact.make('inform', {'name': 'inform', 'verb': 'use'})
    kill = fact.make('kill', {'name': 'kill', 'verb': 'use'})
    toggle = fact.make('toggle', {'name': 'toggle', 'verb': 'use'})
    transfer = fact.make('transfer', {'name': 'transfer', 'verb': 'use'})

    move = fact.make('move', {'name': 'move', 'verb': 'use'})
    ordered = fact.make('ordered', {'name': 'ordered', 'verb': 'use'})
    conditional = fact.make('conditional', {
        'name': 'conditional',
        'verb': 'use'
    })

    # Create and run
    root = tk.Tk()
    group = 2

    if group == 1:
        inform_edit = InformEditor(root, inf, commands)
        inform_edit.grid(row=0, column=1)

        kill_edit = KillEditor(root, kill, commands)
        kill_edit.grid(row=1, column=1)

        toggle_edit = ToggleEditor(root, toggle, commands)
        toggle_edit.grid(row=0)

        transfer_edit = TransferEditor(root, transfer, commands)
        transfer_edit.grid(row=1)

        root.mainloop()

        # Test get
        print(inform_edit.get())
        print(kill_edit.get())
        print(toggle_edit.get())
        print(transfer_edit.get())

    elif group == 2:
        move_edit = MoveEditor(root, move, commands)
        move_edit.grid(row=0, column=1)

        group_edit = GroupEditor(root, ordered, commands)
        group_edit.grid(row=1, column=1)

        cond_edit = ConditionalEditor(root, conditional, commands)
        cond_edit.grid(row=0)

        root.mainloop()

        # Test get
        print(move_edit.get())
        print(group_edit.get())
        print(cond_edit.get())