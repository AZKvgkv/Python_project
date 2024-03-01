# 绘制不同颜色的同心圆
import turtle

p = turtle.Pen()
p.width(4)

radius = [x*10 for x in range(1,6)]
My_colors = ('red','green','black','brown','purple')

for r,i in zip(radius,range(len(radius))):
    p.penup()
    p.goto(0,-r)
    p.pendown()
    p.color(My_colors[i%len(My_colors)])
    p.circle(r)

turtle.done()