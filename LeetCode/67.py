class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a,2)
        int_b = int(b,2)

        sum_a_b = int_a + int_b

        result = bin(sum_a_b)[2:]

        return result
    

s = Solution()
print(s.addBinary('1010','1011'))