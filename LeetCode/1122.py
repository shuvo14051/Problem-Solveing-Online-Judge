from typing import List 

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output = []
        rest = []
        for num in arr2:
            count = arr1.count(num)
            output += [num] * count
        for i in arr1:
            if i not in output:
                rest.append(i)
        output.extend(sorted(rest))

        return output
    
s = Solution()
print(s.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))