import turtle

high_score=0

#Экран игры
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("SeaGreen")
window.setup(width=600, height=500)
window.tracer(0)
window.cv._rootwindow.resizable(False, False)

#Тело змейки
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("DarkGreen")
head.penup()
head.goto(0,0)
head.direction = "stop"
segments=[]

#Яблоко
apple=turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(100,0)

#Отображение счета
score=turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(f"Счёт:{score},Рекорд:{high_score}")

window.mainloop()
