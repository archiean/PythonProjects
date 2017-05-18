import tkinter as tk
window=tk.Tk()
window.title('Find & Replace')

tk.Label(window, text="Find:").grid(row=0,column=0,sticky='e')
tk.Entry(window, width=60).grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)

tk.Label(window, text="Replace:").grid(row=1,column=0,sticky='e')
tk.Entry(window).grid(row=1, column=1, padx=2, pady=2, sticky='we', columnspan=9)

tk.Button(window, text="Find").grid(row=0, column=10, padx=2, pady=2, sticky='e'+'w')
tk.Button(window, text="Find All").grid(row=1, column=10, padx=2, sticky='e'+'w')
tk.Button(window, text="Replace").grid(row=2, column=10, padx=2, sticky='e'+'w')
tk.Button(window, text="Replace All").grid(row=3, column=10, padx=2, sticky='e'+'w')

tk.Checkbutton(window, text="Match Whole Word only").grid(row=2, column=1, columnspan=4, sticky='w')
tk.Checkbutton(window, text="Match Case").grid(row=3, column=1, columnspan=4, sticky='w')
tk.Checkbutton(window, text="Wrap Around").grid(row=4, column=1, columnspan=4, sticky='w')


tk.Label(window, text="Direction:").grid(row=2,column=6,sticky='w')

tk.Radiobutton(window,text="Up", value=1).grid(row=3, column=6, columnspan=6, sticky='w')
tk.Radiobutton(window,text="Down", value=2).grid(row=3, column=7, columnspan=6, sticky='w')

window.mainloop()
