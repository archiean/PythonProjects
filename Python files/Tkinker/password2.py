from tkinter import *
parent = Tk()

#adding widgets

label = Label(parent, text="Enter your Password")
button = Button(parent, text="Search")
checkbutton = Checkbutton(parent, text ="Remember Me")
entry = Entry(parent, width=30)
radiobutton = Radiobutton(parent, text="Male")
radiobutton2 = Radiobutton(parent,text="Female")
optionmenu = OptionMenu(parent, "Select Country", "USA","UK", "Singapore","Others")
scrollbar = Scrollbar(parent)

label.pack()
button.pack()
checkbutton.pack()
radiobutton.pack()
radiobutton2.pack()
optionmenu.pack()
scrollbar.pack()

parent.mainloop()
