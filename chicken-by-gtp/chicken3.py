import turtle

def draw_chicken():
    # Set up the screen
    wn = turtle.Screen()
    wn.title("Chicken Drawing")

    # Set up the turtle
    chicken = turtle.Turtle()
    chicken.speed(1)

    # Draw body
    chicken.begin_fill()
    chicken.circle(50, 180)
    chicken.right(90)
    chicken.forward(100)
    chicken.right(90)
    chicken.circle(50, 180)
    chicken.end_fill()

    # Draw left wing
    chicken.penup()
    chicken.goto(-50, 25)
    chicken.pendown()
    chicken.setheading(-30)
    chicken.begin_fill()
    chicken.circle(30, 180)
    chicken.right(90)
    chicken.forward(60)
    chicken.right(90)
    chicken.circle(30, -180)
    chicken.end_fill()

    # Draw right wing
    chicken.penup()
    chicken.goto(50, 25)
    chicken.pendown()
    chicken.setheading(30)
    chicken.begin_fill()
    chicken.circle(-30, 180)
    chicken.left(90)
    chicken.forward(60)
    chicken.left(90)
    chicken.circle(-30, -180)
    chicken.end_fill()

    # Draw head
    chicken.penup()
    chicken.goto(0, 100)
    chicken.pendown()
    chicken.setheading(0)
    chicken.begin_fill()
    chicken.circle(25)
    chicken.end_fill()

    # Draw beak
    chicken.penup()
    chicken.goto(20, 110)
    chicken.pendown()
    chicken.color("orange")
    chicken.begin_fill()
    chicken.setheading(-30)
    chicken.forward(15)
    chicken.left(120)
    chicken.forward(15)
    chicken.left(120)
    chicken.forward(15)
    chicken.end_fill()
    chicken.color("black")

    # Draw left eye
    chicken.penup()
    chicken.goto(-15, 130)
    chicken.pendown()
    chicken.dot(5)

    # Draw right eye
    chicken.penup()
    chicken.goto(5, 130)
    chicken.pendown()
    chicken.dot(5)

    # Draw left leg
    chicken.penup()
    chicken.goto(-25, 0)
    chicken.pendown()
    chicken.color("orange")
    chicken.setheading(-110)
    chicken.forward(50)
    chicken.right(45)
    chicken.forward(15)
    chicken.right(180)
    chicken.forward(15)
    chicken.right(45)
    chicken.forward(15)

    # Draw right leg
    chicken.penup()
    chicken.goto(25, 0)
    chicken.pendown()
    chicken.setheading(-70)
    chicken.forward(50)
    chicken.left(45)
    chicken.forward(15)
    chicken.left(180)
    chicken.forward(15)
    chicken.left(45)
    chicken.forward(15)
    chicken.color("black")

    # Hide turtle
    chicken.hideturtle()

    # Keep the window open
    wn.mainloop()

draw_chicken()
