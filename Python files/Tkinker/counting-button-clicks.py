import tkinter as tk
window=tk.Tk()
count=0

def buttonClick():
    global count
    count=count+1
    print("Beep")
    button.config(text="Clicked")
    button.config(text=str(count))

entry=tk.Entry(window)

canvas=tk.Canvas(window, width=500, height=500)
canvas.pack()
canvas.create_line(0,0,500,500)    
button=tk.Button(window, text="Click Me!", command=buttonClick)
entry.pack()
button.pack()
window.mainloop()

