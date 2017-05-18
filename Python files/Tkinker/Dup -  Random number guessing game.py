import random
import tkinter as tk
t=tk.Tk()

score=0
rounds=0
maxno=10

def buttonClick():
    global score
    global rounds
    try:
        guess=int(guessBox.get())
        if 0<guess<=maxno:
            result=random.randrange(1,maxno)
            if guess==result:
                score=score+1
            rounds=rounds+1
        else:
            result="Entry not valid"
    except:
        result="Entry not valid"
    resultLabel.config(text=result)
    scoreLabel.config(text=str(score) + "/" + str(rounds))
    guessBox.delete(0,tk.END)


guessLabel=tk.Label(t, text="Enter a number from 1 to " + str(maxno))
guessBox=tk.Entry(t)
resultLabel=tk.Label(t)
scoreLabel=tk.Label(t)
button=tk.Button(t, text="Guess", command=buttonClick)

guessLabel.pack()
guessBox.pack()
resultLabel.pack()
scoreLabel.pack()
button.pack()
t.mainloop()
    
