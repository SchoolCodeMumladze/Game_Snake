from tkinter import simpledialog

def getUserText():
    user_text = simpledialog.askstring("Nickname","Введите ник:")
    return user_text

nickname = getUserText()

import os

#Загружаем рекорд из файла
def load_h():
    if os.path.exists("Nicknames_and_records.txt"):
        try:
            with open("Nicknames_and_records.txt", "r", encoding="utf-8") as f:
                return int(f.read())
        except:
            return 0
    return 0

#Сохраняем рекорды в файл
def save_h():
    with open("Nicknames_and_records.txt", "w+", encoding="utf-8") as f:
        new_record = f"{nickname}:{str(counter)} \n"
        f.write(new_record)


print(f"Hello, {nickname}!")
print("Management:W,A,S,D")
print("(Please,turn on the English layout)")
import ipg
import management
import turtle
import time
import random
import winsound

counter=0
high_score=load_h()
delay=0.1
segments=[]

management.keys()
#Основной игровой цикл
try:
    while True:
        ipg.window.update()

        #Проверка столкновения со стеной
        if ipg.head.xcor()>395 or ipg.head.xcor()<-395 or ipg.head.ycor()>295 or ipg.head.ycor()<-290:
            winsound.PlaySound("the-sound-of-losing.wav", winsound.SND_ASYNC)
            time.sleep(1)
            ipg.head.goto(0,0)
            ipg.head.direction="stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            counter=0
            delay=0.1
            ipg.score.clear()
            ipg.score.write(f"Score:{counter},Record:{high_score}",align="center",font=("Courier",14,"normal"))

        #Проверка столкновения с яблоком
        if ipg.head.distance(ipg.apple)<20:
            winsound.PlaySound("apple-bite-short.wav", winsound.SND_ASYNC)
            #Перемещаем еду в случайное место
            x=random.randint(-385,385)
            y=random.randint(-285,285)
            ipg.apple.goto(x,y)
            #Увеличение скорости при столкновении с яблоком
            for i in range(10):
                ipg.head.speed(i+1)

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
                save_h()
            ipg.score.clear()
            ipg.score.write(f"Score:{counter},Record:{high_score}",align="center",font=("Courier",14,"normal"))
            if delay>0.05:
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
                winsound.PlaySound("the-sound-of-losing.wav", winsound.SND_ASYNC)
                time.sleep(1)
                ipg.head.goto(0,0)
                ipg.head.direction="stop"
                for segment1 in segments:
                    segment1.goto(1000,1000)
                segments.clear()
                counter=0
                delay=0.1
                ipg.score.clear()
                ipg.score.write(f"Score:{counter},Record:{high_score}",align="center",font=("Courier",14,"normal"))

        time.sleep(delay)

except (turtle.Terminator,Exception):
    print("Game Over")
    print(f"Score: {high_score}")
finally:
    try:
        ipg.window.mainloop()
    except:
        pass