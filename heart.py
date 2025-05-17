import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pulsing Heart")

# Create a turtle object
heart = turtle.Turtle()
heart.speed(0)
heart.color("black")

def draw_heart(scale=1):
    heart.clear()  # Clear previous frame
    heart.penup()
    heart.goto(0, 0)  # Start at screen center
    heart.pendown()
    heart.begin_fill()
    heart.setheading(140)  # Adjusted angle for symmetry
    heart.forward(180 * scale)
    heart.circle(-90 * scale, 200)
    heart.setheading(60)
    heart.circle(-90 * scale, 200)
    heart.forward(180 * scale)
    heart.end_fill()
    heart.hideturtle()

# Pulsing animation
while True:
    for i in range(10):
        draw_heart(1 + 0.03 * i)  # Scale up
        time.sleep(0.05)
    for i in range(10):
        draw_heart(1.3 - 0.03 * i)  # Scale down
        time.sleep(0.05)