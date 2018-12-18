from turtle import *
from base import square,vector

p1 = vector(-100,0)
p1aim = vector(4,0)
p1body = set()

p2 = vector(100,0)
p2aim = vector(-4,0)
p2body = set()

def inside(head):
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    p1.move(p1aim)
    p1head=p1.copy()

    p2.move(p2aim)
    p2head=p2.copy()

    
  

    if not inside(p1head) or p1head in p2body:
        print("player 2 wins")
        return
    
    if not inside(p2head) or p2head in p1body:
        print("player 1 wins")
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p2.x,p2.y,3,"blue")
    square(p1.x,p1.y,3,"green")
    

    ontimer(draw,50)

    
setup(420,420,370,0)
hideturtle()
tracer(False)
listen()
onkey(lambda:p1aim.rotate(90),'a')
onkey(lambda:p1aim.rotate(-90),'s')
onkey(lambda:p2aim.rotate(90),'j')
onkey(lambda:p2aim.rotate(-90),'k')
draw()
done()
