n = int(input())

ar = list(map(int, input().split()))[:n]

ml_2 = 0
ml_3 = 0
ml_4 = 0
ml_5 = 0

for i in ar:
    if i % 2 == 0:
        ml_2 += 1
    if i % 3 == 0:
        ml_3 += 1
    if i % 4 == 0:
        ml_4 += 1
    if i % 5 == 0:
        ml_5 += 1

print("%d Multiplo(s) de 2" % ml_2)
print("%d Multiplo(s) de 3" % ml_3)
print("%d Multiplo(s) de 4" % ml_4)
print("%d Multiplo(s) de 5" % ml_5)
