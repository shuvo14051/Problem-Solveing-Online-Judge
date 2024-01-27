

def solve(s):
    custome_title = []
    li = s.split(' ')
    
    for i in li:
        if i.isalpha() and i[0].isdigit():
            custome_title.append(i)
        else:
            custome_title.append(i.capitalize())
    return ' '.join(custome_title)



if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
