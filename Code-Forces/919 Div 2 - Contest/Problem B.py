# Number of test cases
t = int(input())

for _ in range(t):
    # Input for each test case
    n, k, x = map(int, input().split())
    array = list(map(int, input().split()))

    # Sort the array to make it easier to choose elements
    array.sort()

    # Perform the game optimally
    for i in range(min(k, x)):
        if array[i] < 0:
            array[i] *= -1
        else:
            break

    # Calculate and print the sum of elements after the game
    print(sum(array))
