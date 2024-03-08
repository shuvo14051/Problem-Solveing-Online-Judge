class Solution:
    def removeElement(self, nums, val):
        for i in nums[:]: 
            if i == val:
                nums.remove(i)
        return len(nums)
        



s = Solution()
print(s.removeElement([2, 3, 3, 2], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

        