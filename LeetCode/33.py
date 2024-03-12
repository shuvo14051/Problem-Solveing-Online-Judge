from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            index = nums.index(target)
            length = len(nums[:index])

        return length