import pgzrun
import random

TITLE = "Lohith's Random Shapes"
WIDTH = 600
HEIGHT = 400

x = random.randint(50,550)
y = random.randint(50,350)
x2 = random.randint(50,550)
y2 = random.randint(50,350)
x3 = random.randint(50,550)
y3 = random.randint(50,350)
x4 = random.randint(50,550)
y4 = random.randint(50,350)
x5 = random.randint(50,550)
y5 = random.randint(50,350)
w = random.randint(20,100)
h = random.randint(20,100)
w2 = random.randint(20,100)
h2 = random.randint(20,100)
w3 = random.randint(20,100)
h3 = random.randint(20,100)
r = random.randint(10,40)
r2 = random.randint(10,40)

def draw():

    # Rectangles
    rect = Rect((x, y), (w, h))
    screen.draw.rect(rect, "red")

    rect = Rect((x2, y2), (w2, h2))
    screen.draw.rect(rect, "blue")

    rect = Rect((x3, y3), (w3, h3))
    screen.draw.rect(rect, "green")

    # Circles
    screen.draw.circle((x4, y4), r, "yellow")
    screen.draw.circle((x5, y5), r2, "orange")
    
pgzrun.go()