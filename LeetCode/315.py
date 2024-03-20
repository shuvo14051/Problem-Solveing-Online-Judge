from typing import List 

# Time limit exceeded

"""
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(len(nums)):
            count = 0
            sub = nums[i+1: ]
            for j in sub:
                if j<nums[i]:
                    count += 1
            li.append(count)

        return li
    
s = Solution()
print(s.countSmaller(nums = [5,2,6,1]))

"""