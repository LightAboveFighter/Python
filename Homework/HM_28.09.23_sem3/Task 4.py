# def remove_duplicates(nums: list[int]) -> None:
#     res = nums[:]
#     ans = [nums[0]]
#     for i in range(len(res) - 1):
#         if not(res[i] == res[i+1] ):
#             ans.append(res[i+1])
#     nums[:] = ans[:]
#     pass

def remove_duplicates(nums: list[int]) -> None:
    a = len(nums)
    i = 0
    while i < a - 1:
        if nums[i] == nums[i+1]:
            del nums[i+1]
            a -= 1
        else:
            i += 1

nums = [1, 1, 2]
remove_duplicates(nums)
assert nums == [1, 2]
print(nums, " -  Task 4")