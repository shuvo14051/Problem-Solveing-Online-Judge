from typing import List 

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []
        output = []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            elif i > pivot:
                right.append(i)

        output = left + middle + right
        return output
    
s = Solution()
print(s.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))