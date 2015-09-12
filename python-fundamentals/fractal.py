import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("#411F35")
	cup = turtle.Turtle()
	cup.shape("turtle")
	cup.color("yellow")


	window.exitonclick()

draw_art()