import tkinter as tk
t=tk.Tk()

entry1=tk.Entry(t)
entry2=tk.Entry(t, show="*")
Label1=tk.Label(t, text="Username")
Label2=tk.Label(t, text="Password")
canvas=tk.Canvas(t)
tk.Entry(t).grid(row=2, column=2) #can also be typed this way
entry2.grid(row=1, column=2)
Label1.grid(row=1, column=1,sticky="n")
Label2.grid(row=2, column=1, sticky="n")

t.mainloop()
