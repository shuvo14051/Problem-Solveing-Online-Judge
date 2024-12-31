test = int(input())

for _ in range(test):
    word = input()
    c_0 = word[0]
    c_1 = word[1]
    c_2 = word[2]
    if len(word) == 5:
        print(3)
    elif (c_0=='o' and c_1 == 'n')or(c_1=='n' and c_2=='e') or (c_0=='o' and c_2=='e'):
        print(1)
    else:
        print(2)