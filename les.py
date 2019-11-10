import tkinter
import random
canvas=tkinter.Canvas(width=800,height=600,bg="white")
canvas.pack()

def strom(x,y,r,z):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="lime")
    canvas.create_rectangle(x-5,y+r,x+5,y+r+z,fill="brown",outline="brown")

def trava(x,y):
    for i in range(1,random.randint(3,10)):
        q=random.randint(-10,10)
        h=random.randint(10,20)
        canvas.create_line(x,y,x+q,y-h,fill="green",width=random.randint(1,3))
        

for i in range(1,11):
    x=random.randint(0,800)
    y=random.randint(0,600)
    r=random.randint(40,80)
    z=random.randint(50,100)
    strom(x,y,r,z)

for i in range(1,21):
    trava(random.randint(0,800),random.randint(0,600))
