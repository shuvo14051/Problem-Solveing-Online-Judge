from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for index in range(len(nums)):
            bin_num = bin(index)[2:]
            if bin_num.count("1") == k:
                s += nums[index]

        return s
    
s = Solution()
print(s.sumIndicesWithKSetBits([5,10,1,5,2], 1))