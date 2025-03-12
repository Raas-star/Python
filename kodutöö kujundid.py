import turtle
import random

def draw_kujund(kujund):
    if kujund == "ruut":
        for _ in range(4):
            turtle.forward(50)
            turtle.right(90)
    elif kujund == "ring":
        turtle.circle(25)
    elif kujund == "viisnurk":
        for _ in range(5):
            turtle.forward(50)
            turtle.right(72)

type = input("Kujund (ruut, ring, viisnurk, suvaline): ")
num = int(input("Mitu kujundit? "))

for _ in range(num):
    if type == "suvaline":
        type = random.choice(["ruut", "ring", "viisnurk"])
    draw_kujund(type)
    turtle.forward(100)

turtle.exitonclick()
