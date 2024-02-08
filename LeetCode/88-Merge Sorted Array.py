class Solution:
    def merge(self, nums1, m: int, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1 = nums1[:m]
        # print(li1)
        li2 = nums2[:n]
        # print(li2)
        num1 = num1+li2
        sorted(num1)
s = Solution()
s.merge([1,2,3,0,0,0],3,[2,5,6],3)