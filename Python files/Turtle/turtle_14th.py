
import turtle


def drawsquare( size ):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    return()

def main():
    for i in range(50,70):
        drawsquare(i)
main()
