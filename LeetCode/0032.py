class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count_li = []
        count = 0
        if s == "":
            return 0
        for i in range(1,len(s)):
            if s[i-1] == '(' and s[i] == ')':
                count += 2
            elif s[i-1] == '{' and s[i] == '}':
                count += 2
            elif s[i-1] == '[' and s[i] == ']':
                count += 2
            count_li.append(count)
            

        return max(count_li)
            


s = Solution()
print(s.longestValidParentheses(")()())"))