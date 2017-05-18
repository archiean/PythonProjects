import tkinter as tk
t=tk.Tk()
t.title('Find and replace')

tk.Label(t, text="Find:").grid(row=0,column=0, sticky='w')
tk.Entry(t).grid(row=0,column=1, columnspan=9, padx=2, pady=2, sticky='we')
tk.Label(t, text="Replace:").grid(row=1,column=0, sticky='e')
tk.Entry(t).grid(row=1,column=1, columnspan=9, padx=2, pady=2, sticky='we')

tk.Button(t, text="find").grid(row=0, column=10, padx=2, pady=2, sticky='e'+'w')
tk.Button(t, text="find all:").grid(row=1, column=10,padx=2,sticky='e'+'w')
tk.Button(t, text="Replace").grid(row=2, column=10,padx=2,sticky='e'+'w')
tk.Button(t, text="Replace all").grid(row=3, column=10,padx=2,sticky='e'+'w')

tk.Checkbutton(t,text="Match whole word only").grid(row=2, column=1, columnspan=4,sticky='w')
tk.Checkbutton(t,text="Match case").grid(row=3, column=1, columnspan=4,sticky='w')
tk.Checkbutton(t,text="Wrap around").grid(row=4, column=1, columnspan=4,sticky='w')

tk.Label(t, text="Direction:").grid(row=2,column=6, sticky='w')

tk.Radiobutton(t,text="up", value=1).grid(row=3, column=6, columnspan=6,sticky='w')
tk.Radiobutton(t,text="down", value=2).grid(row=3, column=7,sticky='w')

t.mainloop()
