def num_translate(eng_template, rus_template, dig_template, in_val):
    for en_word, ru_word, num_word in zip(eng_template, rus_template, dig_template):

        if en_word == in_val.lower() or num_word == in_val:
            return ru_word


eng_templ = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
rus_templ = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
dig_templ = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
in_value = input('Enter a number: ')

print(num_translate(eng_templ, rus_templ, dig_templ, in_value))

# функция обрабатывает ввод данных в любом регистре и в числовом предствлении.
