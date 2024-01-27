test = int(input())

for _ in range(test):
    li = set()
    a = int(input())
    for i in range(a):
        language = input()
        li.add(language)
    if len(li) == 1:
        print(language)
    else:
        print("ingles")
    