from typing import List 

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        s = 0
        for num in nums:
            if num < 10:
                s += num
            else:
                string_num = str(num)
                sorted_str_num = "".join(sorted(string_num))[-1]
                encripted_num = int(sorted_str_num*len(string_num))
                s+=encripted_num
        return s

s = Solution()
print(s.sumOfEncryptedInt([1,2,3]))