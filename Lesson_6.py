import math
import random
import turtle

# part_1_1 = math.cos(math.pi/3) + math.log2(16)
# print(part_1_1)
# part_1_2 = sum([math.factorial(n) + 1 for n in range(0, 4)])
# print(part_1_2)
# part_1 = part_1_1 * part_1_2
# print(part_1)
# part_2 = (math.sqrt(25) - abs(-5)) ** math.sin(math.pi/2)
# print(part_2)
# part_3 = (3 ** 2 + 4 ** 2) / 5 * (math.tan(0) + 1)
# print(part_3)
# result = part_1 + part_2 - part_3
# print(result)


# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# fruits.insert(1, "lemon")
# fruits.pop(2)
# print(fruits)


# grades = [85, 90, 78, 92, 88, 76, 95, 89, 100, 72]
# print(min(grades))
# print(max(grades))
# summa = sum(grades)
# print(summa / len(grades))
# print (grades.sort())
 

# for i in range(5):
#     rand_num = random.randint(1, 100)
#     print(rand_num)


# for i in range(5):
#     rand_num = random.uniform(1, 10)
#     print(rand_num)


# life = 5
# random_num = random.randint(1,50)
# isWin = False

# print("Было загадано число от 1 до 49. Попробуй угадать!")
# while life != 0:
#     num = int(input("Введите число: "))

#     if num == random_num:
#         print("Вы победили")
#         isWin = True 
#         break

#     elif num < random_num:
#         print("Загаданное число больше.")
#         life -= 1

#     elif num > random_num:
#         print("Загаданное число меньше.")
#         life -= 1

# if (not isWin):
#     print("Вы проиграли")


# screen = turtle.Screen()
# screen.setup(600, 600)
# screen.bgcolor("lightblue")
# screen.title("Весёлый смайлик - Изучаем Turtle")

# t = turtle.Turtle()
# t.speed(5)
# t.width(3)

# t.penup()
# t.goto(0, -100)
# t.pendown()
# t.color("black", "yellow")
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.penup()
# t.goto(-40, 30)
# t.pendown()
# t.color("black", "white")
# t.begin_fill()
# t.circle(20)
# t.end_fill()

# t.penup()
# t.goto(-40, 40)
# t.pendown()
# t.color("black", "black")
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# t.penup()
# t.goto(40, 30)
# t.pendown()
# t.color("black", "white")
# t.begin_fill()
# t.circle(20)
# t.end_fill()

# t.penup()
# t.goto(40, 40)
# t.pendown()
# t.color("black", "black")
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# t.penup()
# t.goto(-60, -20)
# t.pendown()
# t.color("black")
# t.width(5)
# t.setheading(-60)
# t.circle(70, 120)

# t.hideturtle()
# screen.exitonclick()