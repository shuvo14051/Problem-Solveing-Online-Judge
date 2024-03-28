from typing import List 

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        li = []
        for i in strs:
            li.append(list(i))
        print(li)
        li = list(map(list, zip(*li)))

        for i in li:
            if i != sorted(i):
                count += 1

        return count
    
s = Solution()
print(s.minDeletionSize(["cba","daf","ghi"]))