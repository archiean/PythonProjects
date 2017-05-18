import tkinter as tk
import time

window=tk.Tk()

tk.Button(window, text="First Button").pack(fill='x')
tk.Button(window, text="Second only Button..").pack(fill='x')
tk.Button(window, text="Third Button for use").pack(fill='x')
tk.Button(window, text='LEFT').pack(side='left')
tk.Button(window, text='RIGHT').pack(side='left')
tk.Button(window, text='CENTER').pack(side='left')


window.mainloop()
