python -m venv pyvenv_study2324
print('Зачем пришел?')
print('1 - покричать в горы', '2-сложить числа')
v = int(input())
if v == 1:
    print('Покричи в горы:')
    text = input()
    print('Горы отвечают тебе:', text)
    for i in range(len(text)):
        print(text[:(len(text)-i)])
elif v == 2:
    a = input('a= ')
    b = input('b= ')
    print(f'a+b= {a+b}')
