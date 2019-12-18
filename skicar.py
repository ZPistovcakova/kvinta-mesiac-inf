import tkinter
import random 
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX)
canvas.pack()

x, y = X_MAX/2, Y_MAX/2
r = 50

def klik(event):
    xx, yy = event.x, event.y
    if x-r < xx < x+r and\
       y-r < yy < y+r
