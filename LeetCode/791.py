class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = ""
        for i in order:
            if i in s:
                if s.count(i) == 1:
                    output += i
                    s = s.replace(i,"")
                else:
                    output += (i*s.count(i))
                    s = s.replace(i,"")

        sorted_s = sorted(s)
        s = "".join(sorted_s)
        output += s
        
        return output
    
s = Solution()
print(s.customSortString(order = "hucw", s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh" ))