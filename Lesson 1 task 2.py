odds = []
odds_sum = 0
ids = 0

while ids <= 999:
    if ids // 2 != ids / 2:
        odds.append(ids ** 3)
    ids += 1

# на этом месте я застрял и понял, насколько все просто, уже после разбора

for indx, val in enumerate(odds):
    sum_dig = 0
    while val:
        sum_dig += val % 10
        val //= 10
    if sum_dig % 7 == 0:
        odds_sum += odds[indx]
    odds[indx] += 17

print(odds_sum)

for indx, val in enumerate(odds):
    sum_dig = 0
    while val:
        sum_dig += val % 10
        val //= 10
    if sum_dig % 7 == 0:
        odds_sum += odds[indx]

print(odds_sum)