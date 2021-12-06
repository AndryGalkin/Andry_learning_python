#1
from collections import defaultdict
from statistics import mean
from itertools import zip_longest


def comps_comparison():

    company_data = defaultdict(list)
    comp_nums = int(input('Количество предприятий: '))
    avg_profit = 0

    for i in range(comp_nums):
        comp_name = input(f'Название предприятия №{i+1}: ')
        for j in range(4):
            company_data[comp_name].append(int(input(f'Прибыль за квартал №{j+1}: ')))

    avg_profit = mean((mean(element) for element in company_data.values()))
    print(f'Средняя доходность: {avg_profit}')

    for key, value in company_data.items():
        if mean(value) < avg_profit:
            print(f'Прибыль предприятия {key} ниже среднего.')
        elif mean(value) > avg_profit:
            print(f'Прибыль предприятия {key} выше среднего.')
        else:
            pass


# comps_comparison()


#2

def sum_func(first, second):

    BASE = 16
    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    numb_dict = dict(zip(numbers, list(range(BASE))))
    first = first[::-1]
    second = second[::-1]
    third = []
    comp = 0

    for first_, second_ in zip_longest(first, second, fillvalue = '0'):
        if third.append(numbers[(numb_dict[first_] + numb_dict[second_] + comp) % 16]):
            comp = (numb_dict[first] + numb_dict[second] + comp) // 16
        else:
            third.append(numbers[comp % 16])
            return third[::-1]


def mult_func(first, second):

    numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    multi = '0'
    first = first[::-1]
    second = second[::-1]
    third = []
    comp = 0

    for i in range(len(second)):
        third = []
        if i > 0:
            third = ['0'] * i
            comp = 0
            for j in first:
                indx_a = numbers.index(second[i])
                indx_b = numbers.index(j)
                third.append(numbers[(indx_a * indx_b + comp) % 16])
                comp = (indx_a * indx_b + comp) // 16

                if j == len(first):
                    break
                third.append(str(comp))

                multi = sum_func(multi, third[::-1])

    return(multi)


#a = 'A2'
#b = 'CF43'
#print(sum_func(a, b))
#print(mult_func(a, b))

        


