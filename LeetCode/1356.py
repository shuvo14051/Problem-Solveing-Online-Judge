from typing import List 

class Solution:
    def sort_by_ones(self, element):
        return element.count('1')
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        li = [bin(x)[2:] for x in arr]
        sorted_lst = sorted(li, key=self.sort_by_ones)
        int_li = [int(x,2) for x in sorted_lst]
        return int_li
    
s = Solution()
print(s.sortByBits([0,1,2,3,4,5,6,7,8]))