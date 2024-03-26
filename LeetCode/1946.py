from typing import List
# Wrong answer
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        result = ""
        changed = False  
        
        for digit in num:
         
            if int(digit) < change[int(digit)]:
                result += str(change[int(digit)])
                changed = True  
            else:
                if not changed:
                    result += digit
                else:
                    break  
        
        result += num[len(result):]
        
        return result


# Wrong ans on case 1
"""
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        result = ""
        for digit in num:
            if int(digit) < change[int(digit)]:
                result += str(change[int(digit)])
            else:
                result += digit
        return result
"""