import turtle
import random
ekran=turtle.Screen()
ekran.bgcolor("light green")
ekran.title("Turtle Race")
ekran.setup(1.0,1.0)

pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(-200,200)
pen.pendown()
for i in range(1,11):
    pen.write(i)
    pen.right(90)
    pen.forward(250)
    if i==10:
        pen.write("Finish",font=("Arial",15))
    pen.back(250)
    pen.penup()
    pen.left(90)
    pen.forward(50)
    pen.pendown()

finishlinex=250
def createTurle(color,startx,starty):
    player=turtle.Turtle()
    player.color(color)
    player.shape("turtle")
    player.penup()
    player.goto(startx,starty)
    player.pendown()
    return player
p1=createTurle("red",-210,150)
p2=createTurle("black",-210,100)
p3=createTurle("green",-210,50)
p4=createTurle("white",-210,0)
p5=createTurle("blue",-210,-50)

while True:
    p1.forward(random.randint(5,10))
    if p1.pos()[0]>=finishlinex:
        p1.write('I won the race!!',font=('Arial',30))
        break
    p2.forward(random.randint(5,10))
    if p2.pos()[0]>=finishlinex:
        p2.write('I won the race!!',font=('Arial',30))
        break
    p3.forward(random.randint(5,10))
    if p3.pos()[0]>=finishlinex:
        p3.write('I won the race!!',font=('Arial',30))
        break
    p4.forward(random.randint(5,10))
    if p4.pos()[0]>=finishlinex:
        p4.write('I won the race!!',font=('Arial',30))
        break
    p5.forward(random.randint(5,10))
    if p5.pos()[0]>=finishlinex:
        p5.write('I won the race!!',font=('Arial',30))
        break
    
turtle.done()