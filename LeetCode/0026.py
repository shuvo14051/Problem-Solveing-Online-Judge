from collections import Counter
class Solution:
    def removeDuplicates(self, nums):
        # counter = Counter(nums)
        # result = 0
        # for num, count in counter.items():
        #     result += (count - 1)

        # return result
        n = set(nums)
        return list(n)
    

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
        