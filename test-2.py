#1

def calc(a, b, c):
    
    a = float(a)
    b = float(b)

    if c == '+':
        print(a + b)
        
    elif c == '-':
        print(a - b)
        
    elif c == '/':
        if b == 0:
            print('Делить на ноль нельзя!')
        else: print(a / b)
        
    elif c == '*':
        print(a * b)
        
    elif c == '0':
        exit(0)


c = ''

while c != '0':
    
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    c = input('Введите знак операции (+,-,*,/), или 0 для выхода: ')
    
    if a.isdigit() and b.isdigit():
        calc(a, b, c)
    else:
        print('Ошибка! Введите число.')



#2

a = input('Введите число: ')

n = 0
m = 0

if a.isdigit():
    for i in a:
        if int(i) % 2 == 0:
            n += 1
        else: m += 1

    print(f'Четных: {n}, нечетных: {m}')
else:
    print('Ошибка, ожидалось число.')



#3

a = input('Введите число: ')
if a.isdigit():
    b = ''.join(reversed(a))
    print(b)
else:
    print('Ошибка, ожидалось число.')



#4

n = input('Введите количество элементов ряда: ')

a = 1
b = 1

if n.isdigit():

    n = int(n)
    if n > 0:
        while n > 0:
            a /= -2
            b += a
            n -= 1

else:
    print('Ошибка, необходимо число.')
    exit(0)
print(b)


#5
a = 32
b = 127

for i, j in enumerate(range(a, b + 1)):
    if i % 10 == 0:
        print()
    print(f'{chr(j)}-{j}', end = '\t')
    


#6

import random

a = random.randint(0, 100)
b = int(input('Угадайте число от 1 до 100: '))
c = 10

while c != 0:
    if a == b:
        print('Верно!')
        exit(0)
    elif a > b:
        print(f'Это число больше чем {b}')
        c -= 1
        b = int(input(f'Осталось попыток {c}: '))
    else:
        print(f'Это число меньше чем {b}')
        c -= 1
        b = int(input('Осталось попыток {c}: '))
print(f'Вы проиграли. Загадонное число - {a}')
        
        

#7

n = input('Введите число: ')

if n.isdigit():
    
    n = int(n)
    a = 1
    e = 0
    b = n * (n + 1)/2

    for i, j in enumerate(range(a, n + 1)):
        e = j+e
        
    print(f'b = {b}')
    print(f'Sum = {e}')

else:
    print('Ошибка, необходимо число.')
    exit(0)


#8

n = input('Введите числовую строку: ')
a = input('Какую цифру будем искать: ')


if n.isdigit() and a.isdigit():

    print(f'Число повторений цифры {a} = {n.count(a)}')

else:
    print('Ошибка, необходимо число.')
    exit(0)


#9

a = input('Введите числа через пробел: ')
b = a.split(' ')
s_max = 0

for i in b:
    s = 0
    for j in str(i):
        s += int(j)
    if s > s_max:
        s_max = s
        res = i

print(f"максимальная сумма чисел {s_max} у числа {res}")
    

