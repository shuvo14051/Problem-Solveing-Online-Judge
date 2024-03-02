from math import sqrt

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Calculate the total sum of numbers from 1 to n
        y = n * (n + 1) // 2
        # Find the potential square root of y (our pivot x)
        x = int(sqrt(y))
        # Check if x is indeed the pivot
        return x if x * x == y else -1