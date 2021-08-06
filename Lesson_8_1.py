import re

def parse_email(email_addr):
    x_mail = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not x_mail.match(email_addr):
        raise ValueError(f'Wrong email: {email_addr}')
    print(x_mail.match(email_addr).groupdict())


for i in ('someone@geekbranes.ru', 'some&one@geekbranesru', 'someone@geekbranesru'):
    try:
        parse_email(i)
    except ValueError as err:
        print(err)