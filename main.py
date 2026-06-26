import pgzrun
from random import randint

WIDTH=800
HEIGHT=500

TITLE="Click the spongebob!"
message=""
sponge=Actor('bob')
sponge.pos=(randint(0,WIDTH),randint(0,HEIGHT))

def draw():
    screen.fill(color="Yellow")
    sponge.draw()
    screen.draw.text(message,center=(400,20),fontsize=30,color="Brown")

def on_mouse_down(pos):
    global message
    if sponge.collidepoint(pos):
        message="Nice!"
        sponge.pos=(randint(0,WIDTH),randint(0,HEIGHT))
    else:
        message="You Missed :("




pgzrun.go()