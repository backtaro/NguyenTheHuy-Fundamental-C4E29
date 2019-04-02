colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

for i in colors:
    color(i)
    begin_fill()
    forward(50)

    for i in range(2):
        left(90)
        forward(85)
        left(90)
        forward(50)
    end_fill()

mainloop()