test = int(input())

for _ in range(test):
    word1, word2 = input().split()
    result1, result2 = "", ""
    ch1, ch2 = word1[0], word2[0]
    result1 = ch2 + word1[1:]
    result2 = ch1 + word2[1:]

    print(result1, result2)