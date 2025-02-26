
import turtle 

window = turtle.Screen()
window.title("Pong by @MelkCampos")
window.bgcolor("black")
window.setup(width= 800, height= 600)
window.tracer(1) # mudando o tracer para 1, para diminuir a velocidade da bolinha

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# score
score_a = 0
score_b = 0

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 14, "normal"))


# functions
def paddle_a_up():
    y = paddle_a.ycor() # ycor: retorna as coordernadas de Y
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # ycor: retorna as coordernadas de Y
    y -= 20
    paddle_a.sety(y)
    

def paddle_b_up():
    y = paddle_b.ycor() # ycor: retorna as coordernadas de Y
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # ycor: retorna as coordernadas de Y
    y -= 20
    paddle_b.sety(y)
    


# keyboard
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx += -1
        pen.clear()
        score_a += 1 # adiciona uma pontuação quando a bolinha sai da tela
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx += -1
        pen.clear()
        score_b += 1 # adiciona uma pontuação quando a bolinha sai da tela
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 14, "normal"))


    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1