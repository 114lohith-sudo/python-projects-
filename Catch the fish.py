import pgzrun
from random import randint

WIDTH=800
HEIGHT=500

TITLE="Catch the fish"
score=0
f=Actor('fish')
f.pos=(randint(0,WIDTH),randint(0,HEIGHT))

def draw():
    screen.fill(color="Light blue")
    f.draw()
    screen.draw.text(str(score),center=(400,20),fontsize=30,color="Black")

def on_mouse_down(pos):
    global score
    if f.collidepoint(pos):
        score+=1
        f.pos=(randint(0,WIDTH),randint(0,HEIGHT))
    else:
        score-=1


pgzrun.go()