import tkinter
import random
canvas=tkinter.Canvas(width=1000,height=1000,bg="white")
canvas.pack()

def more():
    canvas.create_rectangle(0,500,1000,1000,fill="blue",outline="blue")

def mesiac(x,y,r,a,farba):
    canvas.create_oval(x-r,500-y-r,x+r,500-y+r,fill="yellow",outline="yellow")
    canvas.create_oval(x-a,500-y-r,x+r+r,500-y+r,fill=farba,outline=farba)

def vlajka():
    canvas.create_oval(0,460,250,710,fill="red")
    canvas.create_line(125,350,125,460)
##    canvas.create_rectangle(
## poznqmka

x=random.randint(100,900)
y=random.randint(130,450)
vlajka()
more()
mesiac(x,y,40,15,"white")
mesiac(x,-y,40,15,"blue")
