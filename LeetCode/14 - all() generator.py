class Solution:
    def longestCommonPrefix(self, strs):
        res = ''
        smallest = sorted(strs, key=len)[0]

        for i in range(len(smallest)):
            if all(string[i] == smallest[i] for string in strs):
                res += smallest[i]
            else:
                break

        return res


s = Solution()
print(s.longestCommonPrefix(["car",'ca']))