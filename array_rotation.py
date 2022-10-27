#shifiting the array of size n by d elements.
#method1

"""
def rot_array(arr,d,n):
    temp = []
    i = 0
    while i < d:
        temp.append(arr[i])
        i+=1
    i = 0
    while d<n:
        arr[i] = arr[d]
        i+=1
        d+=1
    arr[:] = arr[:i]+ temp
    return arr

arr=[4,5,6,7,8,9]
print("The array after rotation is: ")
print(rot_array(arr,3,len(arr)))
"""

#method2 using slicing of array

def rotate_array(arr,n,d):

    arr[:] = arr[d:n] + arr[:d]
    return arr

arr=[4,5,6,7,8,9,10,11,12]
print("The array after rotation is: ")
print(rotate_array(arr,len(arr),3))

