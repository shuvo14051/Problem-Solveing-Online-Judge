import numpy

def arrays(arr):
    arr = numpy.array(arr, float)
    arr = numpy.flip(arr)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)