class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        li = []
        for i in range(n):
            li.append(start + (2*i))

        x_or = li[0]
        for i in li[1:]:
            x_or ^= i
        return x_or
    

    
s = Solution()
print(s.xorOperation(4,3))
