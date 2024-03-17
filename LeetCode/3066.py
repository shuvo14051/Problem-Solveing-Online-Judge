from typing import List 
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)  # Convert nums list to a min heap
        
        while True:
            if all(element >= k for element in nums):
                return count
            else:
                min1 = heapq.heappop(nums)
                min2 = heapq.heappop(nums)
                
                new_val = min1 * 2 + min2
                heapq.heappush(nums, new_val)
                count += 1

s = Solution()
print(s.minOperations(nums=[1,1,2,4,9], k=20))
