from tkinter import *
parent= Tk()
parent.title("Find & Replace")

label = Label(parent, text="Find:").grid(row = 0, column = 0, sticky='e')
entry = Entry(parent, width=60).grid(row=0, column = 1,
                                     padx=2, pady= 2, sticky='we', columnspan=9)
label2 = Label(parent, text="Replace").grid(row= 1,column = 0, sticky = 'e')
entry = Entry(parent, width=60).grid(row = 0, column = 1,padx= 2,pady= 2,
                                     sticky='we', columnspan = 9)
button = Button(parent,text = "Find").grid(
    row = 0,column = 10,sticky='e' + 'w', padx = 2, pady=2)
button2 = Button(parent, text="Find All").grid(
    row = 1, column=10, sticky = 'e'+ 'w', padx = 2)
replace = Button(parent, text="Replace").grid(row = 2, column = 10, sticky = 'e'
                                              + 'w', padx = 2)
replaceall = Button(parent, text="Replace All").grid(row= 3, column = 10, sticky
                                                     = 'e' + 'w', padx= 2)
checkbutton = Checkbutton(parent, text="Match whole word only").grid(
    row = 2, column = 1, columnspan = 4, sticky = 'w')
matchcase = Checkbutton(parent, text="Match Case").grid(
    row = 3, column = 1, columnspan = 4, sticky = 'w')
wraparound = Checkbutton(parent, text="Wrap Around").grid(
    row = 4, column = 1, columnspan = 4, sticky = 'w')
direction = Label(parent, text="Direction").grid(row = 2, column = 6, sticky='w')
up = Radiobutton(parent,text="Up", value=1).grid(
    row = 3, column = 6, columnspan = 6, sticky = 'w')
down = Radiobutton(parent,text="Down", value =2 ).grid(
    row = 3, column = 7, columnspan = 2, sticky  = 'e')
parent.mainloop()
