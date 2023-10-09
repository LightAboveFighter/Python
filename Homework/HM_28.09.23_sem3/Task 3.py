def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    res = []
    for i in range(len(intervals) - 1):
        if intervals[i][1] < intervals[i+1][0]:
            res.append(intervals[i])
        else:
            intervals[i+1][0] = intervals[i][0]
            intervals[i+1][1] = max(intervals[i+1][1], intervals[i][1])
    res.append(intervals[-1])
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(intervals[-1], " -  Task 3")
assert merge_intervals(intervals) == [[1,6],[8,10],[15,18]]