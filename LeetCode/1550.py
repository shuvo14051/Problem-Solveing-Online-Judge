from typing import List 

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        n = len(arr)
        for i in range(n):
            
            if arr[i] % 2 == 0:
                count = 0
            else:
                count += 1
                if count == 3:
                    return True
            

        return False
    

s = Solution()
print(s.threeConsecutiveOdds(arr = [1,1,1]))