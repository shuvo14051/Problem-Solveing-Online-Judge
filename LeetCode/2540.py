from typing import List 

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1) 
        s2 = set(nums2)
        intersect = s1.intersection(s2)
        if not intersect:
            return -1
        else:
            return min(intersect)