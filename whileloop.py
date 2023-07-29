from turtle import *

count = 150
pencolor("red")
while count > 0:
    fd(count)
    lt(360//6)

    count -= 5

mainloop()