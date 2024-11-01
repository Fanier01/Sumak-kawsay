import turtle
import random


turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.bgcolor("black")
turtle.color("white")

def edificio(x, y, x_i, y_i):
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.sety(y_i + y)
    turtle.setx(x_i + x)
    turtle.sety(y_i)
    turtle.setx(x_i)
    turtle.end_fill()

    techos(x_i + x, y_i + y, x_i, x)

def techos(x , y, x_i, medio):
    x_p = random.randint(0 , medio)
    y_p = random.randint(30, 50)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.goto(x - x_p ,y + y_p)
    turtle.goto(x_i, y)
    turtle.goto(x, y)
    turtle.end_fill()


def llama_funcion():
    index = 0
    fin = 5
    x_de_inicio = -300
    while index < fin:
        x = random.randint(80, 130)
        y = random.randint(140, 200)
        edificio(x, y, x_de_inicio, 0)
        x_de_inicio += x
        turtle.penup()
        turtle.goto(x_de_inicio, 0)
        turtle.pendown()
        index += 1
    turtle.exitonclick()

llama_funcion()
#buenas noches
#desde android