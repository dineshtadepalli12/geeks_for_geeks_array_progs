"""def max_arr(a,l):
    max = a[0]
    for i in range(0,l):
        if a[i] >= max:
            max = a[i]
    return max

a = [41,4,1,11,2,21,5,9,15]
l = len(a)
print(max_arr(a,l))
"""
#or
from functools import reduce
arr = [15,23,21,1,29]
a = reduce(max,arr)
print(a)