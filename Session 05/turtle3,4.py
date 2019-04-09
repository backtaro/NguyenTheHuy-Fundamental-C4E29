from turtle import *

speed(0)
def draw_square(x,y):
    pencolor(y)
    for i in range(4):
        forward(x)
        left(90)
    
# print(draw_square(90,"green"))

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()