def sum_two_nums(num1: list[int], num2: list[int]) -> list[int]:
    n = max(len(num1), len(num2) ) + 1
    num1 = [0]*(n - len(num1) ) + num1
    num2 = [0]*(n - len(num2) ) + num2
    rest = 0
    result = [0]*n
    for i in range(n-1, 0, -1):
        result[i] = num1[i] + num2[i] + rest
        rest = result[i]//10
        result[i] = result[i]%10
    result[0] = rest
    if result[0] == 0:
        return result[1:]
    return result

def Num_to_list(x: int):
    list1 = []
    list1.extend(str(x))
    x = [ int(list1[i]) for i in range(len(list1) ) ]
    return x

print("Введите два числа через enter для суммирования")
num1 = int(input())
num2 = int(input())
num3 = num1 + num2
num1 = Num_to_list(num1)
num2 = Num_to_list(num2)
print(num1, " + ", num2, " = ", sum_two_nums(num1, num2))
print("My list_sum func is", Num_to_list(num3) == sum_two_nums(num1, num2), " (Task 2)")

num1 = [1, 2, 3]
num2 = [7, 7]
assert sum_two_nums(num1, num2) == [2, 0, 0]
assert sum_two_nums(num2, num1) == [2, 0, 0]