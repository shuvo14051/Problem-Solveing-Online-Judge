import itertools

love = "I love that"
hate = "I hate that"
li = [love, hate]
result = ""
n = int(input())

for i in range(1, n+1):
    if i % 2 == 1:
        result += "I hate that "
    else:
        result += "I love that "

result = result.strip()
print(result)
replace = result[-4:]
res = result.replace(replace, "it")
print(res)
