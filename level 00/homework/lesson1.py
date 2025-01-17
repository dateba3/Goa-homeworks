from turtle import *  

#make squre
speed(30)
width(7)
color("brown")
forward(200)
left(90)               
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
#end of squre

#make door

color("orange")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end of door

#make roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#make window
penup()
goto(200, 130)
pendown()

color("blue")
begin_fill()
right(60)
forward(60)
right(90)
forward(60)     #height of window
right(90)
forward(60)
right(90)
forward(60)
end_fill()

penup()
goto(0,  130)
pendown()

color("blue")
begin_fill()
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()




exitonclick()