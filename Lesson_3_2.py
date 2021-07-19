def thesaurus(in_list):
    res_dic = {}
    for x_name in sorted(in_list):
        first_char = x_name[:1]
        if first_char in res_dic:
            res_dic[first_char] += [x_name]
        else:
            res_dic[first_char] = [x_name]

    return res_dic


names = ["Иван", "Мария", "Петр", "Прасковья", "Илья", "Мелхесидек"]
print(thesaurus(names))
