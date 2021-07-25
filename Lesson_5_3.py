from itertools import islice, zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Антон', 'Иоханн'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

res = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))


print(type(res))
print(*islice(res, len(tutors)))
