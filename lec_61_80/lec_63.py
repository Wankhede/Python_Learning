import tkinter

def main():
    root_window = tkinter.Tk()
    root_window.title("Hello GUI extented version")
    lable_window = tkinter.Label(root_window)
    lable_window.configure(text=f"Hello, Its open now!!!!!!!!!\n Swapnil")
    lable_window.pack(side = tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
    root_window.mainloop()

main()