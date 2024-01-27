test = int(input())

for i in range(test):
    n = int(input())
    sequence = [2**i for i in range(n)]
    result = (sum(sequence)//12)//1000
    print("{} kg".format(result))