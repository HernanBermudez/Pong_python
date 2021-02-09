# SIMPLE PONG GAME
# BY: HERNAN BERMUDEZ

import turtle
import winsound

win = turtle.Screen()

win.title("Pong by ElCombazo")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# SCORE
score_a = 0
score_b = 0

# PADDLE A (default 20x20 px)

paddle_a = turtle.Turtle()
paddle_a.speed(0) # MAXIMUM POSSIBLE SPEED
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize( stretch_wid=5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# PADDLE B

paddle_b = turtle.Turtle()
paddle_b.speed(0) # MAXIMUM POSSIBLE SPEED
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize( stretch_wid=5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL

ball = turtle.Turtle()
ball.speed(0) # MAXIMUM POSSIBLE SPEED
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.18 # CONTROL THE SPEED OF THE BALL
ball.dy = 0.18

# PEN

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center" , font = ("Courier", 24, "normal"))

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
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center" , font = ("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center" , font = ("Courier", 24, "normal"))

    # PADDLE AND BALL COLISIONS
    if (ball.xcor() >= 335 and ball.xcor() <= 355) and (ball.ycor() <= paddle_b.ycor() + 55 and ball.ycor() >= paddle_b.ycor() - 55):
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (ball.xcor() <= -335 and ball.xcor() >= -355) and (ball.ycor() <= paddle_a.ycor() + 55 and ball.ycor() >= paddle_a.ycor() - 55):
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)