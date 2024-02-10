from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result  = []
        for i in nums:
            if i>0:
                positive.append(i)
            else:
                negative.append(i)
        
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result
    
s = Solution()

print(s.rearrangeArray([3,1,-2,-5,2,-4]))