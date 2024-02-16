class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l, r, u, d = 0, 0, 0, 0
    
        for i in moves:
            if i == "L":
                l -= 1
            elif i == "R":
                l += 1
            elif i == "U":
                u += 1
            elif i == "D":
                u -= 1

        if l == 0 and r == 0 and u == 0 and d == 0:
            return True
        else:
            return False
        
s = Solution()
print(s.judgeCircle("LL"))
        