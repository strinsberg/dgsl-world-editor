import tkinter as tk
from . import info_widgets


class SimpleDialog(tk.Toplevel):
    """
    A base class for a dialog.
    
    Default has an OK and Cancel button that will be below whatever
    widgets are made with the overriden make_widgets() method.
    
    Allows for a result to be passed out from calling show()
    This result must be set in some function or it will return None
    
    Must override make_widgets() and apply()
    TODO: make it so validate is used in apply.
    
    Code mostly obtained from
        http://effbot.org/tkinterbook/tkinter-dialog-windows.htm
    
    """

    def __init__(self, parent, title=""):
        tk.Toplevel.__init__(self, parent)
        self.transient(parent)
        self.title = title

        self.result = None

        self.parent = parent
        body = tk.Frame(self)
        if title != "":
            tk.Label(body, text=title).pack()
        self.makeWidgets(body)
        body.pack()
        self.makeButtons()

        self.initial_focus = self

        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.initial_focus.focus_set()
        self.wait_window(self)

    # Can be called on the Window object to store result
    # dialog = SimpleDialog(root, "Title")
    # result = dialoge.get_result()
    def getResult(self):
        return self.result

    # Override to make widgets you want to appear above the buttons
    def makeWidgets(self, master):
        pass

    # Makes default OK and Cancel buttons
    # Override if you want custom buttons
    def makeButtons(self):
        box = tk.Frame(self)

        k = tk.Button(box,
                      text="OK",
                      width=10,
                      command=self.ok,
                      default=tk.ACTIVE)
        k.pack(side=tk.LEFT, padx=5, pady=5)

        c = tk.Button(box,
                      text="Cancel",
                      width=10,
                      command=self.cancel,
                      default=tk.ACTIVE)
        c.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    # Runs apply and closes the dialog
    # TODO: validate is not used yet
    # Default callback to OK button
    def ok(self, event=None):
        if not self.validate():
            SimpleDialog(self, "Incomplete Form")
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        #seperate from cancel so overriding it does not affect OK
        self.parent.focus_set()
        self.destroy()

    # Sets focus back to parent and closes window
    # Default callback for Cancel
    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()

    # Override if input needs validation
    # default is True
    def validate(self):
        return True

    # Override to determine what happens
    # If you want data passed out store it in self.result
    def apply(self):
        self.result = True


class EntryDialog(SimpleDialog):
    def makeWidgets(self, master):
        SimpleDialog.makeWidgets(self, master)
        self.name = info_widgets.InfoEntry(master, '', '')
        self.name.pack()

    def validate(self):
        if self.name.get() == '':
            return False
        return True

    def apply(self):
        self.result = self.name.get()


'''
# Main for Testing ################################################


class TestDialog(SimpleDialog):
    def apply(self):
        self.result = "Return the result"


if __name__ == "__main__":

    root = tk.Tk()

    dialog = TestDialog(root, "Test")
    result = dialog.getResult()

    root.mainloop()

    # Run a simple test to make sure that apply and get_result
    # are working. The test will fail if you press Cancel button.
    # Test won't run until root window is closed.
    assert result == "Return the result", "Failed: get_result.\nExpected: {}\nActual: {}".format(
        "Return the result", result)
'''