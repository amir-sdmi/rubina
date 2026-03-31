import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
colors=["yellow","blue","green","orange"]
for x in range(10000000):
    t.color(colors[x%4])#len(colors) is 4
    t.forward(x)
    t.left(89) #91 



turtle.done()