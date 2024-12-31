from typing import List 

class Solution:
    def arrayRankTransform(self, arr: List[int]):
        sorted_arr = sorted(list(set(arr)))
        d = {}
        result = []
        for i in range (len(sorted_arr)):
            d[sorted_arr[i]] = i+1

        for key in arr:
            if key in d:
                result.append(d[key])

        return result
    
s =  Solution()
print(s.arrayRankTransform([100,100,100]))