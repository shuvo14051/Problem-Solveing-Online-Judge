from typing import List 

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        li = []
        i = 1

        while True:
            if i not in arr:
                li.append(i)
            i += 1 
            if len(li) == k:
                break
        print(li)
        return li[k-1]
    
s = Solution()
print(s.findKthPositive(arr = [2,3,4,7,11], k = 5))