# Приношу свои извинения, блок-схемы не успел, можно отправить их к следующему уроку?

#1
a = input("Введите трёхзначное число:")
b = list(map(int, str(a)))

print(f"сумма = {b[0] + b[1] + b[2]}")
print(f"произведение = {b[0] * b[1] * b[2]}")


#2
print(f'{bin(5) = }, {bin(6) = } ')
print(f'{5 & 6 = }, {5 | 6 = }, {5 ^ 6 = }')
print(5 << 2, 5 >> 2)

#3
x1, y1 = int(input('x1:')), int(input('y1:'))
x2, y2 = int(input('x2:')), int(input('y2:'))

k = (y1 - y2)/(x1 - x2)
b = y1 - k * x1
s = '+' if b > 0 else '-'
print(f'y = {k} * x {s} {abs(b)}')

#4
from random import randint, uniform, choice

fst_char = input('Введите начало диапазона: ')
last_char = input('Введите конец диапазона: ')

p = '.'
if p in fst_char or p in last_char:
    print(uniform(float(fst_char), float(last_char)))
elif fst_char.isdigit() & last_char.isdigit():
    print(randint(int(fst_char), int(last_char)))
else:
    print(choice([chr(i) for i in range(ord(fst_char), ord(last_char))]))


#5
first_char = (ord(input('Первая буква: ')) - ord("a") + 1)
last_char = (ord(input('Вторая буква: ')) - ord("a") + 1)

print(first_char)
print(last_char)
print(f'Between: {last_char - first_char} letters')


#6
first_char = chr(int(input('Номер буквы: ')) + ord("a")-1)
print(first_char)


#7

a = int(input("Side one"))
b = int(input("Side two"))
c = int(input("Side three"))

if (a + b > c and a + c + > b and b + c > a):
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("Равнобедренный треугольник")
    elif a == b == c:
        print("Равносторонний треугольник")
else: print("Невозможно собрать треугольник")

#8

y = int(input("Enter year: "))
if y%400 == 0 or (y%4 == 0 and y%100 !=0):
    print(True)

else:
    print(False)

   
#9
    
a = int(input("Enter first "))
b = int(input("Enter second "))
c = int(input("Enter thrid "))

a,b,c = sorted([a,b,c])
print(f'min: {a}, middle: {b}, max: {c}')





