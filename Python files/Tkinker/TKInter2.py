import tkinter as tk
window=tk.Tk()

def changeString():
    stringToCopy=entry.get()
    stringToCopy=stringToCopy[::-1]
    entry.delete(0, tk.END)
    entry.insert(0, stringToCopy)
    
entry=tk.Entry(window)#creating text box
#s=entry.get() #function returns value in text box
button=tk.Button(window,text="Change", command=changeString)

entry.pack()
button.pack()
window.mainloop()


