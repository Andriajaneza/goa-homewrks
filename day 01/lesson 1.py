from turtle import *


#we want to paint house

#step 1:draw a square

speed(30)

begin_fill()
color("purple")
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

#end of square 

#start drawing a door

begin_fill()
left(90)
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end of drawing a door

#start drawing a roof


penup()
goto (200, 200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of drawing a roof

#start a drawing windows

penup()
goto(7, 70)
pendown()


color("brown")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(193, 120)
pendown()

begin_fill()
forward(50) 
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#end of drawing windows
exitonclick()

#the end