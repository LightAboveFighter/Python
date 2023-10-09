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