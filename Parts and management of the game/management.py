from individual_parts_of_the_game import head
from individual_parts_of_the_game import window

#Управление
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)

#Обработка нажатия клавиш
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
