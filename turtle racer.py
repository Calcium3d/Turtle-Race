import turtle
import random
import time

delay = 0.05

y = -260
edge = 260
x = 0
w = 80

green_score = 0
red_score = 0
blue_score = 0

# screen

window = turtle.Screen()
window.title("Turtle race by AwsomemanNever")
window.setup(600, 400)
window.bgcolor("black")
window.tracer(0)

# turtles

green_racer = turtle.Turtle()
green_racer.speed(0)
green_racer.shape("turtle")
green_racer.color("green")
green_racer.penup()
green_racer.goto(y, 0)
green_racer.pendown()

red_racer = turtle.Turtle()
red_racer.speed(0)
red_racer.shape("turtle")
red_racer.color("red")
red_racer.penup()
red_racer.goto(y, 40)
red_racer.pendown()

blue_racer = turtle.Turtle()
blue_racer.speed(0)
blue_racer.shape("turtle")
blue_racer.color("blue")
blue_racer.penup()
blue_racer.goto(y, -40)
blue_racer.pendown()

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-140, -120)
pen.write("Green Turtle Score: {}".format(green_score), align="center", font=("Courier", 24, "normal"))
pen.goto(-153, -150)
pen.write("Red Turtle Score: {}".format(red_score), align="center", font=("Courier", 24, "normal"))
pen.goto(-147, -180)
pen.write("Blue Turtle Score: {}".format(blue_score), align="center", font=("Courier", 24, "normal"))

racer_list = ["green_racer", "red_racer", "blue_racer"]

for i in range(8):
    white = turtle.Turtle()
    white.penup()
    white.speed(0)
    white.shape("square")
    white.color("white")
    white.goto(edge, w)
    w -= 20


# functions
def go():
    time.sleep(delay)
    go_or_no = random.randint(0, 1)
    choice = random.choice(racer_list)
    if go_or_no == 1:
        if choice == "green_racer":
            x = green_racer.xcor()
            green_racer.setx(x + 20)
        if choice == "red_racer":
            x = red_racer.xcor()
            red_racer.setx(x + 20)
        if choice == "blue_racer":
            x = blue_racer.xcor()
            blue_racer.setx(x + 20)


while True:

    window.update()

    if green_racer.xcor() == edge or red_racer.xcor() == edge or blue_racer.xcor() == edge:
        # resetting positions

        time.sleep(delay)

        pen.clear()

    go()

    if green_racer.xcor() == edge or red_racer.xcor() == edge or blue_racer.xcor() == edge:
        # resetting positions

        time.sleep(delay)

        pen.clear()

        if green_racer.xcor() == edge:
            green_score += 10
        if red_racer.xcor() == edge:
            red_score += 10
        if blue_racer.xcor() == edge:
            blue_score += 10

        green_racer.goto(y, 0)
        red_racer.goto(y, 40)
        blue_racer.goto(y, -40)
        green_racer.clear()
        red_racer.clear()
        blue_racer.clear()

    pen.goto(-140, -120)
    pen.write("Green Turtle Score: {}".format(green_score), align="center", font=("Courier", 24, "normal"))
    pen.goto(-153, -150)
    pen.write("Red Turtle Score: {}".format(red_score), align="center", font=("Courier", 24, "normal"))
    pen.goto(-147, -180)
    pen.write("Blue Turtle Score: {}".format(blue_score), align="center", font=("Courier", 24, "normal"))

window.mainloop()
