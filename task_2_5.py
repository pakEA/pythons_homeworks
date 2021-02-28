prices = [13.21, 78.01, 43, 98.06, 39.92, 27.67, 87, 7, 51, 61.32]
prices_2 = []

print(id(prices))

for price in prices:
    big_price = int(price)
    small_price = price % big_price
    small_price = int(small_price * 100)
    prices_2.append(f'{big_price:02d} руб. {small_price:02d} коп.')

all_price = ', '.join(prices_2)
print(all_price)

prices.sort()
print(id(prices), prices)

prices_rev_sort = sorted(prices, reverse=True)
print(prices_rev_sort)

prices.sort(reverse=True)
print(prices[:5])
