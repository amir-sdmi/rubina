import turtle

t = turtle.Turtle()
t.shape("turtle")


for x in range(3):
    t.forward(100)
    t.right(90)


t.forward(100)
t.right(30)


t.forward(100)
t.right(120)
t.forward(100)


turtle.done()