# Упражнение 85. Вычисляем длину гипотенузы

# def func(a, b):
#     return __import__('math').sqrt(a**2 + b**2)

# print(func(float(input('Enter a -> ')), float(input('Enter b -> '))))





# Упражнение 86. Плата за такси

# def taxi(km:int) -> int:
#     return 4 + (km * 1000 // 140 * 0.25)

# print(taxi(int(input('Enter Km -> '))))





# Упражнение 87. Расчет стоимости доставки

# def func(product):
#     return round(10.95 + (product - 1) * 2.95, 2)
# print(func(int(input('Enter a Amount of Products -> '))))





# Упражнение 88. Медиана трех значений


# def median(string:int):
#     li = sorted(string.split(' '))
#     return li[len(li) // 2]

# print(median(input('Enter 3 Numbers -> ')))





# Упражнение 89. Переводим целые числа в числительные

# li = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

# def num(numbers:int):
#     if numbers < 1 or numbers > 12:
#         return
#     else:
#         return li[numbers - 1]


# print(num(int(input('Enter a Number -> '))))





# Упражнение 91. Григорианский календарь в порядковый

# li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def days(string):
#     li2 = string.split(' ')
#     days = 0
#     for i in range(int(li2[1]) - 1):
#         if int(li2[2]) % 4 == 0:
#             days += 1
#         days += li[i]
#     return days + int(li2[0])

# print(days(input('Enter Day Month Year -> ')))



# Упражнение 93. Центрируем строку

# def center(s, w):
#     if len(s) >= len(w):
#         return s
#     else:
#         return f'{w}\n{" " * ((len(w) - len(s)) // 2)}{s}'

# print(center(input('Enter s -> '), input('Enter w -> ')))





# Упражнение 94. Треугольник ли?

# def triangle(a, b, c):
#     if min(a, b, c) <= 0:
#         return False
#     if max(a, b, c) >= a + b + c - max(a, b, c):
#         return False
#     return True

# print(triangle(int(input('Enter a -> ')), int(input('Enter b -> ')), int(input('Enter c -> '))))





# Упражнение 95. Озаглавим буквы

# def capit(string):
#     string = list(string)
#     for i in range(len(string)):
#         if string[i] in '?!.':
#             for j in range(i, len(string)):
#                 print(string[j])
#                 if string[j].isalpha():
#                     string[j] = string[j].upper()
#                     break
#         if string[i] == 'i':
#             if string[i - 1] == ' ' or string[i + 1] in '!?. ':
#                 string[i] = string[i].upper()
#     return ''.join(string)

# print(capit(input('Enter Something -> ').capitalize()))





# Упражнение 96. Является ли строка целым числом?

# def isInteger(num:int):
#     for i in range(1, len(num)):
#         if num[i].isdigit() == False:
#             return False
#     return True
            

# print(isInteger(input('Enter a Number -> ')))





# Упражнение 97. Приоритеты операторов

# def precedence(string):
#     li = ['+-', '*/', '^']
#     for i in li:
#         if string in i:
#             return li.index(i) + 1
#     return -1

# print(precedence(input('Enter operator -> ')))






# Упражнение 98. Простое число?

# def num(number:int):
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             return False
#     return True

# print(num(int(input('Enter a Number -> '))))





# Упражнение 99. Следующее простое число

# def nextPrime(n):
#     a = 1
#     while True:
#         if num(n + a) == True:
#             return n + a
#         else:
#             a += 1

# print(nextPrime(int(input('Enter a Number -> '))))





# Упражнение 100. Случайный пароль

# from random import randint

# def passwordGenerator():
#     password = ''
#     for _ in range(randint(7, 10)):
#         password += chr(randint(33, 126))
#     return password

# print(passwordGenerator())





# Упражнение 101. Случайный номерной знак

# from random import choice

# letters = 'qwertyuiopasdfghjklzxcvbnm'
# numbers = '1234567890'

# def licensePlate():
#     string = ''
#     for _ in range(7):
#         if len(string) < 4:
#             string += choice(numbers)
#         else:
#             string += choice(letters)
#     return string

# print(licensePlate())





# Упражнение 102. Проверка пароля на надежность

# def passwordCheck(password):
#     numbers = letters = 0
#     if len(password) < 8:
#         return False
#     for i in password:
#         if i.isdigit():
#             numbers += 1
#         if i.isalpha():
#             letters += 1
#     return numbers >= 1 and letters >= 1

