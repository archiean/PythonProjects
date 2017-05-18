import tkinter as tk
t=tk.Tk()

import random
w=400
h=400

canvas=tk.Canvas(t,width=w,height=h)
canvas.pack()
colors=["green","blue","yellow","red","purple"]
def random_triangle():
    p1=random.randrange(w)
    p2=random.randrange(h)
    p3=random.randrange(w)
    p4=random.randrange(h)
    p5=random.randrange(w)
    p6=random.randrange(h)
    color=random.choice(colors)
    canvas.create_polygon(p1,p2,p3,p4,p5,p6,fill=color,outline="black")

for x in range(0,100):
    random_triangle()
