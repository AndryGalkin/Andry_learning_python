my_list = [57.8, 46.51, 97, 32.70, 112.60, 14, 8.80, 75, 13.31, 17.00, 67.13, 26.04, 31.40]
n = 0
print(f'my_list id = {id(my_list)}')

for names in my_list:
    xsplit = str(names).split('.')

    if len(xsplit) == 1:
        print(f'{xsplit[0]} руб 00 коп,', end=" ")
    elif len(xsplit) == 2:
        if xsplit[1][1:]:
            print(f'{xsplit[0]} руб {xsplit[1]} коп,', end=" ")
        else:
            print(f'{xsplit[0]} руб 0{xsplit[1]} коп,', end=" ")
    n += 1

print('\n')

my_list.sort()
print(f'my_list id = {id(my_list)}')

for names in my_list:
    xsplit = str(names).split('.')

    if len(xsplit) == 1:
        print(f'{xsplit[0]} руб 00 коп,', end=" ")
    elif len(xsplit) == 2:
        if xsplit[1][1:]:
            print(f'{xsplit[0]} руб {xsplit[1]} коп,', end=" ")
        else:
            print(f'{xsplit[0]} руб 0{xsplit[1]} коп,', end=" ")
    n += 1

print('\n')
my_list.sort(reverse = True)
print(f'my_list id = {id(my_list)}')

for names in my_list:
    xsplit = str(names).split('.')

    if len(xsplit) == 1:
        print(f'{xsplit[0]} руб 00 коп,', end=" ")
    elif len(xsplit) == 2:
        if xsplit[1][1:]:
            print(f'{xsplit[0]} руб {xsplit[1]} коп,', end=" ")
        else:
            print(f'{xsplit[0]} руб 0{xsplit[1]} коп,', end=" ")
    n += 1

print('\n')
# решение далеко от оптимального, но к моменту разбора на уроке скрипт был уже готов,
# менять ничего не стал, в конце концов это моя логика и мой путь :)
