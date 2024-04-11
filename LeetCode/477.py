from typing import List 
from itertools import combinations

class Solution:
    # Memory Limit Exceeded
    def hammingDistance(self, x: int, y: int) -> int:
        x_or = x^y
        binary = bin(x_or)[2:]
        result = binary.count("1")
        return result
    
    def totalHammingDistance(self, nums: List[int]) -> int:
        s = 0
        pairs = list(combinations(nums,2))
        for x, y in pairs:
            s += self.hammingDistance(x, y)

        return s

s = Solution()
print(s.totalHammingDistance([4,14,4]))