from typing import List 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = []
        for index, value in enumerate(nums):
            if value == target:
                output.append(index)
        if not output:
            return [-1,-1]
        elif len(output) == 1:
            return output*2
        elif len(output) > 2:
            return[output[0], output[-1]]
        else:
            return output

s = Solution()
print(s.searchRange( nums = [5,7,7,8,8,10], target = 8))