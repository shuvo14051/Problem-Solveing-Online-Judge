while True:
    line = input()
    resutl = ""
    if line == "*":
        break
    li = line.split(" ")
    ch = line[0].lower()
    for i in li:
        if i[0].lower() != ch:
            result = "N"
            break
        else:
            result = "Y"

    print(result)