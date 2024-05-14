# Resourses --> https://www.youtube.com/watch?v=PhgtNY_-CiY&t=465s

# Prefix sum
# Has O(n+q) --> O(n) time complexity
n, q = map(int, input().split())
array = list(map(int, input().split()))
pref = [0] * (n+1)

for i in range(n):
    pref[i+1] = pref[i] + array[i]

for i in range(q):
    a, b = map(int, input().split())
    # a-1 beachse the prefix sum array is 1 indexed
    print(pref[b] - pref[a-1])
print(pref)

# Brute force
# Has O(n*q) time complexity
"""
n, q = map(int, input().split())
array = list(map(int, input().split()))
for _ in range(q):
    a, b = map(int, input().split())
    range_sum = sum(array[a-1:b])
    print(range_sum)
"""