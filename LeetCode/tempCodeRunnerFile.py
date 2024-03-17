from typing import List 

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subarrays = []
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subarrays.append(nums[i:j])

        for ar in subarrays:
            if sum(ar) % k == 0:
                count += 1
        return count

s = Solution()
print(s.subarraysDivByK([1,2,3,4], 4))