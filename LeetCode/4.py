class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        median = 0.0
        li = nums1 + nums2
        length = len(li)
        mid = length // 2
        li = sorted(li)

        if length % 2 == 0:
            median = (li[mid-1] + li[mid])/2
        else:
            median = li[mid]
    
        return float(median)
    

s = Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))
        