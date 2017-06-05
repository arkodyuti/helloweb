import turtle
wn = turtle.Screen()
rick = turtle.Turtle()
while True:
	x = raw_input("Enter Command:").split(" ")
	if x[0] == "forward":
		rick.forward(int(x[1]))
	elif x[0] == "left":
		rick.left(int(x[1]))
	elif x[0] == "right":
		rick.right(int(x[1]))
	elif x[0] == "backward":
		rick.backward(int(x[1]))
	elif x[0] == "color":
		rick.pencolor("red")
	elif x[0] == "exit":
		break

