from typing import List 
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        # Count occurrences of each number
        num_counts = Counter(nums)
        result = []
        for num in nums:
            # Check if the number is lonely
            if num_counts[num] == 1 and num + 1 not in num_counts and num - 1 not in num_counts:
                result.append(num)
        return result

    

s = Solution()
print(s.findLonely([10,6,5,8]))