import tkinter
import random
canvas=tkinter.Canvas(width=1000,height=500,bg="white")
canvas.pack()

def more():
    canvas.create_rectangle(0,250,1000,500,fill="blue",outline="blue")

def mesiac(x,y,r,farba,pozadie):
    canvas.create_oval(x-r,250-y-r,x+r,250-y+r,fill=farba,outline=farba)
    canvas.create_oval(x-r/2,250-y-r,x+r+r/2,250-y+r,fill=pozadie,outline=pozadie)

def vlajka(b,farba):
    canvas.create_oval(b,230,b+250,355,fill="red")
    canvas.create_line(b+125,175,b+125,230)
    canvas.create_rectangle(b+125,75,b+250,175,fill=farba)

def mesiac_obrateny(x,y,r,farba,pozadie):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=farba,outline=farba)
    canvas.create_oval(x-1.5*r,y-r,x+r-0.5*r,y+r,fill=pozadie,outline=pozadie)

def logo(x,y,r,farba,pozadie):
    mesiac(x,y,r,farba,pozadie)
    mesiac_obrateny(x-2.5*r,y,r,farba,pozadie)

def lodka(x,y,a,b,c,s,r):
    canvas.create_polygon(x-a,y,x+a,y,x+b,y+c,x-b,y+c,fill="brown",outline="black")
    canvas.create_rectangle(x-s,y-a-a,x+s,y,fill="red",outline="red")
    canvas.create_polygon(x,y-a-a,x+b,y-b,x,y-s-s,fill="white",outline="black")
    logo(x+b/2,y+c/2,r,"light sky blue","brown")


## poznamka
    
x=random.randint(550,750)
y=random.randint(130,200)
vlajka(0,"green")
vlajka(725,"red")
more()
mesiac(x,y,40,"yellow","white")
mesiac(x,-y,40,"yellow","blue")
mesiac(187,125,20,"red","green")
logo(930,125,15,"light sky blue","red")

x=500
z=235
a=70
b=37
c=50
s=5
r=10

for i in range(1,4):
    lodka(x,z,a,b,c,s,r)
    x=x-100
    z=z+90
    a=a+30
    b=b+15
    c=c+15
    s=s+4
    r=r+7
    y=y+90


##lodka(385,300,100,52,65,9)

