import tkinter
import random 
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX)
canvas.pack()


r = 20

farba = "black"
def paleta(x, y, r):
    canvas.create_rectangle(x-r, y-r, x+r, y+r, fill="red")
    canvas.create_rectangle(x+r, y-r, x+3*r, y+r, fill="green")
    canvas.create_rectangle(x+3*r, y-r, x+5*r, y+r, fill="blue")

def kreslenie(event):
    global a, b
    xx, yy = event.x, event.y
    canvas.create_line(a, b, xx, yy, fill = farba)
    a, b = xx, yy
   
def klik(event):
    global a, b
    xx, yy = event.x, event.y
    a, b = xx, yy
    if X_MAX/2-r < xx < X_MAX/2+r and Y_MAX-r-r < yy < Y_MAX:
        farba = "red"
def pusti(event):
    global a, b
    a,b=0,0
       
paleta(X_MAX/2, Y_MAX-r, r)

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', kreslenie)
canvas.bind('<ButtonRelease>', pusti)

