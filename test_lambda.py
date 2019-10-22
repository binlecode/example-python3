
# lambda in Python is a function object created by expression
# syntax: lambda argument1, argument2,... argumentN : expression using arguments

# use reduce function with lambda to find the max
from functools import reduce

max = reduce(lambda a, b: a if (a > b) else b, [23, 11, 34, 56, 24])
print(max)


# lambda has enclosing scope
def func(seed):
    ss = seed * 2
    lp = (lambda n: ss ** n)   # lambda has scope of func, including ss and seed
    return lp

lmd_pow_n = func(2)   # seed => 2
print(lmd_pow_n(3))   # n = 3, (2 * 2) ** 3 => 64

# lambda is handy as callback functions in map-filter-reduce flow
evn_lst = list(filter(lambda x: x%2 == 0, range(10)))
print(evn_lst)

evn_pow_lst = list(map(lambda x: x ** 2, evn_lst))
print(evn_pow_lst)

sum = reduce(lambda a, b: a + b, evn_pow_lst)
print(sum)

# use lambda in list custom sort
import random
lst = [(i, random.randint(0, 100)) for i in range(1, 10, 2)] # list comprehension
print(lst)  # each element is a tuple
lst_sorted = lst.sort(key=lambda tpl: tpl[1])  # sort by 2nd element in tuple
print(lst)
