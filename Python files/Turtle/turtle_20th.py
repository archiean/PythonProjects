# Draws various types of geometric figures
import turtle ,math
#put label on top of page
turtle.title('Geometric Figure')
#setup screen size
turtle.setup(800,800,0,0)   
#create a turtle object
ttl=turtle.Turtle()    
#draw a line from(x1,y1) to (x2,y2)
def drawLine (tt1,x1,y1,x2,y2):
    ttl.color('red')
    ttl.penup()
    ttl.goto(x1,y1)
    ttl.pendown()
    ttl.goto(x2,y2)
    ttl.penup()

def drawPolygon(ttl,x,y,num_side,radius):
    sideLen = 2* radius * math.sin(math.pi/num_side)
    angle = 360/num_side
    ttl.penup()
    ttl.goto(x,y)
    ttl.pendown()
    for iter in range (num_side):
        ttl.forward(sideLen)
        ttl.left(angle)
        ttl.hideturtle()
def main():

    # DRAW A CIRCLE

    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-40,125)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('black')
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(40,125)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('black')
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    ttl=turtle.Turtle()
    turtle.hideturtle()
  

    

    
    #draw equilateral triangle
    ttl.color('blue')
    drawPolygon(ttl,-20,60,3,30)

    #draw a line
    ttl.color('blue')
    drawLine(ttl,-40,30,10,10)
    drawLine(ttl,10,10,50,30)

    #persist drawing
    turtle.done()
main()
