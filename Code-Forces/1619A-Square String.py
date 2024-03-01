test = int(input())

for _ in range(test):
    string = input()
    if len(string) % 2 != 0:
        ans = "NO"
    else:
        half_index = len(string) // 2
        first_half = string[:half_index]
        second_half = string[half_index:]

        if first_half == second_half:
            ans = "YES"
        else:
            ans = "NO"
    print(ans)
    