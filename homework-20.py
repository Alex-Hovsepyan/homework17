# 1. Сумма чисел 2

# def func():
#     summ = 0
#     with open('./textFiles/numbers.txt', 'r') as file:
#         li = file.read().replace('\n', ' ').split(' ')
#         for i in li:
#             if i.isdigit():
#                 summ += int(float(i))
#     with open('./textFiles/answers.txt', 'a') as file2:
#         file2.write(f'sum = {summ}\n')
# func()





# 2. Дзен Пайтона

# def func():
#     with open('./textFiles/zen.txt', 'r') as file:
#         li = file.read().replace('\n', '').split('.')
#         for i in li[::-1]:
#             print(f'\n{i}.')
# func()





# 3. Дзен Пайтона 2

# def func():
#     with open('./textFiles/zen.txt', 'r') as file:
#         li = file.read().lower()
#         letter_count = {i:li.count(i) for i in li if i.isalpha()}
#         print('Word Count:', len(li.replace('\n', ' ').split(' ')))
#         print('Line Count:', len(li.split('.')))
#         print('Letter Count:', sum(letter_count.values()))
#         print('The Rarest Letter:', sorted(letter_count, key=letter_count.get)[0])
# func()





# 4. Файлы и папки

# 5. Сохранение

# def func():
#     text = input('Enter Something => ')
#     try:
#         path = input('Enter location => ').replace(' ', '\\')
#         try:
#             fileName = input('Enter File Name => ')
#             with open(f'{path}\\{fileName}', 'r') as file:
#                 question = input('Do You Want to Overwrite The File? ').lower()
#                 if question == 'yes':
#                     with open(f'{path}\\{fileName}', 'w') as file:
#                         file.write(text)
#         except FileNotFoundError:
#             with open(f'{path}\\{fileName}', 'w') as file:
#                 file.write(text)
#     except OSError:
#         print('ERROR!!!')
# func()





# 6. Паранойя

# letters = 'abcdefghijklmnopqrstuvwxyz'

# with open('./textFiles/text.txt', 'r') as file:
#     string = ''
#     li2 = []
#     li = file.readlines()
#     for i in range(len(li)):
#         for j in li[i]:
#             for a in range(len(letters)):
#                 if j == ' ':
#                     string += ' '
#                     break
#                 if j == letters[a]:
#                     string += letters[a + i + 1]
                        
#         li2.append(string)
#         string = ''
#     print(li2)





# 7. Турнир

# import random

# with open('./textFiles/first_tour.txt', 'r') as file:
#     num = file.readline()
#     li = file.readlines()
#     dict1 = {}
#     for i in range(len(li)):
#         li[i] = li[i].replace('\n', '')
#         li[i] = li[i].split(' ')
#     for j in li:
#         if (j[1][:1] + ' ' + j[0]) in dict1 and int(j[2]) > int(num):
#             dict1[j[1][:1] + ' ' + j[0] + str(random.choice(range(len(li))))] = int(j[2])
#         if int(j[2]) > int(num):
#             dict1[j[1][:1] + ' ' + j[0]] = int(j[2])
#     dict2 = sorted(dict1, key=dict1.get)[::-1]
#     with open('./textFiles/second_tour.txt', 'a') as file2:
#         file2.write(f'{len(dict1)}\n')
#         for j in range(len(dict2)):
#             file2.write(f'{j + 1}) {dict2[j]} {dict1[dict2[j]]}\n')





# 8. Частотный анализ









# 1. Имена 2

# def func():
#     summ = 0
#     with open('./textFiles/people.txt', 'r') as file:
#         li = file.read().split('\n')
#         with open('./textFiles/errors.log', 'a') as file2:
#             for i in range(len(li)):
#                 if len(li[i]) < 3:
#                     file2.write(f'{li[i]}\n')
#                     print(f'Error at Line: {i + 1}')
#                     continue
#                 summ += len(li[i])

#     return summ

# print(func())





# 2. Координаты

# import random

# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     return x / y

# def f2(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     return y / x

# try:
#     with open('./textFiles/coordinates.txt', 'r') as file:
#         li = file.read().replace('\n', ' ').split(' ')
#         li2 = []
#         for i in range(len(li) // 2):
#             li2.append(round(f(int(li[0]), int(li[1])), 2))
#             li2.append(round(f2(int(li[0]), int(li[1])), 2))
#             li2.append(random.randint(0, 100))
#             li = li[2:]

