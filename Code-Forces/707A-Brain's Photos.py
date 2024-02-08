base = "BGW"
n, m = map(int, input().split())
li = [[x for x in input().split()] for _ in range(n)]
li2 = []
for i in li:
    li2 += i

def color_bw(string):
    for i in string:
        if i not in base:
            return False
    return True

pixels = set(li2)
pixel_str = ''.join(pixels)
result = color_bw(pixel_str)

if result:
    print("#Black&White")
else:
    print("#Color")
