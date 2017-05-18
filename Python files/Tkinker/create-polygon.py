import tkinter as tk
t=tk.Tk()

canvas=tk.Canvas(t,width=700,height=700)
#canvas.pack
canvas.create_polygon(1,1,100,10,190,110,fill="green",outline="black")
#canvas.pack()
canvas.create_oval(180,160,600,220,fill="orange")
canvas.pack()
        
#t.mainloop()
