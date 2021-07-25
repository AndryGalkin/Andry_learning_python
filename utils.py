from requests import get, utils
from datetime import datetime

xml_query = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(cur_name=None):
    cur_name = cur_name.upper()
    xml_data = xml_query.split('<Valute ID=')
    date_of = datetime.strptime(xml_query.split('"')[5], '%d.%m.%Y').date()

    for cur_val in xml_data:

        if cur_name in cur_val:
            res = cur_val.replace('/', '').split('<Value>')[1].replace(',', '.')
            print (float(res), date_of)
    return 0


