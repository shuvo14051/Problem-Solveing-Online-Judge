class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)
        li = [x+extraCandies >= greatest for x in candies]
        return li
    
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))
        