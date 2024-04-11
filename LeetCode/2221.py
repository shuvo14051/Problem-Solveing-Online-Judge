class Solution:
    def triangularSum(self, nums):
        while len(nums) > 1:
            new_nums = [(nums[i] + nums[i+1]) % 10 for i in range(len(nums) - 1)]
            nums = new_nums
        return nums[0]

