n = int(input())
x = [int(x) for x in input().split()][:n]

print("Menor valor: {}".format(min(x)))
print("Posicao: {}".format(x.index(min(x))))