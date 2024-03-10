class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  
            summ = 0
            string = str(num)
            for digit in string:
                summ += int(digit)
            num = summ  
        
        return num

s = Solution()
print(s.addDigits(38))