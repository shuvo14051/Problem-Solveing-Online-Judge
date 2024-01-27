
H, Z, L = map(int, input().split())

if (Z > H and Z < L) or (Z < H and Z > L):
    print("zezinho")
elif (L > Z and L<H) or (L < Z and L>H):
    print("luisinho")
else:
    print("huguinho")
    