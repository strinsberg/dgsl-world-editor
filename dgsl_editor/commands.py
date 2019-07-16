from . import type_selector
from . import object_selector
from . import game_data as gd


class Command:
    def __init__(self, editor):
        self.editor = editor

    def execute(self, arg=None):
        assert False, "Command execute must be overridden"


class AddObj(Command):
    # add a has verb attribute that can be set
    # so that add does not always have to have a verb
    def execute(self, kind, old_id=None, is_selector=False):
        if (kind in gd.events or kind == 'event') and not is_selector:
            hasVerb = True
        else:
            hasVerb = False

        dialog = type_selector.TypeSelector(self.editor, kind, hasVerb)
        obj = dialog.getResult()
        if obj:
            self.editor.world.addObject(obj)
            if old_id is not None:
                self.editor.world.removeObject(old_id)
            return obj


class SelectAdd(Command):
    def __init__(self, editor, validate=None):
        Command.__init__(self, editor)
        self.validate = validate

    def execute(self, kind, is_selector=False):
        objects = self.editor.world.getObjects(kind)
        if self.validate:
            objects = [obj for obj in objects if self.validate(obj)]
        dialog = object_selector.ObjectSelector(self.editor, objects)
        obj = dialog.getResult()
        return obj


class SelectRemove(Command):
    def execute(self, kind):
        pass


class EditObj(Command):
    def execute(self, ID):
        self.editor.editNew(ID)


class RemoveObj(Command):
    def execute(self, ID):
        self.editor.world.removeObject(ID)
        # Dont just check if it was the last one
        # check if it still exists.
        if self.editor.obj_editor.obj['id'] == ID:
            self.editor.editLast()


class Commands:
    def __init__(self, editor):
        self.editor = editor
        self.add = AddObj(editor)
        self.remove = RemoveObj(editor)
        self.edit = EditObj(editor)

    def addList(self):
        return {
            'add': self.add,
            'remove': self.remove,
            'edit': self.edit,
        }

    def makeSelect(self, validate=None):
        return SelectAdd(self.editor, validate)

    def selectList(self, validate=None):
        return {
            'add': self.makeSelect(validate),
            'remove': SelectRemove(self.editor),
            'edit': self.edit,
        }