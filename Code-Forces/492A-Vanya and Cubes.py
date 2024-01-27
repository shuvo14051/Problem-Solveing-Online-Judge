def sum_of_n(n):
    res = (n*(n+1))//2
    return res

n = int(input())

def height_of_cube(n):
    count = 0
    if n == 1:
        return 1
    for i in range(1,n+1):
        res = sum_of_n(i)
        print("sum of first {} digits: {}".format(i, res))
        n = n - res
        print("value of n: ", n)
        if n <= 0:
            break
        else:
            count += 1

        
        print("value of count: ", count)

    return count

res = height_of_cube(n)
print(res)
