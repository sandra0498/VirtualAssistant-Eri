from turtle import *


color('blue', 'purple')
begin_fill()
speed(50)
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
