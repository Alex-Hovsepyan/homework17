# Упражнение 149. Отображаем начало файла

# def head():
#     try:
#         with open(input('Enter File Name -> '), 'r') as file:
#             li = file.readlines()
#             for i in range(10):
#                 print(li[i])
#     except FileNotFoundError:
#         print('File Not Found: ')
# head()





# Упражнение 150. Отображаем конец файла

# def tail():
#     try:
#         with open(input('Enter File Name -> '), 'r') as file:
#             li = (file.readlines())[::-1]
#             for i in range(10):
#                 print(li[i], end="")
#     except FileNotFoundError:
#         print('File Not Found: ')
# tail()





# Упражнение 151. Сцепляем файлы

# def cat():
#     li = []
#     while True:
#         fileName = input('Enter File Name -> ')
#         if fileName == '':
#             break
#         try:
#             with open(fileName, 'r') as file:
#                 li += file.readlines()
#         except FileNotFoundError:
#             print(f'{fileName} Not Found:')
#     for i in li:
#         print(i, end="")
# cat()





# Упражнение 152. Нумеруем строки в файле

# try:
#     with open(input('Enter File Name -> '), 'r') as file:
#         li = file.readlines()
#     with open(input('Enter Second File Name -> '), 'a') as file2:
#         for i in range(len(li)):
#             file2.write(f'{i + 1}: {li[i]}')
# except FileNotFoundError:
#     print('File Not Found: ')





# Упражнение 153. Самое длинное слово в файле

# try:
#     with open(input('Enter File Name -> '), 'r') as file:
#         li = file.readlines()
#         for i in range(len(li)):
#             li[i] = li[i].replace(' ', '')
#             li[i] = li[i].replace('\n', '')
        
#         for j in li:
#             if len(j) == len(max(li)):
#                 print(f'{j} -> {len(j)}')

# except FileNotFoundError:
#     print('File Not Found:')





# Упражнение 154. Частота букв в файле

# letters = 'abcdefghijklmnopqrstuvwxyz'
# maxi = 0
# letter = ''

# try:
#     fileName = input('Enter File Name => ')
#     with open(fileName, 'r') as file:
#         li = file.readlines()
#         li = ''.join(li).lower()
#         for i in letters:
#             if maxi < li.count(i):
#                 maxi = li.count(i)
#                 letter = i
#         li = li.replace(letter, 't')
#         print(li)
#     with open(fileName, 'w') as file2:
#         for j in li:
#             file2.write(j)

# except FileNotFoundError:
#     print('File Not Found:')
# print(maxi, letter)


# Упражнение 155. Частота слов в файле

# maxi = 0
# word = ''

# with open('text.txt', 'r') as file:
#     li = file.readlines()
#     li2 = ''.join(li)
#     for i in range(len(li)):
#         li[i] = li[i].replace('\n', '')
#         li[i] = li[i].split()
    
#     for a in li:
#         for b in a:
#             if maxi < li2.count(b):
#                 maxi = li2.count(b)
#                 letter = b       
#     print(maxi, b)



# Упражнение 156. Сумма чисел

# summ = 0
# while True:
#     num = input('Enter a Number -> ')
#     if num == '':
#         break
#     try:
#         summ += float(num)
#         print(summ)
#     except ValueError:
#         print('You Need to Write int or float -> ')





# Упражнение 157. Буквенные и числовые оценки

# grades = {
#     'A+' : 4,
#     'A' : 4,
#     'A-' : 3.7,
#     'B+' : 3.3,
#     'B' : 3,
#     'B-' : 2.7,
#     'C+' : 2.3,
#     'C' : 2,
#     'C-' : 1.7,
#     'D+' : 1.3,
#     'D' : 1,
#     'F' : 0,
#     '4' : 'A+',
#     '4' : 'A',
#     '3.7' : 'A-',
#     '3.3' : 'B+',
#     '3' : 'B',
#     '2.7' : 'B-',
#     '2.3' : 'C+',
#     '2' : 'C',
#     '1.7' : 'C-',
#     '1.3' : 'D+',
#     '1' : 'D',
#     '0' : 'F',
# }

# while True:
#     grade = input('Enter You Grade: ')
#     if grade == '':
#         break
#     try:
#         num = grades[grade]
#         print(num)
#     except KeyError:
#         print('You Need to Write Correct Grade')





# Упражнение 158. Удаляем комментарии

