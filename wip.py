import re


templ_x = open(r'C:\repo\regular.txt', 'r', encoding='utf-8')

for i in templ_x:
    content = re.search(r'\[ \]+', i)
    if content != None:
        print(content[0])


