class Solution:
    def convertDateToBinary(self, date: str) -> str:
        result = []
        date_li = date.split('-')
        for item in date_li:
            result.append(bin(int(item))[2:])
        return "-".join(result)
        
s = Solution()
print(s.convertDateToBinary("2080-02-29"))