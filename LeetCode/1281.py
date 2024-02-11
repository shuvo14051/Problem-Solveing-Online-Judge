class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string_n = str(n)
        s = 0
        p = 1
        for i in string_n:
            s += int(i)
            p *= int(i)
        return p-s