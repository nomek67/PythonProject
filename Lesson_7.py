import random
import string

# def sum_squares_nums(lst):
#     new_lst = []
#     for i in list:
#         new_lst.append(i ** 2)

#         result = sum(new_lst)
#         return result

# lst1 = [23, 57, 13, 67, 75]

# result1 = sum_squares_nums(lst1)
# print(result1)


# lst2 = [14, 49, 6, 64]

# result2 = sum_squares_nums(lst2)
# print(result2)


# lst3 = [8, 90, 55, 83, 1, 22]

# result3 = sum_squares_nums(lst3)
# print(result3)


# Функция с параметрами
# def exam_result(russian, math, informatics):
#     total = russian + math + informatics

#     if 0 <= total and total <= 120:
#         print("Плохо")
#     elif 121 <= total and total <= 210:
#         print("Хорошо")
#     elif 211 <= total and total <= 300:
#         print("Отлично")
#     else:
#         print("Введены некорректные данные")

# exam_result(67, 72, 80)


# Задача №1 
# Создание паролей

# def password_generation(lenPas, iSnums, isUpAlpha):
#     symbols = string.ascii_lowercase
#     password = ""

#     if isUpAlpha:
#         symbols += string.ascii_uppercase
#     if iSnums:
#         symbols += "1234567890"

#     for _ in range(lenPas):
#         password += random.choice(symbols)
    
#     return password

# print("---Программа для генерации пароля---")
# lenPas = int(input("Введите длину пароля: "))
# iSnums = input("Нужны ли цифры в пароле? Y/n: ")
# isUpAlpha = input("Нужны ли большие буквы в пароле? Y/n: ")

# if iSnums.lower() == "y":
#     iSnums = True
# else:
#     iSnums = False

# if isUpAlpha.lower() == "y":
#     isUpAlpha = True
# else:
#     isUpAlpha = False

# password = password_generation(lenPas, iSnums, isUpAlpha)
# print(password)


# def IsEven(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# num = int(input("Введите ваше число: "))

# if(IsEven(num)):
#     print("Число нечётное")
# else:
#     print("Число нечётное")


# def CountGlassSymbols(text):
#     glassSymbols = "аеёиоуыэюя"
#     count = 0
#     for i in text:
#         if glassSymbols.find(i) != -1:
#             count += 1
#     return count
    
# string = "Всем пока, я не строка"
# print(f"В строке \"{string}\" {CountGlassSymbols(string)} гласных букв")


# def SumOfDigits(number):
#     strNum = str(number)
#     sumDigits = 0
#     for i in strNum:
#         sumDigits += int(i)

#     return sumDigits

# print(f"Сумма цифр в числе 1234 равна {SumOfDigits(1234)}")