base = "abc"
test = int(input())
for i in range(test):
    s = input().lower()
    if s == "abc":
        print("YES")
    else:
        # First check
        first_ch1 = s[0]
        last_two1 = s[1] + s[2]
        swaped_last_two1 = first_ch1 + last_two1[::-1]

        first_ch2 = s[2]
        last_two2 = s[0] + s[1]
        swaped_last_two2 = last_two2[::-1] + first_ch2

        first_ch3 = s[1]
        last_two3 = s[0] + s[2]
        swaped = last_two3[::-1]
        swaped_last_two3 = swaped[0] + first_ch3 + swaped[1]

        if swaped_last_two1 == 'abc' or swaped_last_two2 == 'abc' or swaped_last_two3 == 'abc':
            print("YES")
        else:
            print("NO")
