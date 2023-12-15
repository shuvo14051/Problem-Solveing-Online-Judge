test = int(input())

for i in range(test):
    word = input()
    odd = ''
    even = ''
    li_word = []
    for i in word:
        li_word.append(i)

    length = len(li_word)
    for j in range(0, length, 2):
        even += li_word[j]
    for k in range(1, length, 2):
        odd += li_word[k]

    print("{} {}".format(even, odd))
