import turtle
import random

t = turtle.Turtle()
w = turtle.Screen()


def tree(branchLen, t):
    if branchLen > 3:
        if 8 <= branchLen <= 12:
            if random.randint(0, 2) == 0:
                t.color('green yellow')
            else:
                t.color('spring green')
            t.pensize(branchLen / 3)
        elif branchLen < 8:
            if random.randint(0, 1) == 0:
                t.color('green yellow')
            else:
                t.color('spring green')
            t.pensize(branchLen / 2)
        else:
            t.color('sienna4')
            t.pensize(branchLen / 10)

        t.forward(branchLen)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        tree(branchLen - 10 * b, t)
        t.left(40 * a)
        tree(branchLen - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branchLen)
        t.down()


def petal(m, t):  # 落叶
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color("gold2")
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.getscreen().tracer(5, 0)
    turtle.screensize(bg='turquoise1')
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    tree(60, t)
    petal(100, t)

    myWin.exitonclick()


main()

