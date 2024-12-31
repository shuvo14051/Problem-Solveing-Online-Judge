# import heapq

# class KthLargest:

#     def __init__(self, k, nums):
#         """
#         :type k: int
#         :type nums: List[int]
#         """
#         self.k = k
#         self.min_heap = nums
#         heapq.heapify(self.min_heap)  # Transform list into a heap in-place
#         # Maintain only the k largest elements in the heap
#         while len(self.min_heap) > k:
#             heapq.heappop(self.min_heap)

#     def add(self, val):
#         """
#         :type val: int
#         :rtype: int
#         """
#         heapq.heappush(self.min_heap, val)
#         # If the heap exceeds size k, remove the smallest element
#         if len(self.min_heap) > self.k:
#             heapq.heappop(self.min_heap)
#         # The smallest element in the heap is the kth largest element
#         return self.min_heap[0]

# # Example usage:
# kthLargest = KthLargest(3, [4, 5, 8, 2])
# print(kthLargest.add(3))  # return 4
# print(kthLargest.add(5))  # return 5
# print(kthLargest.add(10)) # return 5
# print(kthLargest.add(9))  # return 8
# print(kthLargest.add(4))  # return 8