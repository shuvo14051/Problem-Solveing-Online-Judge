from typing import List 

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_of_num = 0
        sum_of_digit = 0
        for num in nums:
            s = 0
            sum_of_num += num
            if num < 10:
                sum_of_digit += num
            else:
                while num:
                    s += num%10
                    num = num // 10
                sum_of_digit += s

        return abs(sum_of_num-sum_of_digit)
    

s = Solution()
print(s.differenceOfSum([1,15,6,3]))