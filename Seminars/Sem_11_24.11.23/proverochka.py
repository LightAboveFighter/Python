def _mean_func_val_(func, *list_val):
    new_val = list(map(func, *list_val))
    return sum(new_val) / len(new_val)

l = [1, 2, 3, 4]
r = [5, 6, 7, 8]
print(_mean_func_val_(lambda x: x*2, l))