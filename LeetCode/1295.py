from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            s = str(i)
            if len(s) % 2 == 0:
                count += 1


        return count