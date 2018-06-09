#Leonardo Farinha - H2

import turtle

turtle.shape("turtle")
turtle.width(3)

turtle.up()
turtle.goto(0, 0)
turtle.down()

turtle.left(90)

for x in range(0, 20):
    turtle.forward(x)

turtle.up()
turtle.goto(30, 0)
turtle.down()

for x in range(0, 20):
    turtle.forward(x)

turtle.up()
turtle.goto(60, 0)
turtle.down()

for x in range(0, 20):
    turtle.forward(x)

turtle.up()
turtle.goto(0, 0)
turtle.down()

turtle.exitonclick()
