position_and_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                     'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for people in position_and_name:
    name = people.rsplit(' ', maxsplit=1)
    print(f'Привет, {name[1].capitalize()}!')
