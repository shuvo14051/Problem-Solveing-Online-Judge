test = int(input())
for i in range(test):
	A, B, G1, G2 = map(float, input().split())
	count = 0
	while True:
		A = A + int(A*G1*.01)
		B = B + int(B*G2*.01)
		count += 1
		if count >100:
			print("Mais de 1 seculo.")
			break
		if A > B:
			print("{} anos.".format(count))
			break
		