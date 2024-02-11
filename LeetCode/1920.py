from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length
        for i in range(length):
            answer[i] = nums[nums[i]]
        return answer
    
s =  Solution()
print(s.buildArray([0,2,1,5,3,4]))