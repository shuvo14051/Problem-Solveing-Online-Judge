red, blue = map(int,input().split())

diff_pair, same_pair = 0, 0

for i in range(max(red, blue)):
    if red >=1 and blue >=1:
        diff_pair += 1
        red = red - 1
        blue = blue - 1
    elif red >=2 or blue >=2:
        same_pair += 1
        red = red - 2
        blue = blue - 2

print(diff_pair, same_pair)