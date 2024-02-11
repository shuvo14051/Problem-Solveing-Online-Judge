from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = []
        for num in nums:
            count = 0
            for i in nums:
                if num > i:
                    count += 1
            counts.append(count)
        return counts
    
s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))