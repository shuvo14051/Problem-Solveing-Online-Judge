class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2, num+1):
            summ = 0
            for j in str(i):
                summ += int(j)
            if summ %2 == 0:
                count += 1
        return count
