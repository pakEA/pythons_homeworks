NUMBER = 15

nums_gen = (num for num in range(1, NUMBER + 1, 2))

while NUMBER:
    print(next(nums_gen))
