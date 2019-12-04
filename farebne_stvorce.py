import tkinter
from random import randrange, randint
X_MAX, Y_MAX = 300, 200
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="white")
canvas.pack()

r=50
x, y = randint(r, X_MAX-r), r + randrange(Y_MAX - 2*r)
dx = 1
dy = 1

while True:
    canvas.delete("all")
    
    canvas.create_oval(x-r, y-r, x+r, y+r,fill="red",outline="red")
    x += dx
    y += dy
    if y >= Y_MAX - r:
        dy *= -1
    if y <= r: 
        dy *= -1
    if x >= X_MAX - r: 
        dx *= -1
    if x <= r: 
        dx *= -1        

    canvas.update()
    canvas.after(1)

