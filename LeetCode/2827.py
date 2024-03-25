
# Time limit
class Solution:

    def count_odd_even(self, number):
        return number.count('0') + number.count('2') + number.count('4') + number.count('6') + number.count('8') == len(number) // 2
    
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        li = []
        count = 0
        for i in range(low, high+1):
            if len(str(i)) %2 != 0:
                continue
            if i % k == 0 and self.count_odd_even(str(i)):
                count += 1
       
        return count
    

s = Solution()
print(s.numberOfBeautifulIntegers(228,273,3))