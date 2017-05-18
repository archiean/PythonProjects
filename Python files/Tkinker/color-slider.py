#slider and canvas colour
import tkinter as tk
window=tk.Tk()

def slideUpdate(s):
    red=rSlider.get()
    green=gSlider.get()
    blue=bSlider.get()

    colour="#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=colour)
    hexText.delete(0,tk.END)
    hexText.insert(0,colour)


rSlider=tk.Scale(window, from_=0, to=255, command=slideUpdate)
gSlider=tk.Scale(window, from_=0, to=255, command=slideUpdate)
bSlider=tk.Scale(window, from_=0, to=255, command=slideUpdate)

canvas=tk.Canvas(window, height=300, width=300)
hexText=tk.Entry(window)

rSlider.grid(row=1,column=1)
gSlider.grid(row=1, column=2)
bSlider.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
#canvas.grid(row=2, column=1)
hexText.grid(row=3, column=1, columnspan=3)
window.mainloop()
