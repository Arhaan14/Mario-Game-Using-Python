import turtle as t
import os

player_a_score = 0
player_b_score = 0
  
#create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)
  
#Creating the left paddle
left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)
  
#Creating the right paddle
right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)
  
#Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball_dx = 0.15
ball_dy = 0.15
  
#Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0                    Player B: 0", align="center", font=('Arial', 24, 'normal'))
  
#code for moving the left paddle
def left_paddle_up():
    y = left_paddle.ycor()
    y += 50
    left_paddle.sety(y)
  
def left_paddle_down():
    y = left_paddle.ycor()
    y -= 50
    left_paddle.sety(y)
  
#code for moving the right paddle
def right_paddle_up():
    y = right_paddle.ycor()
    y += 50
    right_paddle.sety(y)
  
def right_paddle_down():
    y = right_paddle.ycor()
    y -= 50
    right_paddle.sety(y)
  
#Assign keys to play
window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')
  
while True:
    window.update()
  
    #moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)
  
    #border set up
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1
        os.system("afplay wallhit.wav&")
  
    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1
        os.system("afplay wallhit.wav&")
          
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}                    Player A: {} ".format(player_a_score, player_b_score), align="center", font=('Arial', 24, "normal"))
        os.system("afplay wallhit.wav&")
   
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score), align="center", font=('Arial', 24, "normal"))
        os.system("afplay wallhit.wav&")

       
# bouncing back the ball when it touches left paddle
    if ball.xcor() < -340 and left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50:
        ball.setx(-340)
        ball_dx *= -1
        os.system("afplay paddlehit.wav&")
    
    # bouncing back the ball when it touches right paddle
    if ball.xcor() > 340 and right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50:
        ball.setx(340)
        ball_dx *= -1
        os.system("afplay paddlehit.wav&")
