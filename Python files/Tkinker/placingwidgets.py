from tkinter import *
parent = Tk()

button = Button(parent, text="ALL IS WELL").pack(fill=X)
button2 = Button(parent, text="BACK TO BASICS").pack(fill=X)
button3 = Button(parent, text="CATCH ME IF YOU CAN").pack(fill = X)

sidd = Button(parent, text="LEFT").pack(side=LEFT)
code = Button(parent, text="CENTER").pack(side=LEFT)
app = Button(parent, text="RIGHT").pack(side=LEFT)
parent.pack()

parent.mainloop()
