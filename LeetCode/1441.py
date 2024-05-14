from typing import List 

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        last_target = 0
        for i in range(1,n+1):
            if last_target == len(target):
                break
            if i in target:
                result.append("Push")
                last_target += 1
            else:
                result.extend(["Push", "Pop"])

        return result