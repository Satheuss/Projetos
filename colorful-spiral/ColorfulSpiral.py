import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","purple","orange"]

for i in range(400):
    t.color(colors[i % 6])
    t.circle(i)
    t.left(59)

turtle.done()