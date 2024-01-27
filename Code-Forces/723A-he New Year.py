a, b, c = map(int, input().split())
min_value =  min(a,b,c)
max_value =  max(a,b,c)

mid = a+b+c - min_value - max_value

min_distance = (max_value-mid) + (mid - min_value)

print(min_distance)