from typing import List 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        s = nums1.intersection(nums2)

        return list(s)
    

s = Solution()
print(s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))