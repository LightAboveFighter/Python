def jump(jumps: list[int]) -> int:
    
    paths = [10000] * len(jumps)
    paths[0] = 0

    for i in range(len(jumps) - 1):
        for j in range(jumps[i]):
            if j < len(jumps):
                paths[i + j + 1] = min(paths[i + j + 1], paths[i] + 1)
    print(paths)
    print(jumps)
    return paths[-1]

jumps = [4, 1, 1, 1, 4, 1, 1, 1, 100]
print(jump(jumps))