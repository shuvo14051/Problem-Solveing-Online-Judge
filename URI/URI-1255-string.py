test = int(input())
for _ in range(test):
    d = {}
    result = ''
    text = input().lower()
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
    maxi = max(list(d.values()))
    for key, value in d.items():
        if value == maxi:
            result += key
    print(''.join(sorted(result)))
