class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        s = 0
        while temp:
            s+= temp % 10
            temp = temp // 10

        if x%s == 0:
            return s
        return  -1
    
s = Solution()
print(s.sumOfTheDigitsOfHarshadNumber(23))