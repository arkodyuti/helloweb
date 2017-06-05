import turtle

window = turtle.Screen()
window.setup(400,400)
window.bgcolor("lightgreen")
#window.bgpic("pic.jpg")
rick = turtle.Turtle()
rick.penup()
rick.setx(100)
rick.sety(100)
rick.pendown()

#event handler functions
def event_up():
   rick.forward(30)

def event_left():
   rick.left(45)

def event_right():
   rick.right(45)

def event_down():
    rick.backward(30)

def event_penup():
	rick.penup()

def event_pendown():
	rick.pendown()

def quit():
  window.bye()


#defined key presses
window.onkey(event_up, "Up")
window.onkey(event_left, "Left")
window.onkey(event_right, "Right")
window.onkey(event_down, "Down")
window.onkey(quit, "q")
window.onkey(event_penup, "space")


window.listen()
turtle.done()
