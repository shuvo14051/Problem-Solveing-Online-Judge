while True:
    first, second = 0, 0
    inter, gremio = map(int, input().split())
    print("Novo grenal (1-sim 2-nao)")
    condition = int(input())
    if condition == 1:
        inte, grem = map(int, input().split())
        if inte > grem:
            first += 1
        else:
            second += 1
        continue
    elif condition == 2:
        break