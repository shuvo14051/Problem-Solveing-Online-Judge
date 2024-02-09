from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = nums.count(0)
        print(count_0)
        for i in nums:
            print(i)
            if i == 0:
                nums.remove(0)
        print(nums)
        nums += [0]*count_0
        print(nums)

s = Solution()
s.moveZeroes([0,0])