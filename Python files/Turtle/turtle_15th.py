import turtle
def main():
    wn=turtle.Screen()
    wn.bgcolor("lightgreen")
    a=turtle.Turtle()
    a.color("blue")
    a.penup()
    size=20

    for i in range(30):
        a.stamp()
        size=size+3
        a.forward(size)
        a.right(24)
main() 


