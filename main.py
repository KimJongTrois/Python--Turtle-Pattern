def drawDiamond():
  for i in range(2):
    toytle.right(30)
    toytle.forward(100)
    toytle.left(60)
    toytle.forward(100)
    if i >0:
      break
    else:
      toytle.left(150)

import turtle

toytle = turtle.Turtle()
toytle.hideturtle()
toytle.color("black")

toytle.speed(10)

for i in range(9):
  drawDiamond()
  toytle.left(190)

turtle.done()