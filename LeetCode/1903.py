class Solution:
    def largestOddNumber(self, num: str) -> str:
        index = len(num)
        while num:
            if int(num[-1]) % 2 != 0:
                return num
            index -= 1
            num = num[:index]
            
        return ""
    
s = Solution()
print(s.largestOddNumber("35427"))
