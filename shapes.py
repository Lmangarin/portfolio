from turtle import *


sides = int(input("Enter number of sides:"))
angle = 360/sides
Color = input("Enter color:")
pencolor (Color)
fillcolor (Color)
pensize = input ("Enter pen size:")
width (pensize)


print ("sides:", sides, "angle:", angle)
for i in range(25):
        penup()
        setpos(0,0)
        pendown()
        speed(10)
        begin_fill()
        width (5)
        forward (200)
        left (angle)
        forward (200)
        left (angle)
        forward (200)
        left (angle)
        forward (200)
        left (angle)
        end_fill()

exitonclick()
