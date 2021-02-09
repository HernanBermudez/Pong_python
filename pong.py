# SIMPLE PONG GAME
# BY: HERNAN BERMUDEZ

import turtle

win = turtle.Screen()

win.title("Pong by ElCombazo")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# PADDLE A (default 20x20 px)

paddle_a = turtle.Turtle()
paddle_a.speed(0) # MAXIMUM POSSIBLE SPEED
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize( stretch_wid=5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# PADDLE B

paddle_b = turtle.Turtle()
paddle_b.speed(0) # MAXIMUM POSSIBLE SPEED
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize( stretch_wid=5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL

ball = turtle.Turtle()
ball.speed(0) # MAXIMUM POSSIBLE SPEED
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# FUNCTION

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# MAIN LOOP
while True:
    win.update()

    # BALL MOVEMENT

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BORDER CHECKING
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1