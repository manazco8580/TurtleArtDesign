 
def move(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    

def polygon(t,side,distance):
    angle=360/side
    for times in range(side):
        t.forward(distance)
        t.left(angle)