# try:
#     firstFile = input('Enter File Name => ')
#     newFile = input('Enter New File Name => ')
#     with open(firstFile, 'r') as file:
#         li = file.readlines()
#         for i in range(len(li)):
#             if '#' not in li[i]:
#                 with open(newFile, 'r') as file2:
#                     pass
#                 with open(newFile, 'a') as file2:
#                     file2.write(li[i])
# except FileNotFoundError:
#     print(f'File Not Found')





# Упражнение 159. Случайный пароль из двух слов

# from random import choice

# letterCount = 0
# letterCount2 = 0

# with open('password.txt', 'r') as file:
#     li = file.readlines()
#     first = choice(li)
#     li.remove(first)
#     second = choice(li)
#     for i, j in zip(first, second):
#         if i.isalpha():
#             letterCount += 1
#         if j.isalpha():
#             letterCount2 += 1
#     password = (first.capitalize() + second.capitalize()).replace('\n', '')
#     if 8 <= len(password) <= 10 and letterCount >= 3 and letterCount2 >= 3:
#         print(True, password)
#     else:
#         print(False, password)





# Упражнение 161. Что за химический элемент?

# try:
#     elem = int(input('Enter element -> '))
#     with open('text.txt', 'r') as file:
#         li = file.readlines()
#         if 1 <= elem <= 118:
#             for i in range(len(li)):
#                 li[i] = li[i].replace('\t', '')
#                 li[i] = li[i].replace('\n', '')
#                 if str(elem) in li[i]:
#                     print((li[i + 1].replace('\n', '')), '-', elem)
#                     break
#         else:
#             print('Error')
                
# except ValueError:
#     print('You Need to Write int:')





# Упражнение 162. Книги без буквы E

# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# count = 0
# minimum = [101, '']

# with open('text.txt', 'r') as file:
#     li = file.readlines()
#     for i in range(len(letters)):
#         for j in range(len(li)):
#             li[j] = li[j].replace('\n', '')
#             if letters[i] in li[j].upper():
#                 count += 1
#         # num = count / len(li) * 100
#         if (count / len(li) * 100) < minimum[0]:
#             minimum[0] = (count / len(li) * 100)
#             minimum[1] = letters[i]
#         print(f'{letters[i]} - {round(count / len(li) * 100)}%')
#         count = 0
# print(f'\n{minimum[1]} - {minimum[0]}')





# Упражнение 167. Проверяем правильность написания

# dict1 = {
#     'number' : 0,
#     'color' : 0,
#     'bear' : 0,
#     'butter' : 0,
#     'phone' : 0,
#     'brick' : 0,
#     'forest' : 0,
#     'cup' : 0,
#     'book' : 0,
#     'chair' : 0,
#     'sheep' : 0,
#     'mouse' : 0,
#     'TV' : 0,
#     'apple' : 0,
#     'building' : 0
# }

# li = []

# try:
#     with open(input('Enter File Name => '), 'r') as _:
#         with open(input('Enter File Name => '), 'a') as file:
#             while True:
#                 word = input('Enter a Word => ')
#                 if word == '':
#                     break
#                 file.write(f'{word}\n')
#                 li.append(word)
#             for i in li:
#                 if i in dict1:
#                     li.remove(i)
#             print(li)
# except FileNotFoundError:
#     print('File Not Found:')





# Упражнение 168. Повторяющиеся слова

# maxi = 0
# word = ''

# with open('text.txt', 'r') as file:
#     li = file.readlines()
#     li2 = ''.join(li)
#     li3 = file.readlines()
#     for i in range(len(li)):
#         li[i] = li[i].replace('\n', '')
#         li[i] = li[i].split()
#     for a in li:
#         for b in a:
#             if li2.count(b) > 1:
#                 print(b, li.index(a) + 1)





# Упражнение 169. Редактирование текста в файле

# li2 = ['exam', 'hello', 'python']
# string = ''

# with open('text.txt', 'r') as file:
#     li = file.readlines()
#     li3 = ''.join(li.copy()).lower()
#     for i in range(len(li)):
#         li[i] = li[i].replace('\n', '').lower()
#     for a in li2:
#         for b in li3:
#             string += b
#             if b == ' ':
#                 string = ''
#             if string == a:
#                 print(string)
#                 break




# Упражнение 172. Слова с шестью гласными в ряд

# try:
#     with open(input('Enter File Name => '), 'r') as file:
#         li = file.readlines()
#         for i in range(len(li)):
#             count = 0
#             letters = 'AEIOUY'
#             for j in li[i]:
#                 if j.upper() in letters:
#                     letters = letters.replace(j.upper(), '')
#                     count += 1
#                 else:
#                     break
#                 if count == 6:
#                     print(li[i], end="")
#                     break

# except FileNotFoundError:
#     print('File Not Found:')