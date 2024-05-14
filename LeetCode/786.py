from typing import List 

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        li = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                li.append(str(arr[i]) + "/" + str(arr[j]))

        d = {}
        for item in li:
            numerator, denominator = map(int, item.split('/'))
            division = numerator / denominator
            d[division] = item
        d = dict(sorted(d.items()))
        vals = list(d.values())
        result = vals[k-1].split('/')
        result = list(map(int, result))
        return result
    

s = Solution()
print(s.kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3))