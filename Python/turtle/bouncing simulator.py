import turtle
import random
import time

screen = turtle.Screen()

screen.bgcolor('black')
screen.title('Bouncing Ball Simulator')
screen.tracer(0)

balls = []
for i in range(200):
  balls.append(turtle.Turtle())

for ball in balls:
  ball.shape(random.choice(['circle', 'square', 'turtle']))
  ball.color(random.choice(['red', 'yellow', 'orange', 'white']))
  ball.penup()
  ball.speed(0)

  x = random.randint(-290, 290)
  y = random.randint(200, 400)
  ball.goto(x, y)

  ball.dy = 0
  ball.dx = random.choice([i for i in range(-3, 4)])

gravity = 0.1

counter = 0

while True:
  screen.update()
  time.sleep(0.02)

  counter += 1
  if counter == 100:
    if len(balls) == 0:
      continue

    balls[-1].setx(-5000)
    balls[-1].sety(-5000)
    balls = balls[:-1]
    counter = 0

  for ball in balls:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() < -285:
      ball.dy = -ball.dy

    if ball.xcor() > 300:
      ball.dx = -ball.dx

    if ball.xcor() < -300:
      ball.dx = -ball.dx

screen.mainloop()