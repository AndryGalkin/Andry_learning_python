from time import perf_counter
#import random
#---------------- 1 ------------------

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 97]
#src = [random.randint(1, 10000) for _ in range(1000)]

result = [el for el in src if src.count(el) == 1]
print(result)

#---------------- 2 -----------------

result = set()
tmp_result = set()

for el in src:
    if el not in tmp_result:
        result.add(el)
    else:
        result.discard(el)
    tmp_result.add(el)
print(list(result))

