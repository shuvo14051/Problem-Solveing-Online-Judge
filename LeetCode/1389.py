from typing import List 
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
      idx = 0
      result = []
      for i in index:
        result.insert(i,nums[idx])
        idx+=1
      return result