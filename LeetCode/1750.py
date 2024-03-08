class Solution:
    def minimumLength(self, s: str) -> int:
        while True:
            if s == "":
                break
            first = s[0]
            last = s[-1]
            if first == last:
                for i in range(len(s)):
                    if s[i] == first:
                        s = s.replace(s[i],"")
                        i+=1
        return s
    
s = Solution()
print(s.minimumLength("aabcassa"))
            