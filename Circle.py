import pgzrun

WIDTH = 400
HEIGHT = 400 
TITLE = "Lohith's Circles"

def draw():
    s = 20
    colors=["green","yellow","orange","red"]
    for c in range(4):
        screen.draw.circle((200,200),s,colors[c])
        s += 20
    
pgzrun.go()