#         for j in range(len(li2) // 3):
#             with open('./textFiles/result.txt', 'a') as file2:
#                 li = li2[:3]
#                 li.sort()
#                 file2.write(f'{li}\n')
#                 li2 = li2[3:]

# except:
#     print('ERROR!!!')





# 3. Счастливое число

# def func():
#     summ = 0
#     while True:
#         num = int(input('Enter a Number => '))
#         summ += num
#         if summ >= 777:
#             with open('./textFiles/lucky.txt', 'a') as file:
#                 file.write(f'{num}\n')
#             return 'You Win'
#         if __import__('random').randint(1, 13) == 5:
#             return 'You Lose'

#         with open('./textFiles/lucky.txt', 'a') as file:
#                 file.write(f'{num}\n')
        
# print(func())





# 4. Регистрация

# with open('./textFiles/registrations.txt', 'r') as file:
#     li = [i.split(' ') for i in file.read().split('\n')]
#     for i in li:
#         try:
#             if len(i) != 3:
#                 raise IndexError
#             for j in i[0]:
#                 try:
#                     if j.isalpha() == False:
#                         raise NameError
#                 except NameError:
#                     print('Name Can Only Contain Letters:', i)
#                     with open('./textFiles/wrong.txt', 'a') as file2:
#                         file2.write(f'{i}\n')
#             try:
#                 if '@' not in i[1] or '.' not in i[1]:
#                     raise SyntaxError
#                 try:
#                     if int(i[2]) < 10 or int(i[2]) > 99:
#                         raise ValueError
#                     with open('./textFiles/right.txt', 'a') as file2:
#                         file2.write(f'{i}\n')
#                 except ValueError:
#                     print('Your Age Must >=10 and <=99', i)
#                     with open('./textFiles/wrong.txt', 'a') as file2:
#                         file2.write(f'{i}\n')
#             except SyntaxError:
#                 print('"Email" field does not contain @ or . :', i)
#                 with open('./textFiles/wrong.txt', 'a') as file2:
#                         file2.write(f'{i}\n')
#         except IndexError:
#             print('You Need to Write: Name Email Age', i)
#             with open('./textFiles/wrong.txt', 'a') as file2:
#                         file2.write(f'{i}\n')





# 5. Текстовый калькулятор

# def func(fileName):
#     summ = 0
#     li2 = []
#     string = 0
#     with open(fileName, 'r') as file:
#         li = [i.split(' ') for i in file.read().split('\n')]
#         for i in li:
#             li2.append(i[0])
#             li2.append(i[2])
#             string = (li2[0]) (int('+')) (li2[1])
#             # for j in i:
#             #     print(j)
#             #     string = 
# print(func('./textFiles/calc.txt'))





# def func(fileName):
#     summ = 0
#     with open(fileName, 'r') as file:
#         li = [i.split(' ') for i in file.read().split('\n')]

#         print(li)
#         for j in range(len(li)):
#             if len(li[j][1]) != 1 or (len(li[j][1]) == 2 and (li[j][1] != '**' or li[j][1] != '//')):
#                 question = input(f'Do you Want to Fix It? {li[j]} => ').lower()
#                 if question == 'yes':
#                     answer = input('Enter Fixed Version => ')
#                     li[j] = answer.split(' ')
#                     li[j][0] = int(li[j][0])
#                     li[j][2] = int(li[j][2])
#                     summ += int(f(li[j][0], li[j][2], li[j][1]))
#             elif len(li[j][1]) == 1 or (len(li[j][1]) == 2 and (li[j][1] == '**' or li[j][1] == '//')):
#                 li[j][0] = int(li[j][0])
#                 li[j][2] = int(li[j][2])
#                 summ += f(li[j][0], li[j][2], li[j][1])
                    
#     return summ
                                    
# def f(x, y, a):
#     if a == '+':
#         return x + y
#     elif a == '-':
#         return x - y
#     elif a == '*':
#         return x * y
#     elif a == '**':
#         return x ** y
#     elif a == '/':
#         return x / y
#     elif a == '//':
#         return x // y
#     elif a == '%':
#         return x % y
    
# print(func('./textFiles/calc.txt'))