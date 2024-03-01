from typing import List 

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        li = []
        while nums:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            li.append(bob)
            li.append(alice)

        return li

s = Solution()
print(s.numberGame([5,4,2,3]))