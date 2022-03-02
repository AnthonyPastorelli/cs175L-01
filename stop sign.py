import turtle

for x in range(8):
    turtle.forward(100)
    turtle.left(45)
turtle.penup()
turtle.goto(0,100)

turtle.write('STOP', font=("Arial", 30, "normal"))

import time
time.sleep(5)
