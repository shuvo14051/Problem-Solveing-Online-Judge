class Solution:
    def numberOfMatches(self, n: int) -> int:
        m = 0
        t = n
        li = []
        while True:
            if n%2 == 0:
                t = t // 2
                m = t
                li.append(m)
                if t == 1:
                    break
            elif n%2 != 0:
                t = (t-1) // 2
                m = t+1
                li.append(m)
                if t == 1:
                    break
                t += 1
        return li
    
s = Solution()
print(s.numberOfMatches(14))