# num = input('Введите целое число: ')
# num = num.strip()
# if ( (num[0] in '-+') and num[1:].isdigit() ) or num.isdigit():
#     num = int(num)
#     print(f'You typed number {num}, типа {type(num)}')
# else:
#     print('Incorrect input')

# try:
#     num = int(input('Введите целое число: '))
#     if num == 13:
#         raise Exception('Very_bad_Number')
#     num = 6 / num
#     print(f'You typed number {num}, типа {type(num)}')
# except ArithmeticError as e:
#     print(e)
#     print(type(e))
#     print(dir(e))
#     print(e.args)
#     print('пу пу пуум')
# except TypeError as e:
#     print(e)
#     print(type(e))
#     print(dir(e))
#     print(e.args)
#     print('пу пу пуум х2')
# except ValueError as e:
#     print(e)
#     print(type(e))
#     print(dir(e))
#     print(e.args)
#     print('fopf detected')
# except KeyboardInterrupt as e:
#     print(e)
#     print(type(e))
#     print(dir(e))
#     print(e.args)
#     print('MAI detected')
#     print('muahahahahaha')
#     r = 1
#     while(True):
#         print('muahahahah', r)
#         r *= 3


# else:
#     print('voohooooo')

#======================
arr = [ i for i in range(10) ]
vvod1, vvod2 = input().split()

try:
    vvod = [int(vvod1), int(vvod2)]
    print(arr[vvod[0]]/vvod[1])
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except IndexError as e:
    vvod[0] = abs(vvod[0])%len(arr)
    print(arr[vvod[0]]/vvod[1])
except:
    print('unknown error')
else:
    print('vohooo')

print(-5%4)