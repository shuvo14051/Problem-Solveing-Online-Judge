string = input()
li_of_string = []
result = []

if int(string) == 0:
    print("-1")

else:
    for i in string:
        li_of_string.append(i)

    for i in range(len(li_of_string)):
        number = 0
        string2 = ''
        item = li_of_string.pop()
        li_of_string.insert(0, item)
        for i in li_of_string:
            string2 += i
        number = int(string2, 2)
        result.append(number)

    count = 0
    even_item = []
    final_result = []
    for i in result:
        if i % 2 == 0:
            even_item.append(i)
            count += 1

    if count == 0:
        print("0")

    else:
        for i in even_item:
            d = 0
            while i % 2 == 0:
                i = i // 2
                d += 1
            final_result.append(d)
        max = max(final_result)
        if max > 9:
            print("-1")
        else:
            print(max)
