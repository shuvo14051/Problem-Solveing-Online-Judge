class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]

        reversed_bit = ""
        for i in binary:
            if i == "0":
                reversed_bit += "1"
            elif i == "1":
                reversed_bit += "0"
        complement = int(reversed_bit,2)
        
        return complement
    
s = Solution()
print(s.findComplement(5))