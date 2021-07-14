my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
n = 0
for idx in my_list:

    if idx.isdigit():
        if len(str(idx)) < 2:
            my_list[n] = '"' + '0' + str(idx) + '"'
        else:
            my_list[n] = '"' + str(idx) + '"'

    elif "+" in idx:
        if len(str(idx)) < 3:
            my_list[n] = '"+' + '0' + str(idx)[1:] + '"'
        else:
            my_list[n] = '"' + str(idx) + '"'

    elif "-" in idx:
        if len(str(idx)) < 3:
            my_list[n] = '"-' + '0' + str(idx)[1:] + '"'
        else:
            my_list[n] = '"' + str(idx) + '"'
    n += 1
message = ' '.join(my_list)
print(message)
