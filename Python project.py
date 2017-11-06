from myFunction import *

import turtle
turtle.colormode(255)
turtle.bgcolor("black")

bob=turtle.Turtle()
bob.width(5)
bob.speed(0)
turtle.tracer(0)


for times in range(255):
    bob.circle(200)
    bob.left(217)
    bob.color(times,0,255)


for times in range(255):
    bob.circle(250)
    bob.left(5)
    bob.color(times,times,0)


for time in range(150):
    move(bob,0,0)
    bob.color(255,255,255)
    bob.forward(time * 6 + 100)
    bob.right(217)


move(bob,0,0)
for time in range(75):
    bob.color(255,255,255)
    bob.forward(time * 6)
    bob.right(217)

   
move(bob,-400,400)
for time in range(35):
    bob.color(255,0,0)
    bob.forward(time * 6)
    bob.right(217)


move(bob,400,-400)
for time in range(35):
    bob.color(0,255,0)
    bob.forward(time * 6)
    bob.right(217)


move(bob,400,400)
for time in range(35):
    bob.color(0,0,255)
    bob.forward(time * 6)
    bob.right(217)


move(bob,-400,-400)
for time in range(35):
    bob.color(120,66,253)
    bob.forward(time * 6)
    bob.right(217)


move(bob,0,400)
for time in range(35):
    bob.color(152,250,142)
    bob.forward(time * 6)
    bob.right(217)


move(bob,0,-400)
for time in range(35):
    bob.color(24,142,100)
    bob.forward(time * 6)
    bob.right(217)


move(bob,400,0)
for time in range(35):
    bob.color(175,78,216)
    bob.forward(time * 6)
    bob.right(217)


move(bob,-400,0)
for time in range(35):
    bob.color(255,120,169)
    bob.forward(time * 6)
    bob.right(217)


move(bob,-725,0)
for times in range(255):
    bob.circle(75)
    bob.left(217)
    bob.color(times,50,255)


move(bob,725,0)
for times in range(255):
    bob.circle(75)
    bob.left(217)
    bob.color(times,50,255)


move(bob,-725,0)
for times in range(20):
    bob.begin_fill()
    bob.color(255,255,255)
    bob.forward(times*10)
    bob.left(90)
    bob.end_fill()


move(bob,725,0)
for times in range(20):
    bob.begin_fill()
    bob.color(255,255,255)
    bob.forward(times*10)
    bob.right(90)
    bob.end_fill()
    

move(bob,725,-300)
for times in range(50):
    bob.begin_fill()
    bob.color(255,255,255)
    bob.circle(times)
    bob.forward(times*6)
    bob.left(217)
    bob.end_fill()


move(bob,-725,-300)
for times in range(50):
    bob.begin_fill()
    bob.color(255,255,255)
    bob.circle(times)
    bob.forward(times*6)
    bob.left(217)
    bob.end_fill()


move(bob,725,300)
for times in range(50):
    bob.begin_fill()
    bob.color(255,255,255)
    bob.circle(times)
    bob.forward(times*6)
    bob.left(217)
    bob.end_fill()


move(bob,-725,300)
for times in range(50):
    bob.begin_fill()
    bob.color(255,255,255)
    bob.circle(times)
    bob.forward(times*6)
    bob.left(217)
    bob.end_fill()







 
