""" 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится
нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел
из этого списка, сумма цифр которых делится нацело на 7.
Внимание: новый список не создавать!!!

"""

list_of_cubes = []
list_of_sums = []
sum_of_digits = 0
sum_of_digits_2 = 0

for elem in range(1, 1000, 2):
    list_of_cubes.append(elem ** 3)

print('Список кубов:', list_of_cubes)

for idx in range(len(list_of_cubes)):
    digit_from_list = list_of_cubes[idx]
    for digit in list_of_cubes:
        digits = list_of_cubes[idx] % 10
        sum_of_digits += digits
        list_of_cubes[idx] //= 10
        if list_of_cubes[idx] == 0:
            if sum_of_digits % 7 == 0:
                list_of_sums.append(digit_from_list)
            sum_of_digits = 0
            break

print('Первый список:', sum(list_of_sums))

for elem in range(1, 1000, 2):
    list_of_cubes.append(elem ** 3)

for elem in range(len(list_of_cubes)):
    list_of_cubes[elem] += 17
    digit_from_list = list_of_cubes[elem]
    for digits in list_of_cubes:
        digit = list_of_cubes[elem] % 10
        sum_of_digits += digit
        list_of_cubes[elem] //= 10
        if list_of_cubes[elem] == 0:
            if sum_of_digits % 7 == 0:
                sum_of_digits_2 += digit_from_list
            sum_of_digits = 0
            break

print('Второй список:', sum_of_digits_2)
