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
split = result.split(" ")
split[-1] = "it"
res = " ".join(split)
print(res)