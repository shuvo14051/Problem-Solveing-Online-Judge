class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR can be used to solve this problem
        # If there is a difference between bits that will become 1
        # We will just count the number of 1 after XOR
        x_or = x^y
        binary = bin(x_or)[2:]
        result = binary.count("1")
        return result
 
s = Solution()
print(s.hammingDistance(x = 3, y = 1))


"""
class Solution:
    # wrong answer
    def hammingDistance(self, x: int, y: int) -> int:
        m = max(x,y)
        x = format(x, 'b').zfill(m)
        y = format(y, 'b').zfill(m)
        count = 0
        for i in range(m):
            if x[i] != y[i]:
                count += 1

        return count
"""