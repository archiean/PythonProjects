from tkinter import *
root = Tk()

frame = Frame(root)
label = Label(frame, text="Pack Demo of side and fill").pack()
button = Button(frame, text="A").pack(side=LEFT, fill=Y)
button2 = Button(frame, text="B").pack(side=TOP, fill=X)
button3 = Button(frame, text="C").pack(side=RIGHT, fill=NONE)
button4 = Button(frame, text="D").pack(side=TOP, fill=BOTH)
frame.pack()

label = Label(root, text="Pack Demo of expand").pack()
button5 = Button(root,text="I do not expand").pack()
button6 = Button(root, text=" I don not fill X but I expand").pack(expand = 1)
button7 = Button(root, text="I fill X and expand").pack(fill=X, expand =1)
root.mainloop()
