"""
#method1
def sum_arr(n):
    sum = 0
    for i in n:
        sum = sum+i
    print("The sum of the elements in the list is:", sum)

a = [1,2,3,4]
sum_arr(a)
"""
from functools import reduce
a = [1,2,3,4]
b = reduce(lambda x,y: x+y,a)
print(b)







