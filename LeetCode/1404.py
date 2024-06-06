class Solution:
    def numSteps(self, s: str) -> int:
        integer = int(s, 2)
        print(integer)
        count = 0
        if integer == 1:
            return 0
        while integer !=1:
            if integer % 2 == 0:
                integer //= 2
                count += 1
            elif integer % 2 != 0:
                integer += 1    
                count += 1
            
        return count
    
s = Solution()
print(s.numSteps("1111011110000011100000110001011011110010111001010111110001"))