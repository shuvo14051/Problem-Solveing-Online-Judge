from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = []
        second = []
        m = max(len(nums1), len(nums2))
        # Iterate over the longer list
        for i in range(m):
            if i < len(nums1) and nums1[i] not in nums2 and nums1[i] not in first:
                first.append(nums1[i])
            if i < len(nums2) and nums2[i] not in nums1 and nums2[i] not in second:
                second.append(nums2[i])
        
        return [first, second]

# Test the code
solution = Solution()

print(solution.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))
