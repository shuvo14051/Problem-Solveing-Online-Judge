from typing import List 
import heapq

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums = sorted(nums, reverse=True)
#         return nums[k-1]

"""Without sorting"""
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]
    
s = Solution()
print(s.findKthLargest( nums = [3,2,1,5,6,4], k = 2))