import tkinter as tk
t=tk.Tk()


canvas1=tk.Canvas(t, width=400, height=400)
canvas1.create_arc(10,10,200,80)
canvas1.create_arc(20,20,200,80, extent=90,style="arc")

#t.mainloop()5


#canvas1.create_arc(10,240,200,320,extent=180)

#canvas1.create_arc(120,250,207,340,extent=319,style="pieslice")

canvas1.create_arc(240,250,137,140,extent=227,style="chord")


canvas1.pack()
