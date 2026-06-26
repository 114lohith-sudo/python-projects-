import pgzrun #python game zero run

TITLE ="Lohith's Rectangles"
WIDTH = 300
HEIGHT = 300

def draw():
    #x,y,w,h,c
    rect=Rect((WIDTH/2,HEIGHT/2-5),(20,40))
    screen.draw.rect(rect,color="green")

    rect=Rect((WIDTH/2-20,HEIGHT/2-30),(60,90))
    screen.draw.rect(rect,color="yellow")

    rect=Rect((WIDTH/2-35,HEIGHT/2-45),(90,120))
    screen.draw.rect(rect,color="orange")

    rect=Rect((WIDTH/2-50,HEIGHT/2-60),(120,150))
    screen.draw.rect(rect,color="red")

pgzrun.go()