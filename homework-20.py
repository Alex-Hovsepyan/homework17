def func():
    summ = 0
    with open('numbers.txt', 'r') as file:
        li = file.read().replace('\n', ' ').split(' ')
        for i in li:
            if i.isdigit():
                summ += int(float(i))
    with open('answer.txt', 'a') as file2:
        file2.write(str(summ))
func()