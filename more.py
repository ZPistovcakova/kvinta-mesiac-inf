import tkinter
import random
canvas=tkinter.Canvas(width=1000,height=1000)
canvas.pack()

def more():
    canvas.create_rectangle(0,500,1000,1000,fill="blue",outline="blue")

more()
