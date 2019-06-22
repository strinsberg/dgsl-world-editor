import tkinter as tk
import dgsl_editor.editor_frame as ef
import dgsl_editor.game_object_factory as gof
import dgsl_editor.game_world as gw

# create root window
root = tk.Tk()

# start app
root.resizable(False, False)
root.geometry("600x420")

fact = gof.GameObjectFactory()
room = fact.make('room', {'name': 'captains room'})

world = gw.GameWorld()
world.addObject(room)

frame = ef.EditorFrame(root, world)
frame.pack_propagate(0)
frame.pack(fill=tk.BOTH, expand=1)


# run loop
root.mainloop()
