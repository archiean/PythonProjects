import tkinter as tk
t=tk.Tk()
counter=0
def buttonclick():
    global counter
    counter=counter+1
    print("beep")
    button.config(text=str(counter))
def changeString():
    Text=entry.get()
    entry.insert(0,Text)
    
canvas=tk.Canvas(t,width=500, height=100)
canvas.pack()
button=tk.Button(t, text="Click me", command=changeString)
button.pack()
entry=tk.Entry(t)
entry.pack()


t.mainloop()

