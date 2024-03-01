class Solution:

    def to_base_n(self, num, base):
        if num == 0:
            return '0'
        digit = ''
        while num:
            digit = str(num % base) + digit
            num = num // base
        return digit
    
    def isStrictlyPalindromic(self, n: int) -> bool:
        low = 2
        high = (n-2) + 1
        for i in range(low, high):
            base = self.to_base_n(n, i)
            if base != base[::-1]:
                return False
            
        return True
    
s = Solution()
print(s.isStrictlyPalindromic(4))