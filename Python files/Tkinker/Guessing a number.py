import random
import tkinter as tk
window=tk.Tk()

maxno=10
score=0
rounds=0

def buttonClick():
    global score
    global rounds
    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxno:
            result = random.randrange(1, maxno)
            if guess == result:
                score = score +1
            rounds = rounds +1
        else:
            result = "Entry Not Valid"
    except:
        result = "Entry Not Valid"
    resultLabel.config(text=result)
    scoreLabel.config(text=str(score) + "/" + str(rounds))
    guessBox.delete(0, tk.END)

guessLabel = tk.Label(window, text="Enter a Number from 0 to " + str(maxno))
guessBox=tk.Entry(window)
resultLabel = tk.Label(window)
scoreLabel = tk.Label(window)
button = tk.Button(window, text="Guess", command=buttonClick)

guessLabel.pack()
guessBox.pack()
resultLabel.pack()
scoreLabel.pack()
button.pack()
window.mainloop()
