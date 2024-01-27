test = int(input())

for _ in range(test):
    a, b = input().split()
    if a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")