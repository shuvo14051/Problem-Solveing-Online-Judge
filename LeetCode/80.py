from typing import List 
from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = 0
        
        counter = Counter(nums)
        for key, value in counter.items():
            if value >= 2:
                nums[slow] = key
                slow += 1
                nums[slow] = key
                slow += 1
            else:
                nums[slow] = key
                slow += 1
        
        return slow

# Example usage
s = Solution()
nums = [1, 1, 1, 2, 2, 3]
new_length = s.removeDuplicates(nums)
print(nums[:new_length])  # Output: [1, 1, 2, 2, 3]
