class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        li = []
        for i in range(1,n+1):
            if n%i == 0:
                li.append(i)
        if k <= len(li):
            return li[k-1]
        return -1
    
s = Solution()
print(s.kthFactor(7,2))