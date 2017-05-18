import tkinter as tk
t=tk.Tk()

def Changestring():
    str1=entry.get()
    str1=str1[::-1]
    entry.delete(0,tk.END)
    entry.insert(0,str1)
  

button=tk.Button(t, text="Click me", command=Changestring)
button.pack()
entry=tk.Entry(t)
entry.pack()

t.mainloop()
