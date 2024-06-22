def find_kth_number(n, k):
    num_odds = (n + 1) // 2  # Count of odd numbers
    if k <= num_odds:
        return 2 * k - 1  # k-th odd number
    else:
        return 2 * (k - num_odds)  # (k - num_odds)-th even number

# Read input
n, k = map(int, input().split())
# Print the result
print(find_kth_number(n, k))
