test = int(input())
base = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}


for _ in range(test):
    li = []
    n = int(input())
    for _ in range(n):
        word = input().lower()
        li.append(word)
    element = 0
    val = 0
    for word in li:
        for i in range(len(word)):
            val = val + base[word[i]] + element + i
        element += 1

    print(val)

        