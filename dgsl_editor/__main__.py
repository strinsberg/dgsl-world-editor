import tkinter as tk
from . import editor_frame as ef
from . import game_object_factory as gof
from . import game_world as gw

# create root window
root = tk.Tk()

# start app
root.resizable(False, False)
root.geometry("650x500")

world = gw.GameWorld()

frame = ef.EditorFrame(root, world)
frame.pack_propagate(0)
frame.pack(fill=tk.BOTH, expand=1)


# run loop
root.mainloop()
