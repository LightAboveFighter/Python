from typing import Iterable, Any

ver = "12424"

def my_append(list_instance: list, x: Any) -> None:
    res = [0] * ( len(list_instance) + 1)
    res[:-1] = list_instance[:]
    res[-1] = x
    list_instance[:] = res[:]
    pass

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a.append(ver)
my_append(b, ver)
print(a, " -- ", b, " - my_append function is", a==b)

def my_extend( list_instance: list, expansion: Iterable ) -> None:
    res = [0] * ( len(list_instance) + len(expansion) )
    res[:len(list_instance)] = list_instance[:]
    res[len(list_instance):] = expansion[:]
    list_instance[:] = res[:]
    pass

if type(ver) == type(a) or type(ver) == type("d"):
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    a.extend(ver)
    my_extend(b, ver)
    print(a, " -- ", b, " - my_extend function is", a==b)

def my_insert(list_instance: list, i: int, x: Any) -> None:
    res = [0] * ( len(list_instance) + 1)
    res[:i] = list_instance[:i]
    res[i] = x
    res[ (i+1):] = list_instance[ i:]
    list_instance[:] = res[:]
    pass

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a.insert(2, ver)
my_insert(b, 2, ver)
print(a, " -- ", b, " - my_insert function is", a==b)

def my_reverse(list_instance: list) -> None:
    res = [0] * ( len(list_instance) + 1)
    res[:-1] = list_instance[-1:0:-1]
    res[-1] = list_instance[0]
    list_instance[:] = res[:]
    pass

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a.reverse()
my_reverse(b)
print(a, " -- ", b, " - my_reverse function is", a==b)
print(" End of Task 1")

# Task 2 ================================================================

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

# Task 3 ==================================================================

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    res = []
    for i in range(len(intervals) - 1):
        if intervals[i][1] < intervals[i+1][0]:
            res.append(intervals[i])
        else:
            intervals[i+1][0] = intervals[i][0]
    res.append(intervals[-1])
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(intervals[-1], " -  Task 3")
assert merge_intervals(intervals) == [[1,6],[8,10],[15,18]]

# Task 4 ===================================================================

def remove_duplicates(nums: list[int]) -> None:
    res = nums[:]
    ans = [nums[0]]
    for i in range(len(res) - 1):
        if not(res[i] == res[i+1] ):
            ans.append(res[i+1])
    nums[:] = ans[:]
    pass

nums = [1, 1, 2]
remove_duplicates(nums)
assert nums == [1, 2]
print(nums, " -  Task 4")

# Task 5 ====================================================================

def compute_unique_pathes(grid:list[list[int]]) -> int:
    grid_copy = grid[:]
    grid_copy[0][0] = -1

    for i in range(len(grid_copy)):
        if grid_copy[i][0] != 1 and grid_copy[i-1][0] != 1:
            grid_copy[i][0] = -1
        
    for i in range(len(grid_copy[0])):
        if grid_copy[0][i] != 1 and grid_copy[0][i-1] != 1:
            grid_copy[0][i] = -1
        
    for i in range(1, len(grid_copy) ):
        for k in range(1, len(grid_copy[0]) ):

            if grid_copy[i][k] != 1:
                if grid_copy[i-1][k] != 1:
                    grid_copy[i][k] += grid_copy[i-1][k]
                if grid_copy[i][k-1] != 1:
                    grid_copy[i][k] += grid_copy[i][k-1]

    return -grid_copy[-1][-1]

grid = [
 [0, 0, 0],
 [0, 1, 0],
 [0, 0, 0]
]
print(compute_unique_pathes(grid), " -  Task 5")
#assert compute_unique_pathes(grid) == 2

#=================================================================================
#=================================================================================
ver = "12424"

def my_append(list_instance: list, x: Any) -> None:
    res = [0] * ( len(list_instance) + 1)
    res[:-1] = list_instance[:]
    res[-1] = x
    list_instance[:] = res[:]
    pass

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a.append(ver)
my_append(b, ver)
print(a, " -- ", b, " - my_append function is", a==b)

def my_extend( list_instance: list, expansion: Iterable ) -> None:
    res = [0] * ( len(list_instance) + len(expansion) )
    res[:len(list_instance)] = list_instance[:]
    res[len(list_instance):] = expansion[:]
    list_instance[:] = res[:]
    pass

if type(ver) == type(a) or type(ver) == type("d"):
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    a.extend(ver)
    my_extend(b, ver)
    print(a, " -- ", b, " - my_extend function is", a==b)

def my_insert(list_instance: list, i: int, x: Any) -> None:
    res = [0] * ( len(list_instance) + 1)
    res[:i] = list_instance[:i]
    res[i] = x
    res[ (i+1):] = list_instance[ i:]
    list_instance[:] = res[:]
    pass

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a.insert(2, ver)
my_insert(b, 2, ver)
print(a, " -- ", b, " - my_insert function is", a==b)

def my_reverse(list_instance: list) -> None:
    res = [0] * ( len(list_instance) + 1)
    res[:-1] = list_instance[-1:0:-1]
    res[-1] = list_instance[0]
    list_instance[:] = res[:]
    pass

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
a.reverse()
my_reverse(b)
print(a, " -- ", b, " - my_reverse function is", a==b)
print(" End of Task 1")

# Task 2 ================================================================

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

# Task 3 ==================================================================

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    res = []
    for i in range(len(intervals) - 1):
        if intervals[i][1] < intervals[i+1][0]:
            res.append(intervals[i])
        else:
            intervals[i+1][0] = intervals[i][0]
    res.append(intervals[-1])
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(intervals[-1], " -  Task 3")
assert merge_intervals(intervals) == [[1,6],[8,10],[15,18]]

# Task 4 ===================================================================

def remove_duplicates(nums: list[int]) -> None:
    res = nums[:]
    ans = [nums[0]]
    for i in range(len(res) - 1):
        if not(res[i] == res[i+1] ):
            ans.append(res[i+1])
    nums[:] = ans[:]
    pass

nums = [1, 1, 2]
remove_duplicates(nums)
assert nums == [1, 2]
print(nums, " -  Task 4")

# Task 5 ====================================================================

def compute_unique_pathes(grid:list[list[int]]) -> int:
    grid_copy = grid[:]
    grid_copy[0][0] = -1

    for i in range(len(grid_copy)):
        if grid_copy[i][0] != 1 and grid_copy[i-1][0] != 1:
            grid_copy[i][0] = -1
        
    for i in range(len(grid_copy[0])):
        if grid_copy[0][i] != 1 and grid_copy[0][i-1] != 1:
            grid_copy[0][i] = -1
        
    for i in range(1, len(grid_copy) ):
        for k in range(1, len(grid_copy[0]) ):

            if grid_copy[i][k] != 1:
                if grid_copy[i-1][k] != 1:
                    grid_copy[i][k] += grid_copy[i-1][k]
                if grid_copy[i][k-1] != 1:
                    grid_copy[i][k] += grid_copy[i][k-1]

    return -grid_copy[-1][-1]

grid = [
 [0, 0, 0],
 [0, 1, 0],
 [0, 0, 0]
]
print(compute_unique_pathes(grid), " -  Task 5")