# print(passwordCheck(input('Enter New Password -> ')))





# Упражнение 103. Случайный надежный пароль

# def RealPasswordGenerator():
#     return passwordCheck(passwordGenerator())

# print(RealPasswordGenerator())





# Упражнение 104. Шестнадцатеричные и десятичные числа

# def hex2int(symbol):
#     symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
#     if symbol not in symbols:
#         return False
#     return symbols.index(symbol)

# def int2hex(index2):
#     symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
#     if index2 in symbols:
#         return False
#     return f'{index2}\n{symbols[index2]}'

# print(int2hex(hex2int(input('Enter a Symbol -> '))))




# Упражнение 106. Дни в месяце

# def days(date):
#     li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     date = date.split(' ')
#     if int(date[0]) < 1 or int(date[0]) > 12 or len(date[1]) != 4:
#         return False
#     if int(date[1]) % 4 == 0:
#         li[1] = 29
#     return li[int(date[0]) - 1]

# print(days(input('Enter Day Year -> ')))





# Упражнение 107. Максимальное сокращение дробей

# def num(numbers):
#     numbers = numbers.split(' ')
#     n = min(int(numbers[0]), int(numbers[1]))
#     while True:
#         if int(numbers[0]) % n == 0 and int(numbers[1]) % n == 0:
#             return int(numbers[0]) // n, int(numbers[1]) // n
#         else:
#             n -= 1

# print(num(input('Enter Numbers => ')))





# Упражнение 108. Переводим меры

# def func(string):
#     string = string.split(' ')
#     if string[1] == 'cups':
#         return f'{string[0]} cups'
#     elif string[1] == 'tablespoons':
#         teaspoons = int(string[0]) * 3
#         cup = teaspoons // (16 * 3)
#         teaspoons  %= (16 * 3)
#         tablespoons = teaspoons // 3
#         teaspoons %= 3
#         return f'{cup} cups\n{tablespoons} tablespoons\n{teaspoons} teaspoons'
#     elif string[1] == 'teaspoons':
#         teaspoons = int(string[0])
#         cup = teaspoons // (16 * 3)
#         teaspoons %= (16 * 3)
#         tablespoons = teaspoons // 3
#         teaspoons %= 3
#         return f'{cup} cups\n{tablespoons} tablespoons\n{teaspoons} teaspoons'
    
# print(func(input('Enter Number Type -> ').lower()))





# Упражнение 109. Магические даты

# li = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

# def MagicDate(date):
#     date = date.split(' ')
#     return int(date[0]) * (li.index(date[1]) + 1) == int(date[2][-2:])

# print(MagicDate(input('Enter Day Month Year -> ').lower()))









# ------------------------------------------------------------------------

# 1.Calculator

# def plus(*args):
#     num = 0
#     for i in args:
#         num += i
#     print(num)

# def minus(*args):
#     num = 0
#     for i in args:
#         num -= i
#     print(num)

# def multiply(*args):
#     num = 1
#     for i in args:
#         num *= i
#     print(num)

# def divide(*args):
#     num = 1
#     for i in args:
#         num //= i
#     print(num)

# plus(4, 6, 8, 7, 9)
# minus(4, 6, 8, 7, 9)
# multiply(4, 6, 8, 7, 9)
# divide(4, 6, 8, 7, 9)





# 2.Write a python program to find max of two numbers

# def maxNum(num, num2):
#     return max(float(num), float(num2))

# print(maxNum(4, 5))




# 5.Write a python program to sum all letter and number in your string.

# def summ(string):
#     num = 0
#     string2 = ''
#     string = string.split(' ')
#     for i in string:
#         if i.isdigit():
#             num += int(i)
#         else:
#             string2 += i
#     return string2 + str(num)

# print(summ(input('Enter Numbers And Letters -> ')))





# 6.

# def ages(li):
#     li = li.split(' ')
#     for i in li:
#         if int(i) < 16:
#             return 'Too Young!'
#     return 'Get Ready!'

# print(ages(input('Enter Your Age -> ')))





# ------------------------------------------------------------------------

# Задача 1. Сумма чисел

# def summa_n(num):
#     summ = 0
#     if num < 0:
#         return False
#     for i in range(1, num + 1):
#         summ += i
#     return summ

# print(summa_n(int(input('Enter a Number -> '))))





