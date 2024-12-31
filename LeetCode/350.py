from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        s1 = Counter(nums1)
        s2 = Counter(nums2)

        # Determine the smaller counter to loop through
        if len(s1) < len(s2):
            smaller, larger = s1, s2
        else:
            smaller, larger = s2, s1

        # Loop through the smaller counter
        for key, value in smaller.items():
            if key in larger:
                min_count = min(value, larger[key])
                output.extend([key] * min_count)
        
        return output
    

s = Solution()
print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2,2]))
