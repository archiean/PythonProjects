from tkinter import *
parent = Tk()

button1 = Button(parent, text="ALL IS WELL").pack(fill=X)
button2 = Button(parent, text="BACK TO BASICS").pack(fill=X)
button3 = Button(parent, text="CATCH ME IF YOU CAN").pack(fill = X)

button4 = Button(parent, text="LEFT").pack(side=LEFT)
button5 = Button(parent, text="CENTER").pack(side=LEFT)
button6= Button(parent, text="RIGHT").pack(side=LEFT)
parent.pack()

parent.mainloop()
