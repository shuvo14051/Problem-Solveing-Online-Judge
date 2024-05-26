from typing import List 

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result =  set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)
        return list(result)
    
s = Solution()
print(s.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))