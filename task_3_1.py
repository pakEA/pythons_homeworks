def num_translate(item):
    if item in num_names:
        print(f'"{num_names[item]}"')
    else:
        print(num_names.get(item))


num_names = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

num_translate('one')
num_translate('nine')
num_translate('eleven')
