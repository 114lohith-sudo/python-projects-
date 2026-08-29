import pgzrun
from random import randint
from time import time
WIDTH=600
HEIGHT=400

stars=[]
num_stars=5
lines=[]
next_star=0

start_time=0
total_time=0
end_time=0

def create_stars():
    global start_time
    for count in range(num_stars):
        star=Actor("star")
        star.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
        stars.append(star)
    start_time=time()

number=1
def draw():
    global number
    screen.blit("space",(0,0))
    for star in stars:
        screen.draw.text(str(number),(star.pos[0]),star.pos[1]+30)
        number+=1
        star.draw()

    for line in lines:
        screen.draw.line(line[0],line[1],"red")
    
def on_mouse_down(pos):
    global next_star,lines,num_stars
    if next_star<num_stars:
        lines.append(stars[next_star-1].pos,stars[next_star].pos)
        next_star+=1
    else:
        lines=[]    
        next_star=0




create_stars()
pgzrun.go()