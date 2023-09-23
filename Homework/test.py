def jump(jumps: list[int]) -> int:
    var = 0
    cnt = 0
    for i in range(len(jumps) - 1):
        if var + jumps[i] > jumps[-1]:
            cnt += 1
            break
        cnt += 1
        var += jumps[i]
        if var == jumps[-1]:
            break
    return cnt

jumps = [2,3,1,1,4]
print(jump(jumps))