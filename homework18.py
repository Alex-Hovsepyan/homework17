# Упражнение 173. Сумма значений

# def summ():
#     x = input('Enter a Number -> ')
#     if x == '':
#         return 0
#     return int(x) + summ()
# print(summ())





# Упражнение 174. Наибольший общий делитель










# Упражнение 176. Фонетический алфавит НАТО

# def nato(x, string=""):
#     dict1 = {
#         'A' : 'Alpha',
#         'B' : 'Bravo',
#         'C' : 'Charlie',
#         'D' : 'Delta',
#         'E' : 'Echo',
#         'F' : 'Foxtrot',
#         'G' : 'Golf',
#         'H' : 'Hotel',
#         'I' : 'India',
#         'J' : 'Juliet',
#         'K' : 'Kilo',
#         'L' : 'Lima',
#         'M' : 'Mike',
#         'N' : 'November',
#         'O' : 'Oscar',
#         'P' : 'Papa',
#         'Q' : 'Quebec',
#         'R' : 'Romeo',
#         'S' : 'Sierra',
#         'T' : 'Tango',
#         'U' : 'Uniform',
#         'V' : 'Victor',
#         'W' : 'Whiskey',
#         'X' : 'Xray',
#         'Y' : 'Yankee',
#         'Z' : 'Zulu',
#     }
#     if len(x) == 0:
#         return string
#     if x[0] in dict1:
#         return nato(x[1:], string + f'{dict1[x[0]]} ')
       
# print(nato(input('Enter Something -> ').upper()))





# Упражнение 177. Римские цифры

# def func(x, summ=0):
#     dict1 = {
#         'I' : 1,
#         'V' : 5,
#         'X' : 10,
#         'L' : 50,
#         'C' : 100,
#         'D' : 500,
#         'M' : 1000
#     }

#     if len(x) == 1:
#         return summ + dict1[x]
#     elif dict1[x[0]] >= dict1[x[1]]:
#         summ += dict1[x[0]]
#         return func(x[1:], summ)
#     elif dict1[x[0]] < dict1[x[1]]:
#         summ += (dict1[x[1]] - dict1[x[0]])
#         return func(x[2:], summ)
#     # else:
#     #     summ += dict1[x[0]]
#     return func(x[1:], summ)

# print(func(input('Enter a Number using -> I V X L C D M: ').upper()))





# Упражнение 178. Рекурсивные палиндромы

# def palin(word):
#     if len(word) == 0:
#         return True
#     if word[0] == word[len(word) - 1]:
#         word = word.replace(word[0], '')
#         return palin(word)
#     return False

# print(palin(input('Enter Word -> ').upper()))

# ---------- OR ----------

# def palin(word):
#     if len(word) == 0:
#         return True
#     if word[0] == word[len(word) - 1]:
#         return palin(word[1:-1])
#     return False

# print(palin(input('Enter Word -> ').upper()))





# Упражнение 185. Декодирование на основе длин серий

# def func(li, li2=[]):
#     if len(li) == 0:
#         return li2
#     if li[1] == 0:
#         return func(li[2:])
#     li2.append(li[0])
#     li[1] = li[1] - 1
#     return func(li)


# print(func(["A", 12, "B", 4, "A", 6, "B", 1]))





# Упражнение 186. Кодирование на основе длин серий

# def func(li, li2=[], num=0):
#     if len(li) == 0:
#         li2.append(num)
#         return li2[1:]
#     if len(li2) == 0 or li2[len(li2) - 1] != li[0]:
#         li2.append(num)
#         li2.append(li[0])
#         num = 0
#     return func(li[1:], li2, num + 1)

# print(func(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'V', 'V']))





# Упражнение 181. Возможный размен

# count = 10
# num = 104
# li = [0, 0, 0, 0]
# li[0] = count

# def func(count, num, x, y, a, b):
#     if li[0] < 0 or li[1] < 0 or li[2] < 0 or li[3] < 0:
#         return False
#     if y == 4:
#         x = 0
#         y = 1
#     if (li[0] * 25 + li[1] * 10 + li[2] * 5 + li[3] * 1) == num and (li[0] + li[1] + li[2] + li[3]) == count:
#         return True
#     elif (li[0] * 25 + li[1] * 10 + li[2] * 5 + li[3] * 1) > num and (li[0] + li[1] + li[2] + li[3]) == count:
#         li[x] -= 1
#         li[y] += 1
#         return func(count, num, x+1, y+1, a, b)
#     elif (li[0] * 25 + li[1] * 10 + li[2] * 5 + li[3] * 1) < num and (li[0] + li[1] + li[2] + li[3]) == count:
#         if li[3] != num % 5:
#             li[3] -= 1
#             li[2] += 1
#         elif li[2] != 0:
#             li[2] -= 1
#             li[1] += 1
#         elif li[1] != 0:
#             li[1] -= 1
#             li[0] += 1 
        
#     return func(count, num, x, y, a, b)

# print(func(count, num, 0, 1, 3, 2))
# print(li)