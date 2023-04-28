import turtle
import math

unit = 50

def draw_xy():
    t = turtle.Turtle()
    t.fd(300)
    t.bk(600)
    t.left(90)
    t.fd(100)
    t.bk(200)
    t.hideturtle()
    
    
# 파형을 그리는 함수
def draw_wave(amp, freq, theta, c):
    # turtle 객체를 생성합니다.
    t = turtle.Turtle()
    t.speed(0)
    t.pencolor(c)

    # 시작 위치를 설정합니다.
    t.up()
    t.goto(-300, 0)
    t.down()

    st = 0.0
    # sin 파형을 그립니다.
    for x in range(-300, 300):
        
        y = amp * math.sin(2 * math.pi * freq * st + theta)
        t.goto(x, y * unit)
        st += 0.005

    # turtle 객체를 닫습니다.
    # turtle.done()


# 파형의 진폭과 주파수를 설정합니다.
amplitude = 3
frequency = 1

draw_xy()
# 파형을 그립니다.
draw_wave(amplitude, frequency, 0, "blue")
draw_wave(1, 3, 0, "red")