# Задача 2. Функция в функции

# def test(num):
#     num >= 0 and positive() or num < 0 and negative()

# def positive():
#     print('Положительное')

# def negative():
#     print('Отрицательное')

# test(int(input('Enter a Number -> ')))





# Задача 3. Апгрейд калькулятора


# def plus(numbers):
#     num = 0
#     for i in numbers:
#         num += int(i)
#     print(num)

# def calculator(li, action):
#     li = li.split(' ')
#     action == 'plus' and plus(li) or action == 'minus' and minus(li) or action == 'multiply' and multiply(li) or action == 'divide' and divide(li) or action == 'module' and module(li)

# def minus(numbers):
#     num = int(numbers.pop(0))
#     for i in numbers:
#         num -= int(i)
#     print(num) 

# def multiply(numbers):
#     num = int(numbers.pop(0))
#     for i in numbers:
#         num *= int(i)
#     print(num)

# def divide(numbers):
#     num = int(numbers.pop(0))
#     for i in numbers:
#         num /= int(i)
#     print(num)

# def module(numbers):
#     num = int(numbers.pop(0))
#     for i in numbers:
#         num %= int(i)
#     print(num)

# calculator(input('Enter Numbers -> '), input('Enter Action -> ').lower())





# Задача 4. Число наоборот


# def turn(string):
#     string = list(string)
#     while string[len(string) - 1] == '0':
#         string.pop()
#     return ''.join(string[::-1])

# while True:
#     num = input('Enter a Number -> ')
#     if num == '0':
#         break
#     print(turn(num))





# Задача 5. Текстовый редактор

# def count_letters(text):
#     N = input('Enter a Number -> ')
#     K = input('Enter a Letter -> ')
#     return f'Count of {N}: {text.count(N)}\nCount of {K}: {text.count(K)}'

# print(count_letters(input('Enter Your Text -> ')))





# Задача 6. Монетка

# def coinFinder(x, y):
#     if -1 <= x <= 1 and -1 <= y <= 1:
#         return 'Монетка где-то рядом'
#     return 'Монетки в области нет'

# print(coinFinder(float(input('Enter x -> ')), float(input('Enter y -> '))))





# Задача 7. Опять?

# from random import choice

# nub = '5 -5 -5 5 -5 -5 89 251 23 475 65 98 45 45 23 45 45 45 475 23 23 23 23 23 23 23 1 1 1 1 1 1'

# def minNumber(argument):
#     num = int(choice(argument))
#     random_num = int(choice(argument))
#     argument.count(str(num)) > 1 and argument.remove(str(num))
#     num < random_num and argument.remove(str(random_num))
#     len(argument) == 1 and print(argument[0]) or len(argument) > 1 and minNumber(argument)

# minNumber(nub.split(' '))





# Задача 8. НОД

# def num(numbers):
#     numbers = numbers.split(' ')
#     n = min(int(numbers[0]), int(numbers[1]))
#     while True:
#         if int(numbers[0]) % n == 0 and int(numbers[1]) % n == 0:
#             return n
#         else:
#             n -= 1

# print(num(input('Enter Numbers => ')))





# Задача 9. Недоделка

# import random

# def rock_paper_scissors():
#     li = ['rock', 'paper', 'scissors']
#     computer = random.choice(li)
#     user = input('rock --- paper --- scissors -> ').lower()
#     if user in li:
#         if computer == 'rock' and user == 'scissors' or computer == 'paper' and user == 'rock' or computer == 'scissors' and user == 'paper':
#             print('You Lose...', computer)
#         elif computer == user:
#             print('draw', computer)
#         else:
#             print('You Win!!', computer)
#     user = input('Play Again? ').lower()
#     user == 'yes' and rock_paper_scissors() or user == 'no' and mainMenu()

# def guess_the_number():
#     computer = random.randint(1, 29)
#     while True:
#         user = int(input('Enter Number Less than 30 and Greater than 0 -> '))
#         if user == computer:
#             print('You Win!!')
#             break
#     user = input('Play Again? ').lower()
#     user == 'yes' and guess_the_number() or user == 'no' and mainMenu()

# def mainMenu():
#     game = input('What You Want to Play\n1) rock_paper_scissors\n2) guess_the_number\n3) Nothing\n')
#     game == '1)' and rock_paper_scissors() or game == '2)' and guess_the_number()

# mainMenu()