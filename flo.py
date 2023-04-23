import turtle
import colorsys
s=turtle.getscreen()
s=turtle.bgcolor('black')
t1=turtle.Turtle()
t1.speed(50)
t1.pensize(3)
hue=0.0

for i in range(300):
 col=colorsys.hsv_to_rgb(hue,1,1)
 t1.pencolor(col)
 hue+=0.005
 t1.circle(5-i,100)
 t1.lt(80)
 t1.circle(5-i,100)
 t1.rt(100)