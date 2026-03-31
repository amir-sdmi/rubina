import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

colors=["yellow","blue","green","orange",]

for x in range(30000000000000000000000000000000):
    t.color(colors[x%len(colors)])
    t.circle(x)
    t.left(179)
 



turtle.done()