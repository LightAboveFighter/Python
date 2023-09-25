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