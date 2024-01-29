import numpy 
n, m = map(int, input().split())

li = [[int(x) for x in input().split()] for _ in range(n)]

a = numpy.array(a)
a = numpy.reshape(a, (n,m))

print (numpy.mean(a, axis = 1))
print (numpy.var(a, axis = 0))
print (numpy.std(a))