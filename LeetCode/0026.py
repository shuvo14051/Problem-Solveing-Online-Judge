from collections import Counter
class Solution:
    def removeDuplicates(self, nums):
        
        n = sorted(list(set(nums)))
        return len(n), n
    

s = Solution()
print(s.removeDuplicates([1,1,2]))
        