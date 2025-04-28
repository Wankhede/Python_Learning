# boilerplate code

from logging import config
import tkinter

root_window = tkinter.Tk()
root_window.title("!!! GUI !!!!")

widget_lable = tkinter.Label(root_window)
widget_lable.configure(text="Hello GUI !!!")
widget_lable.pack(side=tkinter.TOP, expand=tkinter.YES, fill= tkinter.BOTH)
root_window.mainloop()