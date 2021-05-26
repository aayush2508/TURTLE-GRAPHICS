import turtle
colors = ["red","blue","orange","purple","yellow","green"]
pen  = turtle.Pen()
turtle. bgcolor("black")
for i in range (360):
    pen.pencolor(colors[i%6])
    pen.width(i/100+1)
    pen.forward(i)
    pen.left(60)
    
