from typing import List
# time limit 
class Solution:
    """
    def countSubarrays(self, nums: List[int], k: int) -> int:
        subarrays = []
        count = 0
        m = max(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                subarrays.append(nums[i:j])

        for ar in subarrays:
            if ar.count(m) <= k:
                count += 1

        return count

    """

    # 

    """
    def countSubarrays(self, nums: List[int], k: int) -> int:
        subarrays = []
        count = 0
        m = max(nums)
        n = len(nums)
        for length in range(1, n+1):
            for start in range(n - length + 1):
                sub = nums[start:start + length]
                if sub.count(m) >=k:
                    count += 1

        return count
    """
    
s = Solution()
print(s.countSubarrays(nums = [1,3,2,3,3], k = 2))