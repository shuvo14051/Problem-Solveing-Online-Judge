class Solution:
    def uniqueOccurrences(self, arr):
        occurance = set()
        for i in arr:
            occurance.add(arr.count(i))
        if len(occurance) == 1:
            return False
        else:
            return True
        
s = Solution()
print(s.uniqueOccurrences([1,2,3]))