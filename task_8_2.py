def type_logger(func):
    def wrapper(*args):
        calc = func(*args)
        for el in args:
            if len(args) != 1:
                print(f'{[*args]}: {type(args)}')
                break
            print(f'{el}: {type(el)}')
            
        return calc

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_box(x, y):
    return x * y


a = calc_cube(5)
print(a)

b = calc_box(3, 5)
print(b)
