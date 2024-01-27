def solve(s):
    custome_title = []
    li = s.split(' ')
    for i in li:
        if i[0].isdigit():
            custome_title.append(i)
        else:
            custome_title.append(i.capitalize())
    return ' '.join(custome_title)