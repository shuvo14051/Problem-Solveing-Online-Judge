p1, c1, p2, c2 = map(int, input().split())

part1 = p1*c1
part2 = p2*c2

if part1 == part2:
    print('0')

elif part1 < part2:
    print('1')

else:
    print('-1')
