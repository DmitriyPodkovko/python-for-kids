import turtle
t = turtle.Pen()

def star(l, fill, k):
    if fill: t.begin_fill()
    for x in range(1, k):
        t.forward(l)
        if x % 2 == 0: t.left(175)
        else: t.left(225)
    if fill: t.end_fill()
        
t.color(0.9, 0.75, 0)
star(120, True, 25)

t.color(0, 0, 0)
star(120, False, 25)
