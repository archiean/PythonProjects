import tkinter as tk
t=tk.Tk()

#color="#A43BC7"

def slidercolor(x):
    red=redslider.get()
    green=greenslider.get()
    blue=blueslider.get()
    Color="#%02x%02x%02x" %(red,green,blue)
    canvas.config(bg=Color)
    entry.delete(0, tk.END)
    entry.insert(0,Color)

canvas=tk.Canvas(t,width=500, height=500)
canvas.grid(row=2, column=1,columnspan=3)
redslider=tk.Scale(t,from_=0, to=255, command=slidercolor)
redslider.grid(row=1,column=1)
greenslider=tk.Scale(t,from_=0, to=255, command=slidercolor)
greenslider.grid(row=1,column=2)
blueslider=tk.Scale(t,from_=0, to=255, command=slidercolor)
blueslider.grid(row=1,column=3)
entry=tk.Entry(t)
entry.grid(row=3,column=1, columnspan=3)



t.mainloop()
