import tkinter as tk
import time

t=tk.Tk()
clicks=0
start=0
goal=10

def buttonClick():
    global clicks
    global start
    global goal

    if clicks ==1:
        start=time.time()
        clicks=clicks+1
    elif clicks==10:
        score=time.time()
        label.config(text="Time:" + str(score))
        clicks=0
    else:
        clicks=clicks+1
    slider.set(clicks)

button=tk.Button(t, text="Click me", command=buttonClick)
slider=tk.Scale(t, from_=0, to=goal)
label=tk.Label(t)

button.pack()
slider.pack()
label.pack()

t.mainloop()
