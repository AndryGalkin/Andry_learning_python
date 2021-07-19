from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def some_jokes(nums, repeat=False):
    """
    Функция возвращает случайные словосочетания, собранные из трех списков слов.
    :param nums: задает количество словосочетаний
    :param repeat: запрещает/разрешает повторы слов
    :return: случайное словосочетание
    """
    ns, advs, adjs = nouns.copy(), adverbs.copy(), adjectives.copy()
    j_list = []
    min_list = min(ns, advs, adjs)
    nums = int(nums)

    while nums and len(min_list):
        numbs = randrange(len(min_list))
        if repeat:
            j_list.append(f'{ns.pop(numbs)} {advs.pop(numbs)} {adjs.pop(numbs)}')
        else:
            j_list.append(f'{choice(ns)} {choice(advs)} {choice(adjs)}')
        nums -= 1
    return j_list


print(some_jokes(input('Сколько вешать в граммах? '), False))
