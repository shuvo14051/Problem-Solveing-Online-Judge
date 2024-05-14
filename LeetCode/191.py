class Solution:
    def hammingWeight(self, n: int) -> int:
        count = bin(n)[2:].count("1")
        return count
    
s = Solution()
print(s.hammingWeight(11))