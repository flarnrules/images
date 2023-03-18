import turtle

def draw_chicken():
    # Set up the screen
    wn = turtle.Screen()
    wn.title("Chicken Drawing")

    # Set up the turtle
    chicken = turtle.Turtle()
    chicken.speed(1)

    # Draw body
    chicken.circle(50)

    # Draw left wing
    chicken.penup()
    chicken.goto(-10, 50)
    chicken.pendown()
    chicken.circle(30, 180)

    # Draw right wing
    chicken.penup()
    chicken.goto(10, 50)
    chicken.pendown()
    chicken.circle(-30, -180)

    # Draw head
    chicken.penup()
    chicken.goto(0, 100)
    chicken.pendown()
    chicken.circle(25)

    # Draw beak
    chicken.penup()
    chicken.goto(25, 125)
    chicken.pendown()
    chicken.right(45)
    chicken.forward(15)
    chicken.right(90)
    chicken.forward(15)

    # Draw left eye
    chicken.penup()
    chicken.goto(-10, 140)
    chicken.pendown()
    chicken.dot(5)

    # Draw right eye
    chicken.penup()
    chicken.goto(10, 140)
    chicken.pendown()
    chicken.dot(5)

    # Draw left leg
    chicken.penup()
    chicken.goto(-25, 0)
    chicken.pendown()
    chicken.right(90)
    chicken.forward(50)

    # Draw right leg
    chicken.penup()
    chicken.goto(25, 0)
    chicken.pendown()
    chicken.forward(50)

    # Hide turtle
    chicken.hideturtle()

    # Keep the window open
    wn.mainloop()

draw_chicken()
