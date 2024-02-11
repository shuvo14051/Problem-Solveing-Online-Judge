import itertools
class Solution:
    def minimumSum(self, num: int) -> int:
        li = [ch for ch in str(num)]
        s = list(set(li))
        comb = itertools.combinations_with_replacement(s, 2)
        return list(comb)
    
s = Solution()
print(s.minimumSum(2932))