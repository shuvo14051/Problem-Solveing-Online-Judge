class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in  nums:
            if i == val:
                nums.remove(i)
            else:
                count += 1
        # sorted_list = sorted(nums, reverse=True,key=lambda x: (isinstance(x, int), x))
        return nums
    

s = Solution()
print(s.removeElement([2, 3, 3, 2], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

        