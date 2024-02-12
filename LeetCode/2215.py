from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = []
        second = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                first.append(nums1[i])
            if nums2[i] not in nums1:
                second.append(nums2[i])
        
        return [first, second]
            
s = Solution()
print(s.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))