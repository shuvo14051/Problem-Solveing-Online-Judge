from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = []
        for person in accounts:
            result.append(sum(person))

        return max(result)