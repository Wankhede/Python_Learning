# Widget is short for window gadget

import sys
import tkinter

# root_window = tkinter.Tk()
# root_window.title("Hello Swapnil in GUI")
# widget_control = tkinter.Label(root_window)
# widget_control.configure(text="Hiiiiiiiiiiiiiiiiiii")
# root_window.mainloop()


root_win = tkinter.Tk()
root_win.title("Button play")

but_win = tkinter.Button(root_win)
but_win.configure(text="OK", command=sys.exit)
but_win.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.Y)
root_win.mainloop()

