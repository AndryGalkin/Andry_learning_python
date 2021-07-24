from requests import get, utils
from datetime import datetime

xml_query = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(cur_name):
    cur_name = cur_name.upper()
    xml_data = xml_query.split('<Valute ID=')
    date_of = xml_query.split('"')[5]
    date_of = datetime.strptime(date_of, '%d.%m.%Y')

    for cur_val in xml_data:

        if cur_name in cur_val:
            res = cur_val.replace('/', '').split('<Value>')[1].replace(',', '.')
            return cur_name, float(res), date_of.date()


in_currency = input('Enter you currency:')
print(*currency_rates(in_currency))
#print(*currency_rates('usd'))
