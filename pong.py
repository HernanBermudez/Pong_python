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




# MAIN LOOP
while True:
    win.update()