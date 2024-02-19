from typing import List 

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for li in items:
            if ruleKey == "type" and li[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and li[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and li[2] == ruleValue:
                count += 1

        return count