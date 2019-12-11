import tkinter
import random 
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX)
canvas.pack()

def klik(event):
    x, y = event.x, event.y
    print(x, y)

def gula(event):
    x, y = event.x, event.y
    r = 10
    canvas.create_oval(x-r, y-r, x+r, y+r, fill = "blue", outline = "blue")

def pohyb(event):
    x, y = event.x, event.y
    r = 10
    canvas.create_oval(x-r, y-r, x+r, y+r, fill = "blue", outline = "blue")
    a = X_MAX - x
    canvas.create_oval(a-r, y-r, a+r, y+r, fill = "red", outline = "red")
    b = Y_MAX - y
    canvas.create_oval(x-r, b-r, x+r, b+r, fill = "green", outline = "green")
    canvas.create_oval(a-r, b-r, a+r, b+r, fill = "yellow", outline = "yellow")

#canvas.bind('<Button-1>', gula)    
canvas.bind('<Motion>', pohyb)
