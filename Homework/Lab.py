a = [5, 8, 9, 11, 14, 16, 18, 20, 23, 28]
s = [5, 8, 10, 12, 15, 17, 20, 22, 25, 30]
print('Таблица чувствительности ЭЛТ')
print()
for i in range(len(a)):
    print(i+1, "  -  ", a[i]/(s[i] * (2**0.5)))

print()
print('Таблица чувствительности осциллографа')
print()

q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
w = [2, 5, 7, 10, 12, 14, 17, 19, 21, 23]
for i in range(len(q)):
    print(i+1, "  -  ", w[i]/(q[i] * (2**0.5)))

ul = 0
u = 0
l = 0
uu = 0
for i in range(10):
    u += s[i]
    uu += s[i]*s[i]
    l += a[i]
    ul += s[i]*a[i]
ul = ul/10
print(ul)
print(u/10)
print(l/10)
print(uu/10)
print(16.4*16.4)
print( (300.8-16.4*15.2)/(325.6 - 268.96))
print(15.2 - 0.91*16.4)