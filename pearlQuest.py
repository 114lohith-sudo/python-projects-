import pgzrun,time
from random import randint
WIDTH = 800
HEIGHT = 400
TITLE="Pearl Quest"

pearl=Actor("pearl")
pearl.pos=(randint(0,WIDTH),randint(0,HEIGHT))
p=Actor("police")
p.pos=(randint(0,750),randint(0,350))
t=Actor("theif")
t.pos=(400,200)

score=0

def draw():
    screen.fill("black")
    pearl.draw()
    p.draw()
    t.draw()
    screen.draw.text("Score:"+str(score),topleft=(50,50))
    
def spawnner():
    pearl.pos=(randint(0,WIDTH),randint(0,HEIGHT))
    p.pos=(randint(0,750),randint(0,350))
    

def update():
    global score
    if keyboard.left:
        t.x-=3
    if keyboard.right:
        t.x+=3
    if keyboard.down:
        t.y+=3
    if keyboard.up:
        t.y-=3
    if t.colliderect(p):
        score-=1
        spawnner()
    if t.colliderect(pearl):
        score+=1
        spawnner()
        


clock.schedule(spawnner,5)

pgzrun.go()