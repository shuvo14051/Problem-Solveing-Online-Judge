import re

class Solution:
    def myAtoi(self, s: str) -> int:
        min_val = -2147483648
        max_val = 2147483647
        s = s.strip()

        if re.search(r'^[a-zA-Z]', s):
            return 0

        if s == "":
            return 0

        s = re.findall(r'^[+-]?\d+', s)
        if s:
            s = s[0]
        else:
            return 0

        if s.startswith('-'):
            s = s[1:]
            int_val = int(s) * -1
        else:
            int_val = int(s)

        if int_val >= max_val:
            return max_val
        elif int_val <= min_val:
            return min_val

        return int_val

s = Solution()
print(s.myAtoi("42 shuvo ji ")) 