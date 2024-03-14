class Solution:
    def capitalizeTitle(self, title: str) -> str:
        output = []
        li = title.split(' ')
        for i in li:
            if len(i)==1 or len(i)==2:
                output.append(i.lower())
            else:
                output.append(i.title())
        result = " ".join(output)
        return result
    

s = Solution()
print(s.capitalizeTitle("First leTTeR of EACH Word"))
        