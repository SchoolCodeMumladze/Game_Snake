import ipg

#Управление
def go_up():
    if ipg.head.direction != "down":
        ipg.head.direction = "up"
def go_down():
    if ipg.head.direction != "up":
        ipg.head.direction = "down"
def go_left():
    if ipg.head.direction != "right":
        ipg.head.direction = "left"
def go_right():
    if ipg.head.direction != "left":
        ipg.head.direction = "right"

def move():
    if ipg.head.direction == "up":
        y=ipg.head.ycor()
        ipg.head.sety(y+20)
    if ipg.head.direction == "down":
        y=ipg.head.ycor()
        ipg.head.sety(y-20)
    if ipg.head.direction == "left":
        x=ipg.head.xcor()
        ipg.head.setx(x-20)
    if ipg.head.direction == "right":
        x=ipg.head.xcor()
        ipg.head.setx(x+20)

#Обработка нажатия клавиш
def keys():
    ipg.window.listen()
    ipg.window.onkeypress(go_up,"w")
    ipg.window.onkeypress(go_down,"s")
    ipg.window.onkeypress(go_left,"a")
    ipg.window.onkeypress(go_right,"d")
