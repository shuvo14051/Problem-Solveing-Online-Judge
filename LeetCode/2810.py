class Solution:
    def finalString(self, s: str) -> str:
        output = ""
        for i in s:
            if i != "i":
                output += i
            else:
                output = output [::-1]
        return output


s  = Solution()
print(s.finalString("string"))