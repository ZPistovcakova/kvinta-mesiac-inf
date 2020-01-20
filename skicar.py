import tkinter
import random 
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX, bg = "white")
canvas.pack()

r = 20

global farba, hrubka
farba = "black"
hrubka = 1

def paleta(x, y, r):
    canvas.create_rectangle(x-r, y-r, x+r, y+r, fill="red")
    canvas.create_rectangle(x+r, y-r, x+3*r, y+r, fill="green")
    canvas.create_rectangle(x+3*r, y-r, x+5*r, y+r, fill="blue")
    canvas.create_rectangle(x-3*r, y-r, x-r, y+r)
    canvas.create_oval(x-3*r+5, y-r+5, x-r-5, y+r-5, fill="black")
    canvas.create_rectangle(x-5*r, y-r, x-3*r, y+r)
    canvas.create_oval(x-5*r+10, y-r+10, x-3*r-10, y+r-10, fill="black")
    canvas.create_rectangle(x-7*r, y-r, x-5*r, y+r)
    canvas.create_oval(x-7*r+15, y-r+15, x-5*r-15, y+r-15, fill="black")
    canvas.create_rectangle(x-9*r, y-r, x-7*r, y+r)
    canvas.create_text(x-8*r, y, font = ("Arial", 7), text = "erase all")
    canvas.create_rectangle(x+5*r, y-r, x+7*r, y+r, fill = "gray")
    canvas.create_rectangle(x+5*r+10, y-r+7, x+7*r-10, y+r-7, fill = "white")
    canvas.create_text(x+6*r, y, font = ("Arial", 7), text = "guma")

def kreslenie(event):
    global a, b, farba, hrubka
    xx, yy = event.x, event.y
    canvas.create_line(a, b, xx, yy, fill = farba, width = hrubka)
    a, b = xx, yy
   
def klik(event):
    global a, b, farba, hrubka
    xx, yy = event.x, event.y
    a, b = xx, yy
    if X_MAX/2-r < xx < X_MAX/2+r and Y_MAX-r-r < yy < Y_MAX:
        farba = "red"

    elif X_MAX/2+r < xx < X_MAX/2+3*r and Y_MAX-r-r < yy < Y_MAX:
        farba = "green"

    elif X_MAX/2+3*r < xx < X_MAX/2+5*r and Y_MAX-r-r < yy < Y_MAX:
        farba = "blue"

    elif X_MAX/2-3*r < xx < X_MAX/2-r and Y_MAX-r-r < yy < Y_MAX:
        hrubka = 10

    elif X_MAX/2-5*r < xx < X_MAX/2-3*r and Y_MAX-r-r < yy < Y_MAX:
        hrubka = 5

    elif X_MAX/2-7*r < xx < X_MAX/2-5*r and Y_MAX-r-r < yy < Y_MAX:
        hrubka = 1

    elif X_MAX/2-9*r < xx < X_MAX/2-7*r and Y_MAX-r-r < yy < Y_MAX:
        canvas.delete("all")
        paleta(X_MAX/2, Y_MAX-r, r)

    elif X_MAX/2+5*r < xx < X_MAX/2+7*r and Y_MAX-r-r < yy < Y_MAX:
        farba = "white"
        hrubka = 10

#    else:
#        print('snezi')
     
def pusti(event):
    global a, b
    a,b=0,0
       
paleta(X_MAX/2, Y_MAX-r, r)

canvas.bind('<Button-1>', klik)
canvas.bind('<B1-Motion>', kreslenie)
canvas.bind('<ButtonRelease>', pusti)

