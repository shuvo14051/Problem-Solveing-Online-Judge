# while True:
#     try:
#         n = int(input())
#         nums = list(map(int, input().split()))[:n]
#         money = int(input())

#         pairs = [(nums[i],nums[j]) for i in range(len(nums)) for j in range (i+1, len(nums))
#                 if nums[i] +nums[j] == money]
#         min_pair = min(pairs, key=lambda pair: abs(pair[0]-pair[1]))
#         sorted_pair = sorted(min_pair)
#         first = sorted_pair[0]
#         second = sorted_pair[1]
#         print("Peter should buy books whose prices are {} and {}.".format(first, second))


#     except EOFError:
#         break  # Exit the loop when EOF is reached

from itertools import combinations

while True:
    try:
        # Input: Number of books
        n = int(input())
        
        # Input: Prices of books
        nums = list(map(int, input().split()))[:n]

        # Input: Amount of money
        money = int(input())

        # Finding pairs with the given sum using combinations
        pairs = [(x, y) for x, y in combinations(nums, 2) if x + y == money]

        pairs.sort(key=lambda pair: pair[0])

        min_pair = min(pairs, key=lambda pair: abs(pair[0] - pair[1]))
        min_pair = sorted(min_pair)

            # Output the result
        print("Peter should buy books whose prices are {} and {}.".format(min_pair[0], min_pair[1]))
        

    except EOFError:
        break  # Exit the loop when EOF is reached
