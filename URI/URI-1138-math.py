from collections import Counter

while True:
    a, b = map(int, input().split())
    li = [0]*10
    string = ""
    if a == 0 and b == 0:
        break
    for i in range(a, b+1):
        string += str(i)
    char_count = Counter(string)
    for key, value in char_count.items():
        if key == '0':
            li[0] = value
        elif key == '1':
            li[1] = value
        elif key == '2':
            li[2] = value
        elif key == '3':
            li[3] = value
        elif key == '4':
            li[4] = value
        elif key == '5':
            li[5] = value
        elif key == '6':
            li[6] = value
        elif key == '7':
            li[7] = value
        elif key == '8':
            li[8] = value
        elif key == '9':
            li[9] = value

    print(li)
    


