class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        li = []
        i = 2
        while len(li) < n:
            if i % a==0 or i % b==0 or i % c==0:
                li.append(i)
            i+=1
        result = li[-1]
        return result
    
s = Solution()
print(s.nthUglyNumber(n = 5, a = 2, b = 11, c = 13))