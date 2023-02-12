# Упражнение 173. Сумма значений

# def summ():
#     x = input('Enter a Number -> ')
#     if x == '':
#         return 0
#     return int(x) + summ()
# print(summ())





# Упражнение 174. Наибольший общий делитель

def euclid(a ,b):
    if b == 0:
        return a
    c = a % b
    return euclid(a, b % c)

print(euclid(64, 48))