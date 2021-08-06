import re

RN = re.compile(r'([\w\.\+\:\/]+)')


def log_parser(str_ln):
    log = RN.findall(str_ln)
    print((log[0], log[1] + log[2], log[3], log[4], log[5], log[6], log[7]))


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        log_parser(line)
