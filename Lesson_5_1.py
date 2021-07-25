def odd_generator(num):
    num = int(num)
    num_gen = (num + 1 for num in range(-1, num))

    for i in num_gen:
        if i < num:
            print(next(num_gen))
    return 0


numb = input('Введите число: ')
odd_generator(numb)

