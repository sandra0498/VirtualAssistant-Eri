import turtle


visuals = turtle.Turtle()

visuals.color('blue', 'purple')
visuals.begin_fill()
visuals.speed(50)
while True:
    visuals.forward(200)
    visuals.left(170)
    if abs(visuals.pos()) < 1:
        break
visuals.end_fill()
turtle.done()
