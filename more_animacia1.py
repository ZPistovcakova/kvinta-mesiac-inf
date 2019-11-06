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
    mesiac_obrateny(x-40,y,r,farba,pozadie)

def lodka(x,y,a,b,c,s,r):
    canvas.create_polygon(x-a,y,x+a,y,x+b,y+c,x-b,y+c,fill="brown",outline="black")
    canvas.create_rectangle(x-s,y-a-a,x+s,y,fill="red",outline="red")
    canvas.create_polygon(x,y-a-a,x+b,y-b,x,y-s-s,fill="white",outline="black")
    logo(x+b/2,y+c/2,r,"light sky blue","brown")

def stupajucimesiac(x,y,q,r):
    mesiac(x,y+q,r,"yellow","white")
    mesiac(x,y-q,r,"yellow","blue")
    
## poznamka
    
x=random.randint(550,750)
y=random.randint(130,200)
for _ in range(1,50):
    canvas.delete("all")
    q=0
    stupajucimesiac(x,250,q,40)
    q+=5
    canvas.update()
    canvas.after(10)

vlajka(0,"green")
vlajka(725,"red")
more()
mesiac(187,125,20,"red","green")
logo(930,125,15,"light sky blue","red")
lodka(500,235,70,37,50,5,10)
lodka(400,325,100,52,65,9,17)
lodka(300,415,130,67,80,13,24)




##lodka(385,300,100,52,65,9)
