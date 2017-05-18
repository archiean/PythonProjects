import tkinter as tk
t=tk.Tk()
import time
canvas=tk.Canvas(t,width=400,height=400)
canvas.create_polygon(10,10,10,60,50,35)
canvas.pack()
for x in range(0,35):

   canvas.move(1,5,0)
   t.update()
   time.sleep(0.05)
for x in range(0,14):
    canvas.move(1,0,10)
    t.update()
    time.sleep(0.05)

for x in range(0,35):
    canvas.move(1,-10,0)
    t.update()
    time.sleep(0.05)

for x in range(0,14):
    canvas.move(1,0,-10)
    t.update()
    time.sleep(0.05)
