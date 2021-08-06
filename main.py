import turtle
import random
import math

screen = turtle.Screen()
screen.setup(800, 500)
screen.bgpic("Webp.net-resizeimage.gif")
screen.tracer(0)
screen.addshape("Webp.net-resizeimage.png")
screen.addshape("sasuke-removebg-preview (1).png")
screen.addshape("rasengan-removebg-preview (1).png")
screen.addshape("Webp.net-resizeimage (1).png")
screen.tracer(0)

#Score Variables
p1score = 0
p2score = 0

#Paddle A creation
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("Webp.net-resizeimage.png")
paddleA.left(90)
paddleA.color("#00F7FF")
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B creation
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.left(90)
paddleB.shape("sasuke-removebg-preview (1).png")
paddleB.color("#FF003E")
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("rasengan-removebg-preview (1).png")
ball.color("#00FF80")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#Score Writer
scorepen1 = turtle.Turtle()
scorepen1.hideturtle()
scorepen1.speed(0)
scorepen1.color("#FFFB00")
scorepen1.penup()
scorepen1.goto(-120, 200)
scorestring = "%s" %p1score
scorepen1.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))

scorepen2 = turtle.Turtle()
scorepen2.hideturtle()
scorepen2.speed(0)
scorepen2.color("#FFFB00")
scorepen2.penup()
scorepen2.goto(120, 200)
scorestring = "%s" %p2score
scorepen2.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))

def pAup():
  y = paddleA.ycor()
  y += 20
  paddleA.sety(y)
  
def pAdown():
  y = paddleA.ycor()
  y -= 20
  paddleA.sety(y)
  
def pBup():
  y = paddleB.ycor()
  y += 20
  paddleB.sety(y)
  
def pBdown():
  y = paddleB.ycor()
  y -= 20
  paddleB.sety(y)
  
def collision(t1, t2):
  dist = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
  if dist < 30:
    return True
  else:
    return False
    
def scoreupdate(player):
  if(player == 1):
    scorepen1.clear()
    scorestring = "%s" %p1score
    scorepen1.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))
  if(player == 2):
    scorepen2.clear()
    scorestring = "%s" %p2score
    scorepen2.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))

screen.listen()
screen.onkey(pAup, "W")
screen.onkey(pAdown, "S")
screen.onkey(pBup, "Up")
screen.onkey(pBdown, "Down")

#Main Loop
game = True
while game:
  screen.update()
  #Ball Move
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)
  
  #Border Creation
  if ball.ycor() > 240:
    ball.sety(240)
    ball.dy *= -1
  if ball.ycor() < -240:
    ball.sety(-240)
    ball.dy *= -1
    
  if ball.xcor() > 390:
    ball.hideturtle()
    ball.goto(0,0)
    ball.showturtle()
    ball.dx *= -1
    p1score+=1
    scoreupdate(1)
    
  if ball.xcor() < -390:
    ball.hideturtle()
    ball.goto(0,0)
    ball.showturtle()
    ball.dx *= -1
    p2score+=1
    scoreupdate(2)
    
  if paddleA.ycor() > 240:
    y = 240
    paddleA.sety(y)
    
  if paddleA.ycor() < -240:
    y = -240
    paddleA.sety(y)
    
  if paddleB.ycor() > 240:
    y = 240
    paddleB.sety(y)
    
  if paddleB.ycor() < -240:
    y = -240
    paddleB.sety(y)
    
  #Paddle Ball Collision
  if collision(paddleA, ball):
    ball.dx *= -1
    ball.shape("rasengan-removebg-preview (1).png")
    
  if collision(paddleB, ball):
    ball.dx *= -1
    ball.shape("Webp.net-resizeimage (1).png")
    
  if p1score >= 10:
    break
  if p2score >= 10:
    break
  
  
