from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        s = 0
        for i in range(length):
            for j in range(i+1, length+1):
                if len(arr[i:j]) % 2 != 0:
                    s += sum(arr[i:j])
            
        return s

s = Solution()
print(s.sumOddLengthSubarrays([1,4,2,5,3]))