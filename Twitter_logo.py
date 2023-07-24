from turtle import *

setup(720, 640)
BLUE = '#3C96D1'
WHITE = 'white'
bgcolor(WHITE)


def circ(x, y, r, c, sa=0, se=360):
    up()
    goto(x, -y)
    seth(sa)
    fd(r)
    lt(90)
    down()
    color(c)
    begin_fill()
    circle(r, se-sa)
    end_fill()


R1 = 276.38
R2 = 195.40
R3 = 97.12

circ(-86.07, -83.12, R1, BLUE, 210, 385)
circ(-213.20, -46.26, R2, WHITE, 180, 330)

circ(-91.53, 10.89, R3, BLUE, 180, 360)
circ(-165.43, -54.50, R3, WHITE, 200, 360)
circ(-121.10, -57.10, R3, BLUE, 170, 370)
circ(-170.23, -141.70, R3, WHITE, 210, 360)
circ(-118.86, -126.53, R3, BLUE, 135, 360)

circ(74.28, -255.43, R2, BLUE, 210, 330)
circ(158.28, -327.35, R2, WHITE, 210, 330)

circ(11.54, -350.11, R1, WHITE, 210, 330)

circ(131.58, -215.44, R3, BLUE, 180, 360)
circ(123.87, -351.55, R2, WHITE, 210, 330)

circ(92.11, -96.20, R3, BLUE, 0, 220)

hideturtle()
done()