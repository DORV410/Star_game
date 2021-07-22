
from turtle import *
import turtle
#Create a back ground of game
wn = turtle.Turtle()
turtle.bgcolor("gray")
turtle.title("Chien Binh Khong Gian")
wn.penup()
wn.speed(0)
wn.color("black")
wn.fillcolor("blue")
wn.setpos(-200,-200)
wn.begin_fill()
wn.pendown()
for side in range(4):
	wn.forward(400)
	wn.left(90)
wn.end_fill()
wn.hideturtle()
#Create enemy
enemy = turtle.Turtle()
enemy.penup()
enemy.shape("circle")
enemy.color("red")
enemy.speed(0)
enemy.setposition(-150,150)
enemyspeed=2
#create player bullet
bullet = turtle.Turtle()
bullet.color("green")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.4,0.4)
bullet.hideturtle()
bulletspeed = 100
bulletstate = "ready"
# Create player
player = turtle.Turtle()
playerspeed = 10
player.color("Black")
player.speed(0)
player.penup()
player.shape("triangle")
player.setposition(0,-190)
player.setheading(90)
# move for player
def moveleft():
	x=player.xcor()
	x-= playerspeed
	if x<-150:
		x=-150
	player.setx(x)
def moveright():
	x=player.xcor()
	x+=playerspeed
	if x >150:
		x=150
	player.setx(x)
def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()	



#keyboard
turtle.listen()
turtle.onkey(moveleft,"Left")
turtle.onkey(moveright,"Right")
turtle.onkey(fire_bullet,"space")



#Main game loop

while True: 
	x= enemy.xcor()
	x+=enemyspeed
	enemy.setx(x)

	if enemy.xcor()>150:
		y=enemy.ycor()
		y-=10
		enemyspeed*=-1
		enemy.sety(y)

	if enemy.xcor() <-150:
		y= enemy.ycor()
		y+=10 
		enemyspeed *= -1
		enemy.sety(y)
	#move the bullet 
	
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	if bullet.ycor()>150:
		bullet.hideturtle()
		bulletstate = "ready"








turtle.exitonclick()

# from turtle import *
# import os 
# import turtle

# # os.getcwd()
# # os.chdir(r"C:\\Users\\Setup\\Desktop\\Python")


# turtle.bgpic('image_2021-01-29_15-20-05.png')

# # player = turtle.textinput("newplayah", "name of first player")
# wn = turtle.Screen()
# wn.title("GAme demo")
# # print(turtle.window_height(),turtle.window_width())
# border_pen = turtle.Turtle()
# border_pen.speed(1000)
# border_pen.color("white")
# border_pen.penup()
# border_pen.setposition(-200,-200)
# border_pen.pendown()
# for side in range(4):
# 	border_pen.fd(400)
# 	border_pen.lt(90)
# border_pen.fillcolor("blue")
# border_pen.filling()
# border_pen.hideturtle()
# # make_enermy

# enemy = turtle.Turtle()
# enemy.penup()
# enemy.shape("circle")
# enemy.color("red")
# enemy.speed(0)
# enemy.setposition(-150,150)
# enemyspeed=50

# #create the player turtle
# player = turtle.Turtle()
# player._color("blue")
# player.shape("triangle")
# player.penup()
# player.speed(0)
# player.setposition(0,-180)
# player.setheading(90)

# playerspeed = 15
# #create player bullet
# bullet = turtle.Turtle()
# bullet.color("green")
# bullet.shape("triangle")
# bullet.penup()
# bullet.speed(0)
# bullet.setheading(90)
# bullet.shapesize(0.4,0.4)
# bullet.hideturtle()
# #keyboard 

# bulletspeed = 100
# bulletstate = "ready"


# # move for player
# def moveleft():
# 	x=player.xcor()
# 	x-= playerspeed
# 	if x<-150:
# 		x=-150
# 	player.setx(x)
# def moveright():
# 	x=player.xcor()
# 	x+=playerspeed
# 	if x >150:
# 		x=150
# 	player.setx(x)
# def fire_bullet():
# 	global bulletstate
# 	if bulletstate == "ready":
# 		bulletstate = "fire"
# 		x = player.xcor()
# 		y = player.ycor() + 10
# 		bullet.setposition(x,y)
# 		bullet.showturtle()	



# #keyboard
# turtle.listen()
# turtle.onkey(moveleft,"Left")
# turtle.onkey(moveright,"Right")
# turtle.onkey(fire_bullet,"space")



# #Main game loop

# while True: 
# 	x= enemy.xcor()
# 	x+=enemyspeed
# 	enemy.setx(x)

# 	if enemy.xcor()>150:
# 		y=enemy.ycor()
# 		y-=10
# 		enemyspeed*=-1
# 		enemy.sety(y)

# 	if enemy.xcor() <-150:
# 		y= enemy.ycor()
# 		y+=10 
# 		enemyspeed *= -1
# 		enemy.sety(y)
# 	#move the bullet 
	
# 	if bulletstate == "fire":
# 		y = bullet.ycor()
# 		y += bulletspeed
# 		bullet.sety(y)
# 	if bullet.ycor()>150:
# 		bullet.hideturtle()
# 		bulletstate = "ready"



# end = input("please enter to finish")