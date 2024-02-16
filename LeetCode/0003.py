class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        li = []
        unique_li = []
        unique_str = ""
        for i in s:
            if i not in li:
                li.append(i)
                unique_str += i

            elif i in li:
                unique_li.append(unique_str)
                li = []

        return unique_li
    

s = Solution()  
print(s.lengthOfLongestSubstring("bbbbb"))