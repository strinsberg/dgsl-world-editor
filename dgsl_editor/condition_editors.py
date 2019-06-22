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
        self.atmos = info_widgets.InfoOption(self, "Atmosphere",
                                             self.obj['atmosphere'],
                                             gd.atmospheres)
        self.atmos.grid(row=5, sticky='we')

    def update(self):
        object_editors.ObjectEditor.update(self)
        self.obj['atmosphere'] = self.atmos.get()


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

        def listCommands(self, isSelect=False):
            return {
                'add': self.add,
                'remove': self.remove,
                'edit': self.edit,
            }

    commands = MockCommands()

    fact = game_object_factory.GameObjectFactory()
    atmos = fact.make('protected', {'name': 'atmos', 'verb': 'use'})
    has = fact.make('hasItem', {'name': 'has', 'verb': 'use'})
    question = fact.make('question', {'name': 'question', 'verb': 'use'})

    # Create and run
    root = tk.Tk()

    atmos_edit = ProtectedEditor(root, atmos, commands)
    atmos_edit.grid(row=0)

    has_edit = HasItemEditor(root, has, commands)
    has_edit.grid(row=1)

    question_edit = QuestionEditor(root, question, commands)
    question_edit.grid(row=2)

    root.mainloop()

    # Test get
    print(atmos_edit.get())
    print(has_edit.get())
    print(question_edit.get())