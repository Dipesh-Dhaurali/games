import turtle
import time
import random

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("green")
screen.setup(width=600, height=600)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

segments = []
score = 0
high_score = 0
delay = 0.1

def write_score():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

def reset():
    global score, delay
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    delay = 0.1
    write_score()

def random_grid_pos():
    return random.randint(-14, 14) * 20

running = True

def quit_game():
    global running
    running = False
    try:
        screen.bye()
    except turtle.Terminator:
        pass

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(quit_game, "q")

write_score()

while running:
    try:
        screen.update()
    except turtle.Terminator:
        break
    time.sleep(delay)

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset()
        continue

    if head.distance(food) < 20:
        x = random_grid_pos()
        y = random_grid_pos()
        food.goto(x, y)
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("gray")
        segment.penup()
        segments.append(segment)
        score += 10
        if score > high_score:
            high_score = score
        delay = max(0.05, delay - 0.001)
        write_score()

    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            reset()
            break
