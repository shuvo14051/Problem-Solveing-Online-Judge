test = int(input())
my_dict = {
    '1': 2,'2': 5, '3':5, '4': 4,'5': 5,  '6': 6,
    '7': 3, '8': 7,  '9': 6, '0': 6
}

for _ in range(test):
    led = 0
    n = input()
    for i in n:
        if i in my_dict:
            led += my_dict[i]
    print("{} leds".format(led))

