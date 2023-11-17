def max2(arg1:int, arg2:int):
    if arg1 > arg2:
        return arg1
    return arg2

test_cases = [(1,1), (-1,-3), (1, 3.14), (6, 3.14), ('c', 'abc'), (True, False)]

for x, y in test_cases:
    res = max2(x, y)
    print(f'max of {(x, y)} is {res}. Type of func is {type(res)}')

def f(name="NoName", mysep=' '):
    print("Hello", name, sep=mysep)

f(mysep='TataRata', name='John')

def qewe(number, *args, **qwargs):
    print(f"args: {args}")
    print(f"qwargs: {qwargs}")
    if 'name' in qwargs:
        print(f'Hello, {qwargs["name"]}, and his {number} wifes' )
    if 'factorial' in qwargs:
        print('чот много просишь')

qewe(3, 15, 'sr', 64, name='John', ERRORITY=101001101001011, factorial = 230402340)