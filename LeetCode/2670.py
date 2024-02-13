from typing import List 

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            unique_elements = set(nums[i+1:])
            unique_elements2 = set(nums[:i+1])

            num_elements = len(unique_elements)
            num_elements2 = len(unique_elements2)
            li.append(num_elements2 - num_elements)
        return li

s = Solution()
print (s.distinctDifferenceArray(nums = [3,2,3,4,2]))

# [-2,-1,0,2,3]
# [0,-1,1,3,2]
