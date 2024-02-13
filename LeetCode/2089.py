from typing import List 

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        li = []
        for index, value in enumerate(nums):
            if value == target:
                li.append(index)

        return li