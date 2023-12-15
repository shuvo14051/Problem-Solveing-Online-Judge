import math
pi = math.acos(-1)
test_case = int(input())
for i in range(test_case):
	length = int(input())
	r = length/5
	width = (length*6)/10
	circle_Area = 2*pi*r
	rect = length*width
	rect_Area = rect - circle_Area
	print('%.2f'%circle_Area,'%.2f'%rect_Area)
