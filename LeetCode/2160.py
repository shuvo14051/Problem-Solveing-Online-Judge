class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        li = list(num)
        li = sorted(li)
        s = int(li[0]+li[2]) + int(li[1]+li[3])

        return s
    
s = Solution()
print(s.minimumSum(2932))