"""
#lambda using a function without defining funciton

mult = lambda x,y: x*y
print(mult(2,3))
"""
"""
#sorted

points_2d = [(6,5),(4,3),(2,1)]

a = sorted(points_2d,key= lambda x: x[1])
print(a)
"""

#map,filter,reduce

b = [1,2,3,4,5]
c = list(map(lambda x: x*2, b))
print(c)

d = list(filter(lambda x:x%2==0,b))
print(d)

from functools import reduce

e = reduce(lambda x,y: x*y,b)
print(e)

