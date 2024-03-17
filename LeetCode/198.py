from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        sum_odd_position = 0
        sum_even_position = 0

        possible_values = []

        if len(nums) == 3 or len(nums) == 4:
            possible_values.append(nums[0] + nums[-1])

        for index, value in enumerate(nums):
            if index % 2 == 0:
                sum_even_position += value
            else:
                sum_odd_position += value

        possible_values.append(sum_even_position)
        possible_values.append(sum_odd_position)

        return max(possible_values)

s = Solution()
print(s.rob([2,1,1,2]))
            

            