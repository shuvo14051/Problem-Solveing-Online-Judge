test = int(input())

for i in range(test):
    result = 0
    word = input()
    if word[0] == word[-1]:
        result = int(word[-1]) * int(word[0])
    elif word[1].isupper():
        result = int(word[-1]) - int(word[0])
    elif word[1].islower():
        result = int(word[-1]) + int(word[0])

    print(result)