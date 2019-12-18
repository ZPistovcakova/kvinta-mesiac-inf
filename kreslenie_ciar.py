import tkinter
import random 
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX)
canvas.pack()

r = 10

def klik(event):
    x, y = event.x, event.y
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
    global xx, yy
    xx, yy = x, y

def pusti(event):
    x, y = event.x, event.y
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")
    canvas.create_line(xx, yy, x, y)


canvas.bind('<ButtonPress>', klik)
canvas.bind('<ButtonRelease>', pusti)
