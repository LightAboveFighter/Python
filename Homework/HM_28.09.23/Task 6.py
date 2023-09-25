def jump(jumps: list[int]) -> int:
    
    paths = [10000] * len(jumps)
    paths[0] = 0

    for i in range(len(jumps) - 1):
        for j in range(jumps[i]):
            if j < len(jumps):
                paths[i + j + 1] = min(paths[i + j + 1], paths[i] + 1)
    return paths[-1]

jumps = [2,3,1,1,4]
print(jump(jumps))