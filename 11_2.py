import turtle
t = turtle.Pen()

def vosmikutnyk(l, fill):
    if fill:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(l)
        t.left(45)
    if fill:
        t.end_fill()
        
t.color(0.9, 0.75, 0)
vosmikutnyk(50, True)

t.color(0, 0, 0)
vosmikutnyk(50, False)
