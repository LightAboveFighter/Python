def compute_unique_pathes(grid:list[list[int]]) -> int:
    if grid[-1][-1] == 1:
        return 0
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