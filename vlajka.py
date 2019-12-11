import tkinter
from random import randrange, randint
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX)
canvas.pack()

r = 10

for _ in range(1,20000):
    farba = "black"

    x, y = randint(r, X_MAX-r), r + randrange(Y_MAX - 2*r)

    if x <= X_MAX/4 and y <= Y_MAX/4:
        farba = "yellow"

    elif x >= X_MAX/2 and y <= Y_MAX/4:
        farba = "yellow"

    elif x <= X_MAX/4 and y >= Y_MAX/2:
        farba = "yellow"

    elif x >= X_MAX/2 and y >= Y_MAX/2:
        farba = "yellow"

    else:
        farba = "blue"

    canvas.create_oval(x-r, y-r, x+r, y+r,fill=farba,outline=farba)    
