from tkinter import *
root = Tk()

button = Button(root, text="Absolute Placement").place(x=20, y=10)
button2 = Button(root, text="Relative").place (
    relx=0.8, rely= 0.2, relwidth=0.5, width=10, anchor=NE)
root.mainloop()
