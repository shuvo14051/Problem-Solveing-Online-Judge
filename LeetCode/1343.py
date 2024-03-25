from typing import List 

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        for i in range(len(arr)-k+1):
            sub_array = arr[i:i+k]
            avg = sum(sub_array) // k
            if avg >= threshold:
                count += 1
        return count
    
s = Solution()
print(s.numOfSubarrays( arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))