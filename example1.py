import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("yellow")
alex.right(150)

colours = ["yellow", "blue", "brown", "green", "teal"]

for colour in colours:
    if alex.color() == "yellow":
        alex.left(50)
        alex.forward(120)
    elif alex.color() == "blue":
        alex.left(55)
        alex.forward(130)
    elif alex.color() == "brown":
        alex.right(50)
        alex.forward(110)
    elif alex.color() == "green":
        alex.left(65)
        alex.forward(100)
    elif alex.color() == "teal":
        alex.left(80)
        alex.forward(100)

alex.pencolor(colour)

'''import turtle
wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("Pink")
amy.right(170)

colors = ["Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Orange", "Pink", "Pink", "Orange", "Yellow", "Purple", "Orange", "Purple", "Yellow", "Orange", "Pink", "Orange", "Purple", "Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Yellow"]


for color in colors:
    if amy.pencolor() == "Purple":
        amy.forward(50)
        amy.right(59)
    elif amy.pencolor() == "Yellow":
        amy.forward(65)
        amy.left(98)
    elif amy.pencolor() == "Orange":
        amy.forward(30)
        amy.left(60)
    elif amy.pencolor() == "Pink":
        amy.forward(50)
        amy.right(57)

    amy.pencolor(color)'''