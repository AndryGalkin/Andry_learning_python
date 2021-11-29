#1


def pos_int_in_range():

    dig_range = [i for i in range(2, 100)]

    for pos_int in range(2, 10):
        print(f'{pos_int} - {len(list(filter(lambda x: x % pos_int == 0, dig_range)))}')

# pos_int_in_range()


#2


def odd_random_list():
    
    from random import seed, randint
    seed(33)

    rnd_list = [randint(0, 100) for r in range(10)]
    print(f'{rnd_list} - {[i for i, odd in enumerate(rnd_list) if odd % 2 == 0]}')


# odd_random_list()

#3


def change_min_max():
    
    from random import seed, randint
    seed(33)

    rnd_list = [randint(0, 100) for r in range(10)]

    print(rnd_list)

    rnd_min = rnd_list.index(min(rnd_list))
    rnd_max = rnd_list.index(max(rnd_list))

    rnd_list[rnd_min], rnd_list[rnd_max] = rnd_list[rnd_max], rnd_list[rnd_min]

    print(rnd_list)


# change_min_max()


#4
def count_max():
    
    from collections import Counter
    from random import seed, randint
    seed(33)

    rnd_list = [randint(0, 2) for r in range(10)]

    print(rnd_list)
    print(Counter(rnd_list).most_common(1))


#count_max()


#5

def max_negative_val():

    from random import seed, randint
    seed(33)

    rnd_list = [randint(-10, 10) for r in range(10)]

    print(rnd_list)
    dic = {num: len(rnd_list) - i -1 for i, num in enumerate(rnd_list[::-1])}
    max_num = max(list(filter(lambda x: x < 0, rnd_list)))
    print(f'Максимальное отрицательное значение: {max_num}, на позиции {dic[max_num]}')


# max_negative_val()

#6

def max_min_sum():

    from random import seed, randint
    seed(33)

    rnd_list = [randint(-10, 10) for r in range(10)]
    
    rnd_min = rnd_list.index(min(rnd_list))
    rnd_max = rnd_list.index(max(rnd_list))

    min_max = 1 if rnd_max > rnd_min else -1

    print(rnd_list)
    print(sum(rnd_list[rnd_min : rnd_max : min_max]))    

# max_min_sum()


#7

def two_min_elements():

    from random import seed, randint
    seed(33)

    rnd_list = [randint(-10, 10) for r in range(10)]
    print(rnd_list)

    srt_rnd_list = sorted(rnd_list)

    print(f'{srt_rnd_list[0]}, {srt_rnd_list[0]}')


#two_min_elements()






