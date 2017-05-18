import tkinter as tk
t=tk.Tk()

canvas=tk.Canvas(t,bg="black",width=300,height=300)
canvas.create_polygon(10,10,100,10,100,100,fill="blue",outline="black")
canvas.create_oval(30,40,100,80,fill="red")
canvas.create_line(60,70,40,60,)
canvas.create_text(120,100,text="hello",font=("courier",30),fill="purple")
my_image=tk.PhotoImage(file="/Users/codingmagics1/Desktop/pygame_tiny.gif")
canvas.create_image(150,160,anchor="nw",image=my_image)
canvas.pack()
