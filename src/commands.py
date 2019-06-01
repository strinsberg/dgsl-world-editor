from TypeSelector import TypeSelector

class Command:
    def execute(self, arg=None):
        assert False, "Command execute must be overridden"

class AddObj(Command):
    def __init__(self, editor, kind):
        self.editor = editor
        self.kind = kind
        
    def execute(self, kind):
        dialog = TypeSelector(self.editor, self.kind)
        obj = dialog.getResult()
        self.editor.world.addObject(obj)
        return obj

class EditObj:
    def execute(self, obj):
        print(obj)

class RemoveObj:
    def execute(self, obj):
        print(obj)