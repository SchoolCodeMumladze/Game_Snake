print("Management:W,A,S,D")
print("(Включите английскую раскладку)")
import ipg
import management
import turtle
import time
import random

counter=0
high_score=0
delay=0.1
segments=[]

management.keys()

#Основной игровой цикл
try:
    while True:
        ipg.window.update()

        #Проверка столкновения со стеной
        if ipg.head.xcor()>395 or ipg.head.xcor()<-395 or ipg.head.ycor()>295 or ipg.head.ycor()<-290:
            time.sleep(1)
            ipg.head.goto(0,0)
            ipg.head.direction="stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            counter=0
            delay=0.1
            ipg.score.clear()
            ipg.score.write(f"Счёт:{counter},Рекорд:{high_score}",align="center",font=("Courier",14,"normal"))

        #Проверка столкновения с едой
        if ipg.head.distance(ipg.apple)<20:
            #Перемещаем еду в случайное место
            x=random.randint(-385,385)
            y=random.randint(-285,285)
            ipg.apple.goto(x,y)

            #Добавляем сегмент тела
            new_s=turtle.Turtle()
            new_s.speed(0)
            new_s.shape("square")
            new_s.color("DarkGreen")
            new_s.penup()
            segments.append(new_s)

            #Увеличиваем счет
            counter+=10
            if counter>high_score:
                high_score=counter
            ipg.score.clear()
            ipg.score.write(f"Счёт:{counter},Рекорд:{high_score}",align="center",font=("Courier",14,"normal"))

            delay-=0.001

        #Движение змейки
        for index in range(len(segments)-1,0,-1):
            x=segments[index-1].xcor()
            y=segments[index-1].ycor()
            segments[index].goto(x,y)
        if len(segments)>0:
            x=ipg.head.xcor()
            y=ipg.head.ycor()
            segments[0].goto(x,y)

        management.move()

        #Проверка столкновения с телом
        for segment in segments:
            if segment.distance(ipg.head)<20:
                time.sleep(1)
                ipg.head.goto(0,0)
                ipg.head.direction="stop"
                for segment1 in segments:
                    segment1.goto(1000,1000)
                segments.clear()
                counter=0
                delay=0.1
                ipg.score.clear()
                ipg.score.write(f"Счёт:{counter},Рекорд:{high_score}",align="center",font=("Courier",14,"normal"))

        time.sleep(delay)

except turtle.Terminator:
    print("Game Over")
except Exception as e:
    print(f"An error has occurred:{e}")
finally:
    try:
        ipg.window.mainloop()
    except:
        pass