#slider and canvas colour - not working
import tkinter as tk
window=tk.Tk()
slider=tk.Scale(window, from_=0, to=100)
colour="#FF0000"
canvas=tk.Canvas(window, height=300, width=300, bg=colour)
canvas.pack()
slider.pack()
#tk.mainloop()
window.mainloop()
