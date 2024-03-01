test = int(input())

for _ in range(test):
    string = input()
    my_list = string.split(" ")
    sorted_list = sorted(my_list, key=len, reverse=True)

    res = " ".join(sorted_list)
    print(res)