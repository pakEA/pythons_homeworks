from requests import get
from decimal import Decimal
from copy import copy


def currency_rates(item):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    content_copy = copy(content)
    date = content_copy.split(' Date="')[1].split('" name=')[0]
    for el in content.split('<CharCode>'):
        some_str = el.split('</Value>')[0].replace(',', '.')
        copy_str = some_str[:]
        currency_code = some_str.split('</CharCode>')[0]
        currency_value = copy_str.split('<Value>')[-1]
        if item.upper() == currency_code:
            currency = Decimal(currency_value).quantize(Decimal('.01'))
            return f'{currency}, {date}'
    return


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('EUR'))
