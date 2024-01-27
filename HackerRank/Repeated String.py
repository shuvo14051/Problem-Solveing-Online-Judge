s = input()
n = int(input())
result = 0

if len(s) == 1:
    result = n
else:
    repeated_s = (s*(n//len(s)+1))[:n]
    result = repeated_s.count('a')
    
print (result)
