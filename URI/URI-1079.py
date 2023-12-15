test_case = int(input())

for i in range(test_case):
    a,b,c = map(float,input().split())
    avg = ((a*2)+(b*3)+(c*5))/10
    print("%.1f" %avg)