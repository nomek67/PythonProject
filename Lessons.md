# Мой конспект

## Мой первый калькулятор
```
print("Введите первое число: ")
numberA = int(input())

print("Введите второе число: ")
numberB = int(input())

print(f"Сумма чисел {numberA} и {numberB} = {numberA + numberB}")
print(f"Разность чисел {numberA} и {numberB} = {numberA - numberB}")
print(f"Произведение чисел {numberA} и {numberB} = {numberA * numberB}")
print(f"Частное чисел {numberA} и {numberB} = {numberA / numberB}")
```

## Конвертация (Parsing):
```
print(str(55))
print(type(str(55)))
print(str(0.32))
print(type(str(0.32)))

print(float(432))
print(type(float(432)))
print(float(23))
print(type(float(23)))

print(int(6.44))
print(type(int(6.44)))
print(int(23.32))
print(type(int(23.32)))
```

## Дополнительные операторы деления (%, //)
```

print(f"Результат остаточного деления числа 435 на 23 = {435 % 23}")
print(f"Результат остаточного деления числа 543 на 246 = {543 % 246}")
print(f"Результат целочисленного деления числа 400 на 20 = {400 // 20}")
```

## Работа с условными конструкциями

*Условные операторы*: **if/elif/else**
```

myAge = int(input("Введите ваш возраст: "))

if(myAge >= 0 and myAge < 13):
    print("Вы ребёнок")
elif (myAge >= 0 and myAge < 20):
    print("Вы подросток")
elif (myAge >= 0 and myAge < 60):
    print("Вы взрослый")
else:
    print("Вы уже пенсионер")
```

## Мой первый проект: определитель возраста
```

now_year = 2025
now_month = 10
now_date = 5

birth_year = int(input("Введите ваш год рождения: "))
birth_month = int(input("Введите число вашего месяца рождения: "))
birth_date = int(input("Введите вашу дату рождения: "))

age = now_year - birth_year

if(now_month > birth_month):
    print("Вам", age, "лет")
elif(now_month == birth_month):
    if(now_day >= birth_day):
        print("Вам", age, "лет")
    else: 
        print("Вам", age - 1, "лет")
else:
    print("Вам", age - 1, "лет")
```

## Цикл WHILE
```

age = 0

while age < 18:
    print(f"Мне {age} лет. Я ребёнок")
    age += 1
print("Пора в универ!")


i = 0
while i < 5:
    print("Привет")
    i += 1
```

## Задача с циклом WHILE
```

# while randomNumber != inputNumber:
#     if randomNumber < inputNumber:
#         print("Загаданное число меньше")
#     else: 
#         print("Загаданное число больше")
#     inputNumber = int(input("Попробуйте ещё раз: "))
```

## Цикл FOR
```

for i in range(0, 51):
    print(Hello, world)
```

## Задача с циклом FOR
```

summa = 0
N = int(input("Введите число"))
for i in range(1, N + 1):  
    summa += i
    print (summa)

summa = 1
N = int(input("Введите число"))
for i in range(1, N * 1):  
    summa *= i
    print (summa)
```

## Практика с циклом WHILE
```

a = 1
b = 1

while a != 0:
    b *= a
    a = (int(input("Введите число: ")))
print(b)
```

## Практика с циклом FOR
```

for i in range(1, 101):
    if i %3 != 0 and i %5 != 0:
     print(i)
```

## Пример с библиотекой MATH
```

part_1_1 = math.cos(math.pi/3) + math.log2(16)
print(part_1_1)
part_1_2 = sum([math.factorial(n) + 1 for n in range(0, 4)])
print(part_1_2)
part_1 = part_1_1 * part_1_2
print(part_1)
part_2 = (math.sqrt(25) - abs(-5)) ** math.sin(math.pi/2)
print(part_2)
part_3 = (3 ** 2 + 4 ** 2) / 5 * (math.tan(0) + 1)
print(part_3)
result = part_1 + part_2 - part_3
print(result)
```

## Примеры с библиотекой RANDOM
```

for i in range(5):
    rand_num = random.randint(1, 100)
    print(rand_num)


for i in range(5):
    rand_num = random.uniform(1, 10)
    print(rand_num)
```

## Игра угадай число
```

life = 5
random_num = random.randint(1,50)
isWin = False

print("Было загадано число от 1 до 49. Попробуй угадать!")
while life != 0:
    num = int(input("Введите число: "))

    if num == random_num:
        print("Вы победили")
        isWin = True 
        break

    elif num < random_num:
        print("Загаданное число больше.")
        life -= 1

    elif num > random_num:
        print("Загаданное число меньше.")
        life -= 1

if (not isWin):
    print("Вы проиграли")
```

## Рисунок смайлика с помощью библиотеки TURTLE
```

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("lightblue")
screen.title("Весёлый смайлик - Изучаем Turtle")

t = turtle.Turtle()
t.speed(5)
t.width(3)

t.penup()
t.goto(0, -100)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-40, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-40, 40)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(40, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(40, 40)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-60, -20)
t.pendown()
t.color("black")
t.width(5)
t.setheading(-60)
t.circle(70, 120)

t.hideturtle()
screen.exitonclick()
```

## Функция с параметрами

```
Функция с параметрами
def exam_result(russian, math, informatics):
    total = russian + math + informatics

    if 0 <= total and total <= 120:
        print("Плохо")
    elif 121 <= total and total <= 210:
        print("Хорошо")
    elif 211 <= total and total <= 300:
        print("Отлично")
    else:
        print("Введены некорректные данные")

exam_result(67, 72, 80)
```

## Задача создание паролей
```

import random
import string

def password_generation(lenPas, iSnums, isUpAlpha):
    symbols = string.ascii_lowercase
    password = ""

    if isUpAlpha:
        symbols += string.ascii_uppercase
    if iSnums:
        symbols += "1234567890"

    for _ in range(lenPas):
        password += random.choice(symbols)
    
    return password

print("---Программа для генерации пароля---")
lenPas = int(input("Введите длину пароля: "))
iSnums = input("Нужны ли цифры в пароле? Y/n: ")
isUpAlpha = input("Нужны ли большие буквы в пароле? Y/n: ")

if iSnums.lower() == "y":
    iSnums = True
else:
    iSnums = False

if isUpAlpha.lower() == "y":
    isUpAlpha = True
else:
    isUpAlpha = False

password = password_generation(lenPas, iSnums, isUpAlpha)
print(password)
```

## Задача: сколько гласных букв в строке
```


def CountGlassSymbols(text):
    glassSymbols = "аеёиоуыэюя"
    count = 0
    for i in text:
        if glassSymbols.find(i) != -1:
            count += 1
    return count
    
string = "Всем пока, я не строка"
print(f"В строке \"{string}\" {CountGlassSymbols(string)} гласных букв")
```

## Задача: какая сумма цифр у числа
```

def SumOfDigits(number):
    strNum = str(number)
    sumDigits = 0
    for i in strNum:
        sumDigits += int(i)

    return sumDigits

print(f"Сумма цифр в числе 1234 равна {SumOfDigits(1234)}")
```