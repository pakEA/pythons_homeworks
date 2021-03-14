NUMBER = 15


def nums_gen(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums = nums_gen(NUMBER)

while NUMBER:
    print(next(nums))
