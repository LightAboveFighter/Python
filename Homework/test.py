# base_line = ["0"]*3
# base_block = [base_line]*3
# glob_line = [base_block]*3
# field = [glob_line]*3
# print(*field)

# def visualize(field: list[list[list[int]]] ):

#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 line = " | ".join(field[i][j][k])
#                 print(line)
#         print()

# visualize(field)
a = [1, 2, 3, 4]
print(map(a**2))