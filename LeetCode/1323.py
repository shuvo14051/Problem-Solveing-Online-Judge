class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for i in range(len(s)):
            if s[i] == "6":
                s = s.replace(s[i],'9',1)
                break

        return int(s)
    
s = Solution()
print(s.maximum69Number(9669))