from tkinter import *
root = Tk()
label = Label(root, text="Username").grid(row=0, sticky=W)
label2 = Label(root, text="Password").grid(row = 1, sticky=W)
entry = Entry(root).grid(row = 0, column = 1, sticky = E)
entry2 = Entry(root).grid(row = 1, column = 1, sticky = E)
button = Button(root, text="Login").grid(row=2, column = 1, sticky = E)

root.mainloop()
