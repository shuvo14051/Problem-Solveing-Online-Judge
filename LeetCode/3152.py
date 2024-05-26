from typing import List
# time limit
class Solution:
    
    def checkQuery(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] % 2 == nums[i + 1] % 2):
                return False
        return True
    
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        output = []
        for query in queries:
            partition = nums[query[0]:query[1] + 1]
            res = self.checkQuery(partition)
            output.append(res)
        return output



from typing import List 
# time limit
class Solution:

    def checkPair(self, a, b):
        if a%2 == 0 and b%2 == 0:
            return False
        elif a%2 != 0 and b%2 != 0:
            return False
        else:
            return True
        
    def checkQuery(self, nums: List[int]) -> bool:
        output = True
        pairs = []
        if len(nums) == 1:
            return True
            
        for i in range(len(nums)-1):
            pairs.append((nums[i], nums[i+1]))

        for pair in pairs:
            pari_check = self.checkPair(pair[0], pair[1])
            if not pari_check:
                return False
            
        return True
    
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        output = []
        for query in queries:
            partition = nums[query[0]:query[1]+1]
            res = self.checkQuery(partition)

            output.append(res)

        return output
    

s = Solution()
print(s.isArraySpecial(nums = [4,3,1,6], queries = [[0,2],[2,3]]))

    