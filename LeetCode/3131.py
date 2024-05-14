from typing import List 

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # num1 = sorted(nums1)
        # num2 = sorted(nums2)

        # return num1

        return min(nums2) -  min(nums1)
    
s = Solution()
print(s.addedInteger(nums1 = [2,6,4], nums2 = [9,7,5]))