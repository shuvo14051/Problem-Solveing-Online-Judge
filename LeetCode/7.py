class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2147483647 or x <= -2147483647:
            return 0
        x = str(x)
        if x.startswith('-'):
            x = x.replace('-', '')
            reverse = int(x[::-1]) *-1
            if reverse <= -2147483647:
                return 0
            return reverse
            
        # if len(x)>1 and x.endswith('0'):
        #     x = x.replace('0', '')
        reverse = int(x[::-1])
        if reverse > 2147483647:
            return 0
        return int(reverse)
    

s = Solution()
print(s.reverse(1534236469))