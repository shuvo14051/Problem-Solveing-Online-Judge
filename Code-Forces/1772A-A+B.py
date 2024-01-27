test = int(input())

for _ in range(test):
    operations = input()
    li = operations.split("+")
    print(int(li[0])+int(li[1]))
