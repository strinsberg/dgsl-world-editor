"""
A menu bar for the world editor
"""
import tkinter as tk
import os
from . import game_world
from . import simple_dialog


class MenuBar(tk.Frame):
    """A MenuBar for the world editor"""

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.editor = parent
        self.make_widgets()

    # could set commands to methods so that they can update and
    # set messages etc.
    def make_widgets(self):
        """Creates widgets"""
        self.world = tk.Button(self,
                               text="World",
                               command=self.editor.editWorld)
        self.world.pack(side=tk.LEFT)

        self.player = tk.Button(
            self,
            text="Player",
            command=lambda: self.editor.editNew(self.editor.world.player))
        self.player.pack(side=tk.LEFT)

        self.back = tk.Button(self, text="Back", command=self.editor.editLast)
        self.back.pack(side=tk.LEFT)

        self.title = tk.StringVar()
        self.title.set(self.editor.world.name)
        self.title_bar = tk.Label(self, textvariable=self.title)
        self.title_bar.pack(side=tk.LEFT, expand=1, fill=tk.X)

        self.load_button = tk.Button(self, text="Load", command=self.load)
        self.load_button.pack(side=tk.RIGHT)

        self.save_button = tk.Button(self, text="Save", command=self.save)
        self.save_button.pack(side=tk.RIGHT)

    def load(self):
        """Load a world"""
        dialog = simple_dialog.EntryDialog(self, "Enter world name")
        result = dialog.getResult()
        if result:
            world_name = result
        else:
            return
        world = game_world.GameWorld()
        world.load(world_name)
        self.editor.loadWorld(world)
        self.set_title(world.name)
        self.editor.setMessage("Loaded: " + world.name)

    def save(self):
        """Save the editors current world"""
        if self.editor.world.name == 'untitled':
            entry = simple_dialog.EntryDialog(self,
                                              "Please choose a world name")
            result = entry.getResult()
            if result:
                self.editor.world.changeName(result)
                self.set_title(result)
            else:
                return

        if (self.editor.world.first_save
                and self.editor.world.filename() in os.listdir('saves')):
            dialog = simple_dialog.SimpleDialog(
                self, ("Do you really want to save? \nWorld already exists! "
                       "Saving will overwrite it. \nThere will be no more "
                       "Reminders\nCancel and rename world if you don't want"
                       "this to happen"))
            if not dialog.getResult():
                return

        self.editor.update()
        self.editor.world.save()
        self.set_title(self.editor.world.name)
        self.editor.setMessage("Saved")

    def set_title(self, title):
        """Sets the title"""
        self.title.set(title)

    def editing(self):
        """Shows that the world is being edited"""
        self.set_title("** " + self.editor.world.name + " **")


# Testing ######################################################

if __name__ == '__main__':
    ROOT = tk.Tk()

    FRAME = MenuBar(ROOT)
    FRAME.pack()

    ROOT.mainloop()
