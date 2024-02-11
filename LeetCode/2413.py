class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        temp = n
        if n%2 == 0:
            return n
        else:
            while True:
                temp += n
                if temp % 2 == 0:
                    return temp

s = Solution()
print(s.smallestEvenMultiple(5))