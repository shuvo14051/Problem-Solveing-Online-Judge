class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix of left and right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

s = Solution()
print(s.rangeBitwiseAnd(left = 1, right = 2147483647))