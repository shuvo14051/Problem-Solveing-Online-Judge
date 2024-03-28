class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        val = 0
        for i in stones:
            if i in jewels:
                val += 1

        return val