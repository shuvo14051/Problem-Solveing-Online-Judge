n, m = map(int, input().split())
li = [[x for x in input().split()] for _ in range(n)]
li2 = []
for i in li:
    li2 += i

pixels = set(li2)
pixel_str = ''.join(pixels)

if pixel_str == 'WB' or pixel_str == 'BW' or pixel_str == 'B' or pixel_str == 'W':
    print("#Black&White")
else:
    print("#Color")