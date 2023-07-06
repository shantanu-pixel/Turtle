import turtle
z=turtle.Turtle()
z.getscreen().bgcolor("black")
z.penup()
z.goto(-200,100)
z.pendown()
z.color("red")
z.speed(495)

def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
            turtle.end_fill()
            
star(z,360)
turtle.done()