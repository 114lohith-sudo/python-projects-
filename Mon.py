import pgzrun
from random import randint

WIDTH = 700
HEIGHT = 500
TITLE = "Help the monkey eat a banana"

mo =Actor("monkey")
mo.pos = (100, 60)

def draw():
    global screen
    screen.blit("jungle", (0, 0))
    mo.draw()

def update():
    pass

pgzrun.go()