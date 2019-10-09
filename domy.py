import tkinter
import random
canvas=tkinter.Canvas(width=800,height=600)
canvas.pack()
x=10
y=50

def strecha():
    canvas.create_polygon([x,y,x+25,y-40,x+50,y],fill="red")
def dom():
    for i in range(1,11):
        global x
        canvas.create_rectangle(x,y,x+50,y+50,fill="blue")
        strecha()
        canvas.create_line(x,y,x+25,y-40)
        canvas.create_line(x+25,y-40,x+50,y)
    
        x=x+60
        
dom()
