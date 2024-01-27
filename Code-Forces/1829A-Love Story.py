test = int(input())
base = 'codeforces'
base_index = 0

for _ in range(test):
    count = 0
    word = input()
    for i in range (len(word)):
        if word[i] != base[i]:
            count += 1
    print(count)
    