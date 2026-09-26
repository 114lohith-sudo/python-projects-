import pgzrun
from random import randint
from time import time
WIDTH=600
HEIGHT=400

stars=[]
num_stars=5
lines=[]
#So we can know the next star when doing the connections
next_star=0

start_time=0
total_time=0
end_time=0

def create_stars():
    #Need to globalize valiables if they need to be used in other funtions
    #Globalizing start_time so it can be used in other functions
    global start_time
    #Adds stars to the list of stars based on the number in num_stars
    for count in range(num_stars):
        #Actor is used to maken charecters/sprites with images
        star=Actor("star")
        star.pos=(randint(50,WIDTH-50),randint(50,HEIGHT-50))
        stars.append(star)
    #time function from the library time gives you the current time 
    start_time=time()

def draw():
    number=1
    global total_time
    #screen.blit is used to draw the background
    screen.blit("space",(0,0))
    #this for loop is made to draw a nnumber for each star
    for star in stars:
        #index of x is 0 and index of y is 1 
        screen.draw.text(str(number),(star.pos[0],star.pos[1]+30))
        star.draw()
        number+=1

    for line in lines:
        screen.draw.line(line[0],line[1],(255,0,0))
    
    if next_star<num_stars:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(300,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(300,10),fontsize=30)
    
def on_mouse_down(pos):
    global next_star,lines,num_stars
    x,y=pos
    if next_star<num_stars:
        if stars[next_star].collidepoint(x,y):
            if next_star > 0:
                lines.append((stars[next_star-1].pos,stars[next_star].pos))
            next_star+=1
    else:
        lines=[]    
        next_star=0




create_stars()
pgzrun.go()