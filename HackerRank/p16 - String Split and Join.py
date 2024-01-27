def split_and_join(line):
    splited_s = line.split()
    joined_s = '-'.join(splited_s)
    return joined_s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)