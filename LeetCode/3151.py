from typing import List

class Solution:

    def checkPair(self, a, b):
        if a%2 == 0 and b%2 == 0:
            return False
        elif a%2 != 0 and b%2 != 0:
            return False
        else:
            return True
        
    def isArraySpecial(self, nums: List[int]) -> bool:
        output = True
        pairs = []
        if len(nums) == 1:
            return True
            
        for i in range(len(nums)-1):
            pairs.append((nums[i], nums[i+1]))

        for pair in pairs:
            pari_check = self.checkPair(pair[0], pair[1])
            if not pari_check:
                return False
            
        return True


        
s = Solution()
print(s.isArraySpecial([1,3,2,4]))