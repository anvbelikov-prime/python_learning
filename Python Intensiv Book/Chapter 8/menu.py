class WorngKeyFunc(Exception):
    pass

def menu(**kwargs):
    options = '/'.join(sorted(kwargs.keys()))
    while True:
        s = input(f"Введите функцию {options}: ")
        if s in kwargs:
            return kwargs[s]()
        else:
            raise WorngKeyFunc('Wrong key function!')


def func_a():
    return 'a'

def func_b():
    return 'b'

if __name__ == '__main__':
    returned_res = menu(a=func_a, b=func_b)
    print(returned_res)
