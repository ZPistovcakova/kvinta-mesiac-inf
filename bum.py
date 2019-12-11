import tkinter
import random 
X_MAX, Y_MAX = 800, 600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX)
canvas.pack()

x, y = 400,300

for _ in range(1,20000):
    farba = "black"
    a, b = random.randint(1, X_MAX), random.randint(1, Y_MAX)

    if a <= X_MAX/2 and b <= Y_MAX/2:
        farba = "red"

    elif a <= X_MAX/2 and b > Y_MAX/2:
        farba = "green"

    elif a > X_MAX/2 and b <= Y_MAX/2:
        farba = "blue"

    elif a > X_MAX/2 and b > Y_MAX/2:
        farba = "yellow"

    else:
        print('hbgewfhwqbc')

    canvas.create_line(x, y, a, b, fill = farba)    
