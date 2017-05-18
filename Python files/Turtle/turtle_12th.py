import turtle
import random
max=turtle.Turtle()
for x in range(100):
    angle=random.randint(0,45)
    max.right(angle)
    dist=random.randint(10,100)
    max.forward(dist)
    max.back(dist)


