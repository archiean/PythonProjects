import turtle

wn = turtle.Screen()
elsa = turtle.Turtle()

for i in range(10):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(36)

wn.exitonclick()
#wn.mainloop()
