import turtle
penSize = str(input("How many pixels would you like the pen to be: "))
penColour = str(input("What colour would you like the pen to be: "))
bgColour = str(input("What colour would you like the background to be: "))
wn = turtle.Screen()
turtle.bgcolor(bgColour)
alex = turtle.Turtle()
alex.color(penColour)
alex.pensize(penSize)
for i in range(8):
    for i in range(3):
        for i in range(3):
            alex.forward(30)
            alex.backward(30)
            alex.right(45)
        alex.left(90)
        alex.backward(30)
        alex.left(45)
    alex.right(90)
    alex.forward(90)
    alex.left(45)
