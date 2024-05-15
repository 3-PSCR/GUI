import threading

import interface

#Set frame dimensions
x = 1000
y = 650

gui = interface.GUISet(x, y)

# Offload updating the GUI to a separate thread (so that the buttons remain clickable)
get_thread = threading.Thread(target=gui.update, args=())
get_thread.start()

# gui.provide(board.seg())
gui.window.mainloop()
