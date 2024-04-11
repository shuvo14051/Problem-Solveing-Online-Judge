import math 

class Solution:
    # time limit
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        summ = 1

        square_root = num//2 + 1
        for i in range(2, square_root):
            if num % i == 0:
                summ += i
        return summ == num
    
s = Solution()
print(s.checkPerfectNumber(7))