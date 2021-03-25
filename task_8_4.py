def val_checker(_x):
    def _val_checker(func):
        def wrapper(*args):
            calc = func(*args)
            for el in args:
                if [*args] <= [0]:
                    raise ValueError(f'wrong val {el}')
            return calc

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
