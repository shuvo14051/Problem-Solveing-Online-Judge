from typing import List 
from math import *

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)

        return gcd(minimum, maximum)