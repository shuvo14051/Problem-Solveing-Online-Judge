from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        li = [i for i in range(1,n+1)]
        permutation = list(permutations(li))
        k_th = list(permutation[k-1])
        output = "".join(str(i) for i in k_th)
        return output

s = Solution()
print(s.getPermutation(n = 3, k = 3))