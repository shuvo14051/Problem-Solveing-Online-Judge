class Solution:
    def sumBase(self, n: int, k: int) -> int:
        li = []
        temp = n
        while temp>0:
            rem = temp % k
            li.append(rem)
            temp = temp // k

        return sum(li)