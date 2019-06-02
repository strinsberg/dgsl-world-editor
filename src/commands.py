from TypeSelector import TypeSelector

class Command:
    def __init__(self, editor):
        self.editor = editor
    def execute(self, arg=None):
        assert False, "Command execute must be overridden"

class AddObj(Command):
    def execute(self, kind):
        dialog = TypeSelector(self.editor, kind)
        obj = dialog.getResult()
        if obj:
            self.editor.world.addObject(obj)
            return obj

class SelectObj(Command):
    def execute(self, kind):
        print(kind)

class EditObj(Command):
    def execute(self, ID):
        self.editor.editNew(ID)

class RemoveObj(Command):
    def execute(self, ID):
        self.editor.world.removeObject(ID)

class Commands:
    def __init__(self, editor):
        self.add = AddObj(editor)
        self.remove = RemoveObj(editor)
        self.edit = EditObj(editor)
        self.select = SelectObj(editor)
    
    def listCommands(self, isSelect=False):
        return{
            'add': self.add if not isSelect else self.select,
            'remove': self.remove,
            'edit': self.edit,
        }