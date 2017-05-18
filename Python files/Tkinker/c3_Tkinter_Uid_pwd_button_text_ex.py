#not working


import tkinter as tk
window=tk.Tk()

def show():
    p = password.get() #get password from entry
    print(p)

    
password = StringVar() #Password variable
tk.Label(window, text="UserName").grid(row=0, sticky='w')
tk.Label(window, text="Password").grid(row=1, sticky='w')
tk.Entry(window, width=20).grid(row=0,column=1,sticky='e')
passEntry=tk.Entry(window, textvariable=password, show="*", width=15).grid(row=1,column=1,sticky='e')
submit = Button(window, text='Show Console',command=show).pack() 
window.mainloop()


     
