"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
from turtle import *

from freegames import square, vector
num = 10

food = vector(0, 0)
snake = [vector(num, 0)]
aim = vector(0, -num)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -210 < head.x < 200 and -210 < head.y < 200


def move():
    "Move snake forward one segment."
    global num
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        # 碰壁显示9宽的红色
        square(head.x-1, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * num
        food.y = randrange(-15, 15) * num
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9,'green')
    update()
    ontimer(move, 200)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(num, 0), 'Right')
onkey(lambda: change(-num, 0), 'Left')
onkey(lambda: change(0, num), 'Up')
onkey(lambda: change(0, -num), 'Down')
move()
done()