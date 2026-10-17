import pgzrun
from random import randint
from time import time

WIDTH=600
HEIGHT=500

satellites=[]
num_satellites=6
lines=[]
next_sat=0


def create_satellite():
    for count in range(num_satellites):
        sat=Actor('satellite')
        sat.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
        satellites.append(sat)

def draw():
    number=1
    for sat in satellites:
        screen.draw.text(str(number),(sat.pos[0],sat.pos[1]+30))
        sat.draw()
        number+=1

    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,0))

def on_mouse_down(pos):
    global next_sat,lines,num_satellites
    x,y=pos
    if next_sat<num_satellites:
        if satellites[next_sat].collidepoint(x,y):
            if next_sat > 0:
                lines.append((satellites[next_sat-1].pos,satellites[next_sat].pos))
            next_sat+=1
    else:
        lines=[]    
        next_sat=0

create_satellite()
pgzrun.go()