n = int(input())
total = 0
c = 0
r = 0
s = 0

for i in range(n):
    ar = list(input().split()[:2])
    total += int(ar[0])
    if ar[1] == 'C':
        c += int(ar[0])
    if ar[1] == 'R':
        r += int(ar[0])
    if ar[1] == 'S':
        s += int(ar[0])

x = (c * 100.00) / total
y = (r * 100.00) / total
z = (s * 100.00) / total

print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % c)
print("Total de ratos: %d" % r)
print("Total de sapos: %d" % s)

print("Percentual de coelhos: {0:.2f} %".format(x))
print("Percentual de ratos: {0:.2f} %".format(y))
print("Percentual de sapos: {0:.2f} %".format(z))
