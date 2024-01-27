test = int(input())

for _ in range(test):
    m, n = map(int, input().split())
    li = [[0 for i in range(n)] for i in range(m)]
    # This is one way of taking input
    # for i in range(m):
    #     for j in range(n):
    #         li[i][j] = input()
    # This is the second way    
    for i in range(m):
        line = input()
        li[i] = list(line)[:n]

    
    