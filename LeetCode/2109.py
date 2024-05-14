from typing import List 

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_index = 0
        result = ""
        for index, val in enumerate(s):
            if space_index < len(spaces) and index == spaces[space_index]:
                result += (" " + val)
                space_index += 1
                
            else:
                result+=val

        return result

s = Solution()
print(s.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))