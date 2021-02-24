""" 3. Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем
число 2 — получаем «2 процента». Вывести все склонения для
проверки.

"""

number = int(input('Ввведите число до 50: '))
message_1 = 'процент'
message_2 = 'процента'
message_3 = 'процентов'

if number == 1 or number == 21 or number == 31 or number == 41:
    print(number, message_1)
elif number <= 4 or 21 < number < 25 or 31 < number < 35 or 41 < number < 45:
    print(number, message_2)
elif number <= 20 or 25 <= number <= 30 or 35 <= number <= 40 or 45 <= number <= 50:
    print(number, message_3)

for number in range(1, 51):
    if number == 1 or number == 21 or number == 31 or number == 41:
        print(number, message_1)
    elif number <= 4 or 21 < number < 25 or 31 < number < 35 or 41 < number < 45:
        print(number, message_2)
    elif number <= 20 or 25 <= number <= 30 or 35 <= number <= 40 or 45 <= number <= 50:
        print(number, message_3)
