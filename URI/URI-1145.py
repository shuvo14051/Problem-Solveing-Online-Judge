a, b = map(int, input().split())
x = 0

if ((a > 1 and a < 20) and (b > a and b < 100000)):
    result = ''
    final_result = ''
    for i in range(1, b + 1):
        result = result + str(i) +' '
        final_result += result.strip()
        x += 1
        if x == a:
            result += "\n"
            x = 0
print(final_result)