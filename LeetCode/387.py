class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for key, value in d.items():
            if value == 1:
                return s.index(key)
        return -1
    
s = Solution()
print(s.firstUniqChar("aabb"))