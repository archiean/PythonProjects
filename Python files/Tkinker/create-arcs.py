import tkinter as tk
t=tk.Tk()

canvas=tk.Canvas(t,bg="green",width=300,height=300)
coord=10,240,200,320
canvas.create_arc(coord, start=0,extent=180,fill="red")
canvas.create_arc(coord, start=120,extent=180,fill="red")
canvas.create_arc(coord, start=-120,extent=180,fill="red")

canvas.create_arc(coord,extent=180,fill="red")
canvas.pack()
