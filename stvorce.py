import tkinter
import random
X_MAX,Y_MAX=800,600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,bg="white")
canvas.pack()

def stvorec(x,y,z):
    canvas.create_rectangle(x-z,y-z,x+z,y+z)

for i in range(1,11):
    x=random.randint(101,700)
    y=random.randint(101,500)
    z=random.randint(50,100)
    stvorec(x,y,z)
    for i in range(5,11):
        stvorec(x,y,z)
        z=z+5




   

