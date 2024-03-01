# 计算两点距离
import turtle,math

# 定义多个点坐标
x1,y1,x2,y2,x3,y3,x4,y4 = 100,100,100,-100,-100,-100,-100,100


turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)


distances = math.sqrt((x1-x4)**2+(y1-y4)**2)
turtle.write(distances)

turtle.done()