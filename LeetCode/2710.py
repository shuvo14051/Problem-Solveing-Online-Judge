class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while True:
            if num.endswith("0"):
                num = num[:-1]
            else:
                break

        return num

s = Solution()
print(s.removeTrailingZeros("510100"))