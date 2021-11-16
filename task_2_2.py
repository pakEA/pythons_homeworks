raw_message = ['в', '5', 'часов', '17', 'минут', 'температура',
               'воздуха', 'была', '+5', 'градусов']

raw_message.insert(1, '"')
raw_message.insert(3, '"')
raw_message.insert(5, '"')
raw_message.insert(7, '"')
raw_message.insert(12, '"')
raw_message.insert(14, '"')

for elem in range(len(raw_message)):
    if raw_message[elem] == '+5':
        raw_message[elem] = raw_message[elem].replace('+', '')
    if raw_message[elem].isdigit():
        raw_message[elem] = '{:0>2}'.format(raw_message[elem])

new_list = raw_message[13].split()
new_list.insert(0, '+')
raw_message[13] = ''.join(new_list)

print(' '.join(raw_message))
