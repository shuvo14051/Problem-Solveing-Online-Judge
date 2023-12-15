n = int(input())
li = []
for i in range(n):

    ar = list((input().split()))
    option = ar[0]

    if option == "insert":
        position, item = ar[1], ar[2]
        position = int(position)
        item = int(item)
        li.insert(position, item)

    elif option == "append":
        item = int(ar[1])
        li.append(item)

    elif option == "pop":
        li.pop()

    elif option == "print":
        print(li)

    elif option == "remove":
        item = int(ar[1])
        li.remove(item)

    elif option == "sort":
        li.sort()

    elif option == "reverse":
        li.reverse()
