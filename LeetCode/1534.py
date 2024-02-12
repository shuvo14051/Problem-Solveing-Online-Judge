from typing import List
import itertools

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        arr = list(itertools.combinations(arr,3))
        result = 0
        for i in arr:
            cond1 = abs(i[0] - i[1]) <= a
            cond2 = abs(i[1] - i[2]) <= b
            cond3 = abs(i[2] - i[0]) <= c

            if cond1 and cond2 and cond3:
                result += 1

        return result
    
s =Solution()
print(s.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))