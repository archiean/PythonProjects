import tkinter as tk
t=tk.Tk()

button1=tk.Button(t, text="First button").pack(fill='x')
button2=tk.Button(t, text="Second button").pack(fill='x')
button3=tk.Button(t, text="Third button").pack(fill='x')
button4=tk.Button(t, text="Left").pack(side="left")
button5=tk.Button(t, text="Right").pack(side="left")
button6=tk.Button(t, text="Center").pack(side="left")


button1=tk.Button(t, text="A").pack(fill='y', side="left")
button2=tk.Button(t, text="B").pack(fill='x', side="top")
button3=tk.Button(t, text="C").pack(fill='x')
button4=tk.Button(t, text="D").pack(side="left")
