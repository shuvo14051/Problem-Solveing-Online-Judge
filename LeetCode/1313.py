from typing import List 

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        start = 0
        end = 2
        output = []
        while end <= len(nums):
            pair = nums[start:end+1]
            output.extend([pair[1]]*pair[0])
            start += 2
            end += 2

        return output
    
s = Solution()
print(s.decompressRLElist([1,1,2,3]))