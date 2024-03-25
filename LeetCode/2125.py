from typing import List 

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        d = {}
        index = 0
        total = 0
        for b in bank:
            d[index] = b.count("1")
            index += 1
        lasers = [val for val in d.values() if val>0]
        if len(lasers) <= 1:
            return 0
        for i in range (0, len(lasers)-1):

            total = total + (lasers[i] * lasers[i+1])
        return total
    
s = Solution()
print(s.numberOfBeams(["000","111","000"]))
