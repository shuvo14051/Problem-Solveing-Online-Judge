test = int(input())
base = "abcdefghijklmnopqrstwuvxyz"
for i in range(test):
    result = ""
    for i in range(8):
        line = input().lower()
        for i in line:
            if i in base:
                result += i

    print(result)
