import turtle

def main():
    turtle.title('Hello')
    turtle.setup(1000,1000,0,0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.color('navy')
    turtle.write('Welcome',font=('Times New Roman',36,'bold'))
    turtle.hideturtle()
    turtle.done()

main()
#puttitle
#setup screen size
#move turtle to origin
#set the color to navy
#write the message
#hide the turtle
#persist the drawing

