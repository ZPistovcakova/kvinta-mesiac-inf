import tkinter
from random import randrange, randint
X_MAX, Y_MAX = 300, 200
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX)
canvas.pack()

r, g, b = 255, randint(0, 255), randrange (256)
