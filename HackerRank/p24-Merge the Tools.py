import textwrap


def merge_the_tools(s, k):
    li = textwrap.wrap(s, k)

    for item in li:
        s = []
        for char in item:
            if char not in s:
                s.append(char)
        result = ''
        for i in s:
            result += i
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)