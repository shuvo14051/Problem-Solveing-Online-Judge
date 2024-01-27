from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        sum_odd_position = 0
        sum_even_position = 0

        for i in range(0, len(nums), 2):
            sum_odd_position += nums[i]
        
        for j in range(1, len(nums), 2):
            sum_even_position += nums[j]

        if sum_odd_position > sum_even_position:
            return (sum_odd_position)
        else:
            return (sum_even_position)

s = Solution()
print(s.rob([2,7,9,3,1]))
            

            