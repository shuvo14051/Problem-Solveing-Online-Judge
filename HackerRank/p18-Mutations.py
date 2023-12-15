def mutate_string(s, position, character):
    li = []
    result = ''
    for i in s:
        li.append(i)

    li[position] = character

    for j in li:
        result += j

    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)