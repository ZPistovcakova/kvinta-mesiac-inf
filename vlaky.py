import tkinter
import random
canvas=tkinter.Canvas(width=800,height=600,bg="white")
canvas.pack()

def vagon(x,y,r,farba):
    canvas.create_rectangle(x,y-50,x+80,y,fill=farba)
    canvas.create_line(x-10,y-10,x,y-10,width="5")
    canvas.create_oval(x+20-r,y-r,x+20+r,y+r,fill="black")
    canvas.create_oval(x+60-r,y-r,x+60+r,y+r,fill="black")
    canvas.create_line(x+80,y-10,x+90,y-10,width="5")

x=30
for i in range(1,5):
    vagon(x,80,10,"red")
    x+=100

x=30
for i in range(1,3):
    vagon(x,200,10,"green")
    x+=100
x=30
for i in range(1,4):
    vagon(x,350,10,"blue")
    x+=100    
    
