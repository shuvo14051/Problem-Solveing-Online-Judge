class Solution:
    # Memory limit
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        matrix = [[i*j for i in range(1,n+1)] for j in range(1,m+1)]
        li = []
        for row in matrix:
            li.extend(row)
        li = sorted(li)
        return li[k-1]
    
s = Solution()
print(s.findKthNumber(m = 2, n = 3, k = 6))


