class Solution:
    def myAtoi(self, s: str) -> int:
        min_val = -2147483647
        max_val = 2147483647
        s = s.strip()
        digit_string = ""
        if s == "":
            return 0
        
        if s.startswith('-'):
            s = s.replace('-', '')
            int_val = int(s) *-1
            print("Negative  integer")
        
        else:
            print("Positive  integer")
            int_val = int(s)
            
        if int(s) >= max_val:
            return max_val - 1
        elif int(s) <= min_val:
            return min_val
        
        return int_val


s = Solution()
print(s.myAtoi("0"))