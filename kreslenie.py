import tkinter
import random 
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX)
canvas.pack()

r=1

def klik(event):
    x, y = event.x, event.y
    canvas.create_oval(x-r, y-r, x+r, y+r)
   

def kreslenie(event):
    global a, b
    xx, yy = event.x, event.y
    canvas.create_line(a, b, xx, yy)
    a, b = xx, yy

def pusti(event):
    canvas.create_oval(a-r, b-r, a+r, b+r)

#def kreslenie(event):
    
#for _ in range    
a, b = 0, 0
canvas.bind('<ButtonPress>', klik)
canvas.bind('<Motion>', kreslenie)
canvas.bind('<ButtonRelease>', pusti)

