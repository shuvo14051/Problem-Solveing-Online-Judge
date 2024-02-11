from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xs = nums[:n]
        ys = nums[n:]
        final_li = []
        for i in range(n):
            final_li.append(xs[i])
            final_li.append(ys[i])

        return final_li
    
s = Solution()
print(s.shuffle([1,2,3,4,4,3,2,1], 4))