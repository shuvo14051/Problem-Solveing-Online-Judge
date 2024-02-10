class Solution:
    def productExceptSelf(self, nums):
        mul = 1
        for i in nums:
            mul = mul * i

        li = [0]*len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                li[i]  = mul // nums[i]
        return li

s = Solution()
print(s.productExceptSelf([1,2,3,4,0]))
            