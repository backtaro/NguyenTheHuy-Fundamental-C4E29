colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

for i in range(3):
    pencolor(colors[0])
    forward(150)
    left(360/3)

for i in range(4):
    pencolor(colors[1])
    forward(150)
    left(360/4)

for i in range(5):
    pencolor(colors[2])
    forward(150)
    left(360/5)

for i in range(6):
    pencolor(colors[3])
    forward(150)
    left(360/6)

for i in range(7):
    pencolor(colors[4])
    forward(150)
    left(360/7)

mainloop()