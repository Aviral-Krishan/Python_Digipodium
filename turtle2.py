from turtle import *
speed("slowest")
side = 6
for i in range(side):
    forward(50)
    for i in range(5):
        forward(50)
        left(72)
        write(i)
    left(360//side)


mainloop() #to keep the window